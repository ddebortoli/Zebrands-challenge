import unittest
import requests

class TestProductos(unittest.TestCase):
    # setup and teardown methods
    def create_app(self):
        # create a test app
        pass

    def setUp(self):
        self.base_url = "http://localhost:8006/api"
        self.product_ids = [1, 2, 3]
        self.products = [
            {
                "amount": 10,
                "brand": "Brand 1",
                "name": "Product 1",
                "price": 20.5,
                "sku": "SKU1"
            },
            {
                "amount": 15,
                "brand": "Brand 2",
                "name": "Product 2",
                "price": 30.5,
                "sku": "SKU2"
            }
        ]

    def tearDown(self):
        pass

    def test_get_products(self):
        # Test GET request to /Productos
        response = requests.get(f"{self.base_url}/Productos", params={"id": self.product_ids})
        self.assertEqual(response.status_code, 200)
        # check the response data

    def test_create_products(self):
        # Test POST request to /Productos
        headers = {"Content-Type": "application/json", "Authorization": "Basic VGVzdDI6NDUwMA=="}
        response = requests.post(f"{self.base_url}/Productos", json={"products": self.products}, headers=headers)
        self.assertEqual(response.status_code, 201)
        # check the response data

    def test_update_products(self):
        # Test PUT request to /Productos
        headers = {"Content-Type": "application/json", "Authorization": "Basic VGVzdDI6NDUwMA=="}
        response = requests.put(f"{self.base_url}/Productos", json={"products": self.products}, headers=headers)
        self.assertEqual(response.status_code, 200)
        # check the response data

    def test_delete_products(self):
        # Test DELETE request to /Productos
        headers = {"Content-Type": "application/json", "Authorization": "Basic VGVzdDI6NDUwMA=="}
        response = requests.delete(f"{self.base_url}/Productos", json={"products": self.products}, headers=headers)
        self.assertEqual(response.status_code, 200)
        # check the response data

if __name__ == '__main__':
    unittest.main()