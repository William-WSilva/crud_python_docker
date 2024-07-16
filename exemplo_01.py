from sqlalchemy import create_engine

# Conectar ao Sqqlite em memoria
engine = create_engine("sqlite:///meubanco.db", echo=True)

print("Conexão com Sqlite estabelecida.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

Base.metadata.create_all(engine)