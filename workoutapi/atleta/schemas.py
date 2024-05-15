from typing import Annotated


from contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.70)]
    genero: Annotated[str, Field(description='Gênero do Atleta', example='F', max_length=1)]