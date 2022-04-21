#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/21 14:29
# @Author : zxiaosi
# @desc :
import uvicorn
from fastapi import FastAPI

from apis import api_async, api_sync
from models import Base, Note
from session_async import async_engine
from session_sync import engine, DBSession

app = FastAPI()
app.include_router(api_async.router, prefix='/async')
# app.include_router(api_sync.router, prefix='/sync')


def sync_init():
    """ 初始化数据(同步) """
    try:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print('f"删除表失败!!! -- 错误信息如下:\n{e}"')

    with DBSession() as session:
        session.execute(Note.__table__.insert(),
                        [{'id': 1, 'name': 'one'}, {'id': 2, 'name': 'two'}, {'id': 3, 'name': 'three'}])
        session.commit()


async def async_init():
    """ 初始化数据(异步) """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(Note.__table__.insert(), [
            {'id': 1, 'name': 'one'}, {'id': 2, 'name': 'two'}, {'id': 3, 'name': 'three'}])
    await async_engine.dispose()


@app.on_event("startup")
async def startup():
    # sync_init()
    await async_init()
    pass


@app.on_event("shutdown")
async def shutdown():
    pass


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000)
