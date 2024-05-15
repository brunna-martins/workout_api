from typing import Annotated


from contrib.schemas import BaseSchema
from pydantic import Field, PositiveFloat

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT KING', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='Rua X Quadra 2', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do Centro de Treinamento', example='Marcos', max_length=30)]