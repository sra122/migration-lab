import unittest
from app import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting_mentions_migration_lab(self):
        self.assertIn("migration lab", greeting())


if __name__ == "__main__":
    unittest.main()
