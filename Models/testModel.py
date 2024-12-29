from sqlalchemy import  Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from typing import List
from pydantic import BaseModel, ConfigDict
from DatabaseConfiguration.databaseConfig import Base


class Post(Base):

    __tablename__ = 'posts'
    id : Mapped[int] = mapped_column(Integer, primary_key=True,index=True,autoincrement=True)
    title : Mapped[str] = mapped_column(String,nullable=False)




class PostCreate(BaseModel):
    title : str
    description : str
    model_config = ConfigDict(from_attributes=True)