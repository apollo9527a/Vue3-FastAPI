#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2022/4/21 14:26
# @Author : zxiaosi
# @desc :
from fastapi import APIRouter, Depends
from sqlalchemy import desc, select, update, insert, delete
from sqlalchemy.orm import Session

from models import Note, NoteUpdate, NoteCreate
from session_sync import DBSession


def get_db() -> Session:
    with DBSession() as session:
        yield session


router = APIRouter()


@router.get("/", summary='read')
def get_notes(db: Session = Depends(get_db), pageIndex: int = 1, pageSize: int = 10):
    sql = select(Note).offset((pageIndex - 1) * pageSize).limit(pageSize).order_by(desc(Note.id))
    result = db.execute(sql)
    return result.scalars().all()


@router.post("/", summary='add')
def create_note(db: Session = Depends(get_db), *, note_in: NoteCreate):
    sql = insert(Note).values(note_in.dict())
    db.execute(sql)
    db.commit()
    return {'msg': 'Success'}


@router.put("/{id}", summary='update')
def update_note(db: Session = Depends(get_db), *, id: int, note_in: NoteUpdate):
    sql = update(Note).where(Note.id == id).values(note_in.dict())
    result = db.execute(sql)
    db.commit()
    return {'data': result.rowcount, 'msg': 'Success'}


@router.delete("/{id}", summary='delete')
def delete_note(db: Session = Depends(get_db), *, id: int):
    sql = delete(Note).where(Note.id == id)
    result = db.execute(sql)
    db.commit()
    return {'data': result.rowcount, 'msg': 'Success'}
