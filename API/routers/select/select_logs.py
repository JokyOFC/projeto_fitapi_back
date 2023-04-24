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
from schema.schema import logs

router = APIRouter()

@timeout(10)
@router.get("/select/logs/{logs_id}")
async def read_logs(logs_id: int):
    conn = None
    try:
        conn = await get_database_connection()
        query = "SELECT * FROM logs WHERE logs_id = $1"
        result = await conn.fetchrow(query, logs_id)
        if result is None:
            raise HTTPException(status_code=404, detail="logs not found")
        return logs(**result)

    except PostgresError as e:
        return {"message": f"Error {e}"}

    except TimeoutError as e:
        return {"message": f"Error {e}"}

    finally:
        await conn.close()
