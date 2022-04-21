#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/21 14:28
# @Author : zxiaosi
# @desc :
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# DATABASE_URI: str = "sqlite+aiosqlite:///./sql_app_async.db"  # Sqlite(异步)
# DATABASE_URI: str = "mysql+asyncmy://root:123456@localhost:3306/async_test?charset=utf8"  # MySQL(异步)
DATABASE_URI: str = "postgresql+aiopg://postgres:123456@localhost:5432/async_test"  # PostgreSQL(异步)
DATABASE_ECHO: bool = False  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)

async_engine = create_async_engine(url=DATABASE_URI, echo=DATABASE_ECHO)
async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
