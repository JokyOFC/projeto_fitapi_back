import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '...')))

from connection.conexao import get_database_connection
from asyncpg.exceptions import PostgresError
from timeout_decorator import timeout, TimeoutError
from fastapi import APIRouter, HTTPException
# from schema.schema import Product

router = APIRouter()

@timeout(10)
@router.get("/select/produto/{product_id}")
async def read_produto(product_id: int):
    conn = None
    # try:
    #     # conn = await get_database_connection()
    #     # query = "SELECT * FROM produto WHERE produtos_id = $1"
    #     # result = await conn.fetchrow(query, product_id)
    #     # if result is None:
    #     #     raise HTTPException(status_code=404, detail="produto not found")
    #     # return Product(**result)

    # except PostgresError as e:
    #     return {"message": f"Error {e}"}

    # except TimeoutError as e:
    #     return {"message": f"Error {e}"}

    # finally:
    #     await conn.close()
