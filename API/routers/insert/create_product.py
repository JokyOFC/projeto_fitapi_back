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
from schema.schema import Product, empresa, categoria
from connection.conexao import get_database_connection


router = APIRouter()


@timeout(10)
@router.post("/create/product/")
async def create_product(produto: Product):
    conn = None
    try:
        conn = await get_database_connection()

        values = (produto.nome, produto.preco,
                  produto.descricao, produto.codigo,
                  produto.is_Published, produto.categoria_categoria_fk,
                  produto.empresa_empresa_fk)

        

        ver_emp = "SELECT empresa_id FROM empresa WHERE empresa_id = $1"

        ver_cat = "SELECT categoria_id FROM categoria WHERE categoria_id = $1"

        empresa = await conn.fetchrow(ver_emp, produto.empresa_empresa_fk)
        categoria = await conn.fetchrow(ver_cat, produto.categoria_categoria_fk)

        # return{ "message": values, "comando_1": empresa, "comando_2": categoria }

        if empresa is None:
            raise HTTPException(status_code=404, detail="empresa not found")
        elif categoria is None:
             raise HTTPException(status_code=404, detail="categoria not found")

        query = "INSERT INTO produto (nome, descricao, codigo, empresa_empresa_fk, preco,  is_published, categoria_categoria_fk ) VALUES ($1, $2, $3, $4, $5, $6, $7)"
        await conn.execute(query, *values)
        return {"message": "Produto inserido com sucesso"}

    except PostgresError as e:
        return {"message": f"Error {e}"}

    except TimeoutError as e:
        return {"message": f"Error {e}"}

    except HTTPException as e:
        return {"message": f"Error {e}"}

    finally:
        await conn.close()
