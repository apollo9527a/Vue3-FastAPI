#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/17 11:05
# @Author : zxiaosi
# @desc : 操作学生表
from datetime import datetime
from typing import Union, Dict, Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core import get_password_hash, settings
from crud.base import CRUDBase
from models import Student
from schemas import StudentCreate, StudentUpdate


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def create(self, db: Session, *, obj_in: StudentCreate) -> Student:
        """
        添加学生信息

        :param db: Session
        :param obj_in: 学生添加模型
        :return: 学生orm模型对象
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            id=obj_in_data['id'],
            name=obj_in_data['name'],
            sex=obj_in_data['sex'],
            birthday=datetime.strptime(obj_in_data['birthday'], "%Y-%m-%d").date(),
            address=obj_in_data['address'] if obj_in_data['address'] else '广东省广州市',
            image=obj_in_data['image'] if obj_in_data['image'] else f'{settings.BASE_URL}/{settings.STATIC_DIR}/author.jpg',
            hashed_password=get_password_hash(obj_in_data['password']),
            major_id=obj_in_data['major_id']
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: Student, obj_in: Union[StudentUpdate, Dict[str, Any]]) -> Student:
        """
        更新学生信息

        :param db: Session
        :param db_obj: 学生orm模型对象
        :param obj_in: 学生更新模型
        :return: 学生orm模型对象
        """
        if isinstance(obj_in, dict):  # 判断对象是否为字典类型
            student_data = obj_in
        else:
            student_data = obj_in.dict(exclude_unset=True)
        if 'password' in student_data.keys():  # 判断输入字典中是否有 password
            if student_data["password"]:  # 判断是否有密码输入,输入新密码则加密(密码不为空)
                hashed_password = get_password_hash(student_data["password"])
                del student_data["password"]
                student_data["hashed_password"] = hashed_password
        else:
            student_data.update({'password': ''})  # '' 为原密码
        return super().update(db, db_obj=db_obj, obj_in=student_data)


student = CRUDStudent(Student)
