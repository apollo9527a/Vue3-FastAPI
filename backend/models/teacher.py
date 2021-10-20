#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/19 22:24
# @Author : 小四先生
# @desc : 教师表
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, ForeignKey, CheckConstraint, Date
from sqlalchemy.orm import relationship

from backend.db.base_class import Base

if TYPE_CHECKING:
    from .department import Department  # noqa


class Teacher(Base):
    """ 教师表 """
    id = Column(String(6),
                primary_key=True,
                index=True,
                doc='职工号')

    name = Column(String(10),
                  nullable=False,
                  index=True,
                  doc='教师姓名')

    sex = Column(String(2),
                 CheckConstraint("sex in ('男', '女')"),
                 nullable=False,
                 doc='教师性别')

    birthday = Column(Date,
                      default=date(2012, 1, 1),
                      nullable=False,
                      doc='教师生日')

    hashed_password = Column(String(20), nullable=False, doc='教师密码')

    education = Column(String(6),
                       CheckConstraint("education in ('学士', '硕士', '博士')"),
                       nullable=False,
                       doc='教师学历')

    title = Column(String(10),
                   CheckConstraint("title in ('助教', '讲师', '副教授', '教授')"),
                   nullable=False,
                   doc='教师职称')

    department_id = Column(String(4), ForeignKey('department.id'), doc='院系编号')

    department = relationship("Department", backref="teacher")