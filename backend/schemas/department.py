#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/22 9:59
# @Author : zxiaosi
# @desc : 院系表模型
from typing import Optional
from pydantic import BaseModel, Field

from schemas import GMT


class DepartmentIn(BaseModel):
    """ 共享模型字段 """
    name: str = Field(min_length=1, max_length=20, example='名字')
    chairman: str = Field(min_length=1, max_length=10, example='主任名')
    phone: Optional[str] = Field(regex=r'(^\s{0}$)|^(0\d{2,3}-\d{7,8})|(1[34578]\d{9})$', example='主任手机号')


class DepartmentCreate(DepartmentIn):
    """ 添加数据时的字段验证 """
    id: str = Field(regex=r'^10[0-9]{2}$', min_length=4, max_length=4, example='编号')


class DepartmentUpdate(DepartmentIn):
    """ 更新数据的字段验证 """
    pass


class DepartmentOut(DepartmentCreate, GMT):
    """ 查询数据的字段验证 """

    class Config:
        orm_mode = True  # 是否使用orm模型(个人理解: 放行,不验证)
