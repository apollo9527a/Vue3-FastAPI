#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/21 14:27
# @Author : zxiaosi
# @desc :
from fastapi import APIRouter, Depends
from sqlalchemy import select, desc, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import Note, NoteCreate, NoteUpdate
from session_async import async_session


async def get_async_db() -> AsyncSession:
    async with async_session() as session:
        yield session


router = APIRouter()


@router.get("/", summary='read')
async def get_notes(db: AsyncSession = Depends(get_async_db), pageIndex: int = 1, pageSize: int = 10):
    sql = select(Note).offset((pageIndex - 1) * pageSize).limit(pageSize).order_by(desc(Note.id))
    result = await db.execute(sql)
    await db.close()
    return result.scalars().all()


@router.post("/", summary='add')
async def create_note(db: AsyncSession = Depends(get_async_db), *, note_in: NoteCreate):
    sql = insert(Note).values(note_in.dict())
    await db.execute(sql)
    await db.commit()
    await db.close()
    return {'msg': 'Success'}


@router.put("/{id}", summary='update')
async def update_note(db: AsyncSession = Depends(get_async_db), *, id: int, note_in: NoteUpdate):
    sql = update(Note).where(Note.id == id).values(note_in.dict())
    result = await db.execute(sql)
    await db.commit()
    await db.close()
    return {'data': result.rowcount, 'msg': 'Success'}


@router.delete("/{id}", summary='delete')
async def delete_note(db: AsyncSession = Depends(get_async_db), *, id: int):
    sql = delete(Note).where(Note.id == id)
    result = await db.execute(sql)
    await db.commit()
    await db.close()
    return {'data': result.rowcount, 'msg': 'Success'}
