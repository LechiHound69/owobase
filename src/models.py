import uuid
import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.database import Base


class Usuario(Base):

    __tablename__ = "usuariosuwu"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    telefono = Column(String, nullable=True)
    edad = Column(Integer, nullable=True)

    notas = relationship(
        "Nota",
        back_populates="propietario",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}', edad={self.edad})>"


class Nota(Base):
    __tablename__ = "notasowo"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    contenido = Column(String)

    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuariosuwu.id"))

    propietario = relationship("Usuario", back_populates="notas")

    def __repr__(self):
        return f"<Nota '{self.titulo}'>"
