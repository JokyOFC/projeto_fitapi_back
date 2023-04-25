# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:26:24 2023

@author: Everton
"""
from routers.insert import create_product
from routers.delete import delete_product 
from routers.select import select_produto
from fastapi import FastAPI

app = FastAPI(title='API Shopping')
routers = [
        select_produto.router,
        delete_product.router,
        create_product.router,
    ]
    
for router in routers:
    app.include_router(router)
                
