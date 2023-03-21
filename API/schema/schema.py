# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:10:52 2023

@author: Everton Castro
"""
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    code: str
    empresa: str
    description: str
    dimensions: str
    value: float
