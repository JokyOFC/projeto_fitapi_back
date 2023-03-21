# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:26:24 2023

@author: Everton
"""
from routers.create_product import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
