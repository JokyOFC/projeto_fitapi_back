# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:26:24 2023

@author: Everton
"""
from Integracao.insert import create_product

if __name__ == "__main__":
    uvicorn.run(create_product.app, host="0.0.0.0", port=8000)