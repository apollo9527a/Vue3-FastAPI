#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/21 14:28
# @Author : zxiaosi
# @desc :
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base:
    __name__: str  # 表名
    __table_args__ = {"mysql_charset": "utf8"}  # 设置表的字符集

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Note(Base):
    """ 院系表 """
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, comment='编号')
    name = Column(String(20), nullable=False, index=True, comment='名字')


class NoteCreate(BaseModel):
    id: int
    name: str


class NoteUpdate(BaseModel):
    name: str
