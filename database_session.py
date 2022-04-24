#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/21 21:12
# @Author : zxiaosi
# @desc :
from databases import Database

# DATABASE_URI: str = "sqlite+aiosqlite:///./sql_app_async.db"  # Sqlite(异步)
# DATABASE_URI: str = "mysql+asyncmy://root:123456@localhost:3306/async_test?charset=utf8"  # MySQL(异步)
DATABASE_URI: str = "postgresql+asyncpg://postgres:123456@localhost:5432/async_test"  # PostgreSQL(异步)

database = Database(DATABASE_URI)
