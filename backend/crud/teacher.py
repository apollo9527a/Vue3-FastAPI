#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/11/15 19:53
# @Author : zxiaosi
# @desc : 操作教师表
from datetime import datetime
from typing import Union, Dict, Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from core import get_password_hash, settings
from crud.base import CRUDBase
from models import Teacher
from schemas import TeacherCreate, TeacherUpdate


class CRUDTeacher(CRUDBase[Teacher, TeacherCreate, TeacherUpdate]):
    def create(self, db: Session, *, obj_in: TeacherCreate) -> Teacher:
        """
        添加教师信息

        :param db: Session
        :param obj_in: 创建模型
        :return: 教师模型对象
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(
            id=obj_in_data['id'],
            name=obj_in_data['name'],
            sex=obj_in_data['sex'],
            birthday=datetime.strptime(obj_in_data['birthday'], "%Y-%m-%d").date(),
            education=obj_in_data['education'],
            title=obj_in_data['title'],
            address=obj_in_data['address'] if obj_in_data['address'] else '广东省广州市',
            image=obj_in_data['image'] if obj_in_data['image'] else f'{settings.BASE_URL}/{settings.STATIC_DIR}/author.jpg',
            hashed_password=get_password_hash(obj_in_data['password']),
            department_id=obj_in_data['department_id']
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, db_obj: Teacher, obj_in: Union[TeacherUpdate, Dict[str, Any]]) -> Teacher:
        """
        更新教师信息

        :param db: Session
        :param db_obj: 教师orm模型对象
        :param obj_in: 教师更新模型
        :return: 教师模型对象
        """
        if isinstance(obj_in, dict):  # 判断对象是否为字典类型
            teacher_data = obj_in
        else:
            teacher_data = obj_in.dict(exclude_unset=True)
        if 'password' in teacher_data.keys():  # 判断输入字典中是否有 password
            if teacher_data["password"]:  # 判断是否有密码输入,输入新密码则加密(密码不为空)
                hashed_password = get_password_hash(teacher_data["password"])
                del teacher_data["password"]
                teacher_data["hashed_password"] = hashed_password
        else:
            teacher_data.update({'password': ''})  # '' 为原密码
        return super().update(db, db_obj=db_obj, obj_in=teacher_data)


teacher = CRUDTeacher(Teacher)
