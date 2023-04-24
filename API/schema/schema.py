# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:10:52 2023

@author: Everton Castro
"""
from pydantic import BaseModel

class categoria(BaseModel):
    nome: str

class Product(BaseModel):
    preco: float
    nome: str
    descricao: str
    codigo: str
    is_published: bool
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
    email: str

class logs(BaseModel):
    data_hora: str
    users_user_fk: int
    descricao: str