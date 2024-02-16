from sqlalchemy import create_engine, inspect
from .models import User, Base

engine = create_engine("sqlite:///database/tokens.db", echo=True)  # создание движка бд
if not inspect(engine).has_table(User.__tablename__):
    Base.metadata.create_all(engine)  # создание всех таблиц