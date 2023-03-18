# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:27:29 2023

@author: Evertonaa
"""

from fastapi import FastAPI
from pydantic import BaseModel
import asyncpg
from timeout_decorator import timeout, TimeoutError


class Product(BaseModel):
    name: str
    description: str
    code: str
    dimensions: str
    value: float

app = FastAPI()

@timeout(10)
@app.post("/create/product/")
async def create_product(product: Product):
    try:
        conn = await asyncpg.connect(user='everton',
                                     password='admin', 
                                     database='banco_legal', 
                                     host='localhost')
        
        values = (product.name, product.description, product.code, product.dimensions, product.value)
        await conn.execute("INSERT INTO products (name, description, code, dimensions, value) VALUES ($1, $2, $3, $4, $5)", *values)
        return {"message": "Ok"}
    
    except asyncpg.exceptions.PostgresError as e:
        return {"message": f"Error {e}"}
        
    except TimeoutError as e:
        return {"message": f"Error {e}"}
        
    finally:
        await conn.close()
        




