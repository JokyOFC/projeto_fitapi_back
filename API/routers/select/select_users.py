# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:00:40 2023

@author: Everton
"""
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '...')))

from connection.conexao import get_database_connection
from asyncpg.exceptions import PostgresError
from timeout_decorator import timeout, TimeoutError
from fastapi import APIRouter, HTTPException
from schema.schema import users

router = APIRouter()

@timeout(10)
@router.get("/select/users/{users_id}")
async def read_users(users_id: int):
    conn = None
    try:
        conn = await get_database_connection()
        query = "SELECT * FROM users WHERE user_id = $1"
        result = await conn.fetchrow(query, users_id)
        if result is None:
            raise HTTPException(status_code=404, detail="users not found")
        return users(**result)

    except PostgresError as e:
        return {"message": f"Error {e}"}

    except TimeoutError as e:
        return {"message": f"Error {e}"}

    finally:
        await conn.close()
