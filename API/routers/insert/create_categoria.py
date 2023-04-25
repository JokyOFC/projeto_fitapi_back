# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 00:17:29 2023

@author: JokyOFC
"""
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '....')))

from timeout_decorator import timeout, TimeoutError
from fastapi import APIRouter, HTTPException
from asyncpg.exceptions import PostgresError
from schema.schema import categoria
from connection.conexao import get_database_connection


router = APIRouter()


@timeout(10)
@router.post("/create/categoria/")
async def create_product(categoria: categoria):
    conn = None
    try:
        conn = await get_database_connection()

        values = (categoria.nome)

        query = "INSERT INTO categoria (nome) VALUES ($1)"
        await conn.execute(query, values)
        return {"message": "Ok"}

    except PostgresError as e:
        return {"message": f"Error {e}"}

    except TimeoutError as e:
        return {"message": f"Error {e}"}

    except HTTPException as e:
        return {"message": f"Error {e}"}

    finally:
        await conn.close()
