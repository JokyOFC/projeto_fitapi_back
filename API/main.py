# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:26:24 2023

@author: Everton
"""
from routers.insert import create_product
from routers.insert import create_categoria 
from routers.insert import create_empresa 
from routers.delete import delete_product 
from routers.select import select_produto, select_empresa, select_categoria, select_logs, select_users
from fastapi import FastAPI

app = FastAPI(title='API Shopping')
routers = [
        select_produto.router,
        select_empresa.router,
        select_categoria.router,
        select_logs.router,
        select_users.router,
        delete_product.router,
        create_product.router,
        create_categoria.router,
        create_empresa.router
    ]
    
for router in routers:
    app.include_router(router)
                
