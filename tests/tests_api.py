# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:33:19 2023

@author: Everton
"""

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../API'
            )
        )
    )
except:
    raise

import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAPI(unittest.TestCase):

    def test_create_product(self):
        response = client.post("/create/product/", json={
            "name": "Product 1",
            "description": "Product 1 description",
            "code": "123456",
            "empresa": "Company 1",
            "dimensions": "10x20x30",
            "value": 100.0
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Ok"})

    def test_select_product(self):
        response = client.get("/select/products/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "id": 1,
            "name": "Product 1",
            "description": "Product 1 description",
            "code": "123456",
            "empresa": "Company 1",
            "dimensions": "10x20x30",
            "value": 100.0
        })

    def test_delete_product(self):
        response = client.delete("/delete/products/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Product deleted"})


if __name__ == '__main__':
    unittest.main()