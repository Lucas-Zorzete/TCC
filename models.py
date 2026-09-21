from database import Base
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Date, ForeignKey
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    phone = Column(Integer)
    email = Column(String(100))
    password = Column(Text)
    photo = Column(String(255))
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    charge = Column(String(50))
    genre = Column(String(50))

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    icon = Column(String(50))
    description = Column(String(100))
    order = Column(Integer)

class Checkup(Base):
    __tablename__ = "checkups"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(50))
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    date = Column(Date)
    media_bpm = Column(Float)
    observation = Column(Text)

class Medicao_bpm(Base):
    __tablename__ = "medicoes_bpm"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    sistolica = Column(Integer)
    diastolica = Column(Integer)
    date_time = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
