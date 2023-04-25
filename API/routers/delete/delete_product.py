
from fastapi import APIRouter, HTTPException
from timeout_decorator import timeout, TimeoutError     
from asyncpg.exceptions import PostgresError
from connection.conexao import get_database_connection   


router = APIRouter()
        
@timeout(10)        
@router.delete("/delete/products/{product_id}")
async def delete_product(product_id: int):
    conn = None
    # try:
    #     # conn = await get_database_connection()
    #     # query = "DELETE FROM produto WHERE produtos_id  = $1"
    #     # result = await conn.execute(query, product_id)
    #     # if result == "DELETE 0":
    #     #     raise HTTPException(status_code=404, detail="Product not found")
    #     # return {"message": "Product deleted"}
    
    # except PostgresError as e:
    #     return {"message": f"Error {e}"}
        
    # except TimeoutError as e:
    #     return {"message": f"Error {e}"}
        
    # finally:
    #     await conn.close()
