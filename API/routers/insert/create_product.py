# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:27:29 2023

@author: Evertonaa
"""
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '....')))

from timeout_decorator import timeout, TimeoutError
from fastapi import APIRouter, HTTPException
from asyncpg.exceptions import PostgresError
from schema.schema import Product
from connection.conexao import get_database_connection


router = APIRouter()


@timeout(10)
@router.post("/create/product/")
async def create_product(product: Product):
    conn = None
    try:
        conn = await get_database_connection()

        values = (product.name, product.description,
                  product.code, product.empresa,
                  product.dimensions, product.value)

        query = "INSERT INTO products (name, description, code, empresa, dimensions, value) VALUES ($1, $2, $3, $4, $5, $6)"
        await conn.execute(query, *values)
        return {"message": "Ok"}

    except PostgresError as e:
        return {"message": f"Error {e}"}

    except TimeoutError as e:
        return {"message": f"Error {e}"}

    except HTTPException as e:
        return {"message": f"Error {e}"}

    finally:
        await conn.close()
