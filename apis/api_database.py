#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/21 21:11
# @Author : zxiaosi
# @desc :
from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete

from database_session import database
from models import Note, NoteCreate, NoteUpdate


async def get_db():
    transaction = await database.transaction()
    try:
        yield transaction
    except:
        await transaction.rollback()
    else:
        await transaction.commit()


router = APIRouter()


@router.get("/", summary='read')
async def get_notes(db=Depends(get_db), pageIndex: int = 1, pageSize: int = 10):
    sql = select(Note).offset((pageIndex - 1) * pageSize).limit(pageSize).order_by(desc(Note.id))
    return db.fetch_all(query=sql)


@router.post("/", summary='add')
async def create_note(note_in: NoteCreate):
    sql = insert(Note).values(note_in.dict())
    await database.execute(sql)
    return {'msg': 'Success'}


@router.put("/{id}", summary='update')
async def update_note(id: int, note_in: NoteUpdate):
    sql = update(Note).where(Note.id == id).values(note_in.dict())
    await database.execute(sql)
    return {'msg': 'Success'}


@router.delete("/{id}", summary='delete')
async def delete_note(id: int):
    sql = delete(Note).where(Note.id == id)
    await database.execute(sql)
    return {'msg': 'Success'}
