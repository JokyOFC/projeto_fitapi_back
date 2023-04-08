# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:17:24 2023

@author: Everton
"""
import asyncpg


async def get_database_connection():
    conn = await asyncpg.connect(user='everton',
                                 password='admin',
                                 database='banco_legal',
                                 host='localhost')
    return conn
