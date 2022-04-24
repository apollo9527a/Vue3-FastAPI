#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/21 14:27
# @Author : zxiaosi
# @desc :
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URI: str = "sqlite:///./sql_app_sync.db"  # Sqlite(异步)
# DATABASE_URI: str = "mysql://root:123456@localhost:3306/sync_test?charset=utf8"  # MySQL(异步)
# DATABASE_URI: str = "postgresql://postgres:123456@localhost:5432/sync_test"  # PostgreSQL(异步)
DATABASE_ECHO: bool = False  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)


def is_open_thread():
    """ 是否关闭sqlite单线程 """
    if DATABASE_URI.startswith('sqlite'):
        return {"check_same_thread": False}
    else:
        return ''


engine = create_engine(url=DATABASE_URI, echo=DATABASE_ECHO, connect_args=is_open_thread())
DBSession = sessionmaker(bind=engine)


