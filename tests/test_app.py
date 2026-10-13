import unittest
from app import greeting, health_payload


class AppTests(unittest.TestCase):
    def test_greeting(self):
        self.assertIn("migration lab", greeting())

    def test_health_payload(self):
        self.assertEqual(health_payload()["status"], "ok")
        self.assertEqual(health_payload()["service"], "migration-lab")


if __name__ == "__main__":
    unittest.main()
