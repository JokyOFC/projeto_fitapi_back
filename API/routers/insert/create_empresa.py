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
from schema.schema import empresa
from connection.conexao import get_database_connection


router = APIRouter()


@timeout(10)
@router.post("/create/empresa/")
async def create_product(empresa: empresa):
    conn = None
    try:
        conn = await get_database_connection()

        values = (empresa.nome_fantasia, empresa.razao_social,
                  empresa.email, empresa.cnpj)

        query = "INSERT INTO empresa (nome_fantasia, razao_social, email, cnpj) VALUES ($1, $2, $3, $4)"
        await conn.execute(query, *values)
        return {"message": "Empresa criada com sucesso!"}

    except PostgresError as e:
        return {"message": f"Error {e}"}

    except TimeoutError as e:
        return {"message": f"Error {e}"}

    except HTTPException as e:
        return {"message": f"Error {e}"}

    finally:
        await conn.close()
