"""Standard-library unittest suite; never contacts external hosts."""
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from examples.archive_inspector import inspect_zip, suspicious_name
from examples.binary_triage import classify_magic, entropy, analyze
from examples.file_manifest import manifest, sha256_path
from examples.indicator_normalizer import normalize_ip, records
from examples.local_port_check import check_port
from examples.log_detector import detect, parse_event
from examples.sqlite_safety_demo import find_roles


class ManifestTests(unittest.TestCase):
    def test_known_sha(self):
        with tempfile.TemporaryDirectory() as temporary:
            p = Path(temporary) / "message.txt"
            p.write_bytes(b"abc")
            self.assertEqual(sha256_path(p),
                             "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_inventory(self):
        with tempfile.TemporaryDirectory() as temporary:
            p = Path(temporary) / "a.txt"
            p.write_text("safe", encoding="utf-8")
            output = list(manifest(Path(temporary)))
            self.assertEqual(len(output), 1)
            self.assertEqual(output[0]["path"], "a.txt")

    def test_limits(self):
        with self.assertRaises(ValueError):
            list(manifest(Path("."), limit_files=0))


class AuthTests(unittest.TestCase):
    def test_parse_requires_timezone(self):
        with self.assertRaises(ValueError):
            parse_event('{"timestamp":"2026-01-01T00:00:00","actor":"a","action":"login_failure"}')

    def test_bad_json(self):
        with self.assertRaises(ValueError):
            parse_event("not json")

    def test_trigger_once(self):
        rows = [
            json.dumps({"timestamp": f"2026-01-01T00:0{i}:00Z",
                        "actor": "a", "action": "login_failure"})
            for i in range(4)
        ]
        alerts = list(detect(rows, threshold=3))
        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["failure_count"], 3)

    def test_out_of_order(self):
        rows = [
            '{"timestamp":"2026-01-01T00:01:00Z","actor":"a","action":"login_failure"}',
            '{"timestamp":"2026-01-01T00:00:00Z","actor":"a","action":"login_failure"}'
        ]
        with self.assertRaises(ValueError):
            list(detect(rows))

    def test_reset_window(self):
        times = ["00:00:00", "00:00:01", "00:00:02",
                 "00:10:00", "00:10:01", "00:10:02"]
        rows = [json.dumps({"timestamp": f"2026-01-01T{t}Z",
                            "actor": "a", "action": "login_failure"}) for t in times]
        self.assertEqual(len(list(detect(rows, threshold=3, window_seconds=60))), 2)


class NetworkTests(unittest.TestCase):
    def test_invalid_ports(self):
        for port in (-1, 0, 65536, True):
            with self.subTest(port=port), self.assertRaises(ValueError):
                check_port(port)


class BinaryTests(unittest.TestCase):
    def test_entropy_empty(self):
        self.assertEqual(entropy(b""), 0.0)

    def test_entropy_repeated(self):
        self.assertEqual(entropy(b"AAAA"), 0.0)

    def test_entropy_balanced(self):
        self.assertAlmostEqual(entropy(b"ABAB"), 1.0)

    def test_magic(self):
        self.assertEqual(classify_magic(b"%PDF-1.4"), "PDF")

    def test_file_sample(self):
        with tempfile.TemporaryDirectory() as temporary:
            p = Path(temporary) / "sample.txt"
            p.write_bytes(b"AAAAAAAA")
            self.assertEqual(analyze(p)["sample_size"], 8)


class IntelTests(unittest.TestCase):
    def test_ip(self):
        self.assertEqual(normalize_ip("2001:0db8::1"), "2001:db8::1")

    def test_bad_ip(self):
        with self.assertRaises(ValueError):
            normalize_ip("not-an-ip")

    def test_dedup_by_source(self):
        item = '{"indicator":"192.0.2.5","source":"toy"}'
        self.assertEqual(len(list(records([item, item]))), 1)


class DatabaseTests(unittest.TestCase):
    def test_parameterized(self):
        self.assertEqual(find_roles("alice"), ["reader"])
        self.assertEqual(find_roles("alice' OR '1'='1"), [])


class ZipTests(unittest.TestCase):
    def test_unsafe_paths(self):
        self.assertTrue(suspicious_name("../outside"))
        self.assertTrue(suspicious_name("/absolute"))
        self.assertTrue(suspicious_name("C:\\outside"))
        self.assertFalse(suspicious_name("safe/subdir"))

    def test_zip_inspection(self):
        with tempfile.TemporaryDirectory() as temporary:
            p = Path(temporary) / "sample.zip"
            with zipfile.ZipFile(p, "w") as zf:
                zf.writestr("../outside", "demo")
            flagged = inspect_zip(p)
            self.assertEqual(flagged[0]["reasons"], ["unsafe-path"])


if __name__ == "__main__":
    unittest.main()
