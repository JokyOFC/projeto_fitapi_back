# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:10:52 2023

@author: Everton Castro
"""
from pydantic import BaseModel

class categoria(BaseModel):
    nome: str

class Product(BaseModel):
    nome: str
    preco: float
    descricao: str
    codigo: str
    is_Published: bool
    categoria_categoria_fk: int
    empresa_empresa_fk: int

class users(BaseModel):
    username: str
    email: str
    password: str
    empresa_empresa_fk: int

class empresa(BaseModel):
    cnpj: str
    razao_social: str
    nome_fantasia: str
<<<<<<< HEAD
    email: str    
=======
    email: str

class logs(BaseModel):
    data_hora: str
    users_user_fk: int
    descricao: str
>>>>>>> 9f605cecdc5066a1abf38b810a8fcaaf38c8f9e8

# class logs(BaseModel):
#     data_hora: str,
#     users_user_fk: int,
#     descricao: str



