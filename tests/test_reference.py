"""Small executable smoke tests; they do not establish full UL-xDFD conformance."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ReferenceExampleTests(unittest.TestCase):
    def test_synthetic_example_passes_existing_structural_validator(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'tools/validate.py'),
             str(ROOT / 'examples/hotel-ai.yaml'),
             str(ROOT / 'schemas/ul-xdfd-ai-v1.schema.json')],
            text=True, capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('PASS:', result.stdout)

if __name__ == '__main__':
    unittest.main()
