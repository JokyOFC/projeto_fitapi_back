# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:27:29 2023

@author: Evertonaa
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from schema.schema import Product
import asyncpg
from timeout_decorator import timeout, TimeoutError

app = FastAPI()

@timeout(10)
@app.post("/create/product/")
async def create_product(product: Product):
    conn = None
    try:
        conn = await asyncpg.connect(user='everton',
                                     password='admin', 
                                     database='banco_legal', 
                                     host='localhost')
        
        values = (product.name, product.description,
                  product.code, product.empresa,
                  product.dimensions, product.value)
        
        await conn.execute("INSERT INTO products (name, description, code, empresa, dimensions, value) VALUES ($1, $2, $3, $4, $5, $6)", *values)
        return {"message": "Ok"}
    
    except asyncpg.exceptions.PostgresError as e:
        return {"message": f"Error {e}"}
        
    except TimeoutError as e:
        return {"message": f"Error {e}"}
        
    finally:
        await conn.close()
        




