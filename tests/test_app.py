import unittest
from app import health_payload


class HealthPayloadTests(unittest.TestCase):
    def test_health_payload_has_ok_status(self):
        self.assertEqual(health_payload()["status"], "ok")

    def test_health_payload_has_service_name(self):
        self.assertEqual(health_payload()["service"], "migration-lab")


if __name__ == "__main__":
    unittest.main()
