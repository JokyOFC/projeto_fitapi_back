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
                '../API/Integracao/insert'
            )
        )
    )
except:
    raise

import unittest
from fastapi.testclient import TestClient
from create_product import app

client = TestClient(app)


class TestProduct(unittest.TestCase):
    def test_create_product(self):
        # Teste para criar um produto
        product_data = {
            "name": "Produto 1",
            "description": "Descrição do Produto 1",
            "code": "PRD-001",
            "dimensions": "10x20x30",
            "value": 100.0
        }
        response = client.post("/create/product/", json=product_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Ok"})
    
            

if __name__ == '__main__':
    unittest.main(verbosity=2)