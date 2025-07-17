import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client(use_cookies=False)

    def test_random_joke_route(self):
        res = self.client.get("/joke/random")

        self.assertEqual(res.status_code, 200)

    def test_joke_with_id(self):
        res = self.client.get("/joke/3")
        self.assertEqual(res.status_code, 200)

    def test_create_joke(self):
        new_joke = {"joke": "Nigeria my country"}
        res = self.client.post("/joke/create", json=new_joke)

        self.assertEqual(res.status_code, 201)
        self.assertIn(b"data", res.data)
        self.assertIn(b"message", res.data)


if __name__ == "__main__":
    unittest.main()
