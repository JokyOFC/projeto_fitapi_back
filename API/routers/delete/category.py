# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:00:40 2023

@author: Everton
"""
from fastapi import APIRouter, HTTPException
from timeout_decorator import timeout, TimeoutError     
from asyncpg.exceptions import PostgresError
from connection.conexao import get_database_connection   


router = APIRouter()
        
@timeout(10)        
@router.delete("/delete/category/{category_id}")
async def delete_category(category_id: int):
    conn = None
    try:
        conn = await get_database_connection()
        query = "DELETE FROM category WHERE category_id = $1"
        result = await conn.execute(query, category_id)
        if result == "DELETE 0":
            raise HTTPException(status_code=404, detail="category not found")
        return {"message": "category deleted"}
    
    except PostgresError as e:
        return {"message": f"Error {e}"}
        
    except TimeoutError as e:
        return {"message": f"Error {e}"}
        
    finally:
        await conn.close()