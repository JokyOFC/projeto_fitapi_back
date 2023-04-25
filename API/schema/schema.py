from pydantic import BaseModel

class Aparelho(BaseModel):
    Base_Empresa_idEmprea: int
    Bases_idBases:int
    data_de_compra: str
    idAparelhos: int
    nome: str
    tipo: str

class Cargos(BaseModel):
    area_de_atuacao: str
    funcionarios_idfuncionarios: int
    idCargos: int
    media_salarial: float
    nome: str

class agendamento(BaseModel):
    alunos_idalunos: int
    data_agendamento: str
    idagendamento: int
    instrutores_idinstrutores: int

class alunos(BaseModel):
    cpf: str
    dadosalunos_iddadosalunos: int
    data_de_nascimento: str
    dieta_iddieta: int
    idalunos: int
    nome: str
    sexo: str
    tipo_corpo_idtipo_corpo: int

class bases(BaseModel):
    tipo_corpo_idtipo_corpo: int
    endereco: str
    idbases: int
    nome: str
    turmas_idturmas: int

class contatos(BaseModel):
    email: str
    email_alternativo: str
    empresa_idempresa: int
    endereco: str
    idcontatos: int
    nome: str
    telefone: str
    telefone_alternativo: str

class dados_contato(BaseModel):
    email: str
    endereco: str
    iddadosalunos: int
    telefone: str
    telefone_alternativo: str

class dadoscontatofuncionario(BaseModel):
    email: str
    email_alternativo: str
    endereco: str
    iddadosfuncionarios: int
    telefone: str
    telefone_alternativo: str

class dadoscontatoinstrutores(BaseModel):
    email: str
    email_alternativo: str
    endereco: str
    iddadosfuncionarios: int
    telefone: str
    telefone_alternativo: str

class dieta(BaseModel):
    descricao: str
    iddieta: int
    media_calorias: float
    rotina: str
    tipo: str

class empresa(BaseModel):
    cnpj: str
    data_de_abertura: str
    email: str
    endereco: str
    idempresa: int
    nome_fantasia: str
    razaosocial: str

class exercicios(BaseModel):
    descricao: str
    idexercicios: int
    media_calorias: float
    media_peso: float
    media_peso: float
    media_peso: float

class funcionarios(BaseModel):
    bases_empresa_idempresa: int
    bases_idbases: int
    cpf: str
    dadosfuncionarios_iddadosfuncionarios: int
    data_de_nascimento: str
    idfuncionarios: int
    nome: str

class instrutores(BaseModel):
    bases_empresa_idempresa: int
    bases_idbases: int
    cpf: str
    dadoscontatoinstrutores_iddadosfuncionarios: int
    idinstrutores: int
    nome: str
    turmas_idturmas: int

class tabela_alimentar(BaseModel):
    alimento: str
    caloria: float
    dieta_iddieta: int
    gordura: float
    idtabela_alimentar: int


class tipo_corpo(BaseModel):
    alimento: str
    caloria: float
    dieta_iddieta: int
    gordura: float
    idtabela_alimentar: int


class treinos(BaseModel):
    alunos_idalunos: int
    data_treino: str
    idtreinos: int
    tipo_treino: str

class turmas(BaseModel):
    data_aulas: str
    idturmas: int
    materia_turma: str



