#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time : 2021/9/25 23:00
# @Author : zxiaosi
# @desc : 假数据
""" 免责声明: 数据来自网络，如有侵权，请联系删除！！！ """
from datetime import date

departmentData = [
    {'id': 1001, 'name': '计算机工程学院', 'chairman': '张强', 'phone': '13312312312'},
    {'id': 1002, 'name': '医学院', 'chairman': '马建国', 'phone': '13312312312'},
]

majorData = [
    # 计算机工程学院
    {'id': 100101, 'name': '计算机科学与技术', 'assistant': '钱伟', 'phone': '13312312312', 'department_id': '1001'},
    {'id': 100102, 'name': '物联网工程', 'assistant': '吴晓红', 'phone': '13312312312', 'department_id': '1001'},
    {'id': 100103, 'name': '软件工程技术', 'assistant': '柯刚', 'phone': '13312312312', 'department_id': '1001'},
    # 医学院
    {'id': 100201, 'name': '中药学专业', 'assistant': '赵露', 'phone': '13312312312', 'department_id': '1002'},
    {'id': 100202, 'name': '护理学专业', 'assistant': '朱壮', 'phone': '13312312312', 'department_id': '1002'},
    {'id': 100203, 'name': '针灸推拿学专业', 'assistant': '李勇', 'phone': '13312312312', 'department_id': '1002'},
]

studentData = [
    # Mysql日期可以写成下面语句  ||  date(1999, 9, 9) 为了 Sqlite
    # {'id': '1810010101', 'name': '王芳', 'sex': 'woman', 'birthday': '1999-09-09', 'hashed_password': '123456',
    # 'major_id': '100101'},

    # 计算机科学与技术
    {'id': 1810010101, 'name': '王芳', 'sex': '1', 'birthday': date(1999, 9, 9), 'major_id': '100101',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010102, 'name': '孙悟空', 'sex': '0', 'birthday': date(1999, 5, 23), 'major_id': '100101',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010103, 'name': '猪悟能', 'sex': '0', 'birthday': date(1998, 2, 12), 'major_id': '100101',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010104, 'name': '唐三葬', 'sex': '0', 'birthday': date(2000, 1, 7), 'major_id': '100101',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010105, 'name': '张悟本能', 'sex': '0', 'birthday': date(2000, 3, 29), 'major_id': '100101',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    # 物联网工程
    {'id': 1810010201, 'name': '宋清江', 'sex': '1', 'birthday': date(2000, 2, 10), 'major_id': '100102',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010202, 'name': '甄无用', 'sex': '0', 'birthday': date(1999, 6, 21), 'major_id': '100102',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010203, 'name': '关不胜', 'sex': '0', 'birthday': date(1999, 7, 19), 'major_id': '100102',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010204, 'name': '秦复明', 'sex': '1', 'birthday': date(2001, 1, 26), 'major_id': '100102',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010205, 'name': '花繁荣', 'sex': '1', 'birthday': date(2000, 5, 27), 'major_id': '100102',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    # 软件工程技术
    {'id': 1810010301, 'name': '柴进门', 'sex': '0', 'birthday': date(1999, 4, 26), 'major_id': '100103',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010302, 'name': '李天应', 'sex': '1', 'birthday': date(1999, 6, 4), 'major_id': '100103',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010303, 'name': '董不平', 'sex': '0', 'birthday': date(1999, 9, 30), 'major_id': '100103',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010304, 'name': '徐宁静', 'sex': '1', 'birthday': date(2000, 8, 20), 'major_id': '100103',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810010305, 'name': '索超越', 'sex': '0', 'birthday': date(1999, 7, 20), 'major_id': '100103',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    # 中药学专业
    {'id': 1810020101, 'name': '刘唐氏', 'sex': '1', 'birthday': date(1999, 1, 17), 'major_id': '100201',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020102, 'name': '李逵悟', 'sex': '0', 'birthday': date(1999, 5, 13), 'major_id': '100201',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020103, 'name': '阮小三', 'sex': '0', 'birthday': date(1999, 9, 16), 'major_id': '100201',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020104, 'name': '石秀气', 'sex': '1', 'birthday': date(2000, 1, 18), 'major_id': '100201',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020105, 'name': '谢宝庆', 'sex': '0', 'birthday': date(2000, 2, 25), 'major_id': '100201',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    # 护理学专业
    {'id': 1810020201, 'name': '燕青青', 'sex': '1', 'birthday': date(2000, 7, 29), 'major_id': '100202',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020202, 'name': '朱文武', 'sex': '0', 'birthday': date(1999, 2, 12), 'major_id': '100202',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020203, 'name': '鲍旭日', 'sex': '0', 'birthday': date(1999, 8, 25), 'major_id': '100202',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020204, 'name': '孔明亮', 'sex': '1', 'birthday': date(1999, 3, 12), 'major_id': '100202',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020205, 'name': '童威猛', 'sex': '0', 'birthday': date(1999, 4, 16), 'major_id': '100202',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    # 针灸推拿学专业
    {'id': 1810020301, 'name': '朱富贵', 'sex': '0', 'birthday': date(1998, 2, 15), 'major_id': '100203',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020302, 'name': '孙大嫂', 'sex': '1', 'birthday': date(1999, 3, 27), 'major_id': '100203',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020303, 'name': '王小二', 'sex': '0', 'birthday': date(1999, 6, 28), 'major_id': '100203',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020304, 'name': '白胜利', 'sex': '1', 'birthday': date(1999, 8, 10), 'major_id': '100203',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 1810020305, 'name': '段金柱', 'sex': '0', 'birthday': date(1999, 2, 12), 'major_id': '100203',
     'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
]

teacherData = [
    # 计算机工程学院
    {'id': 180101, 'name': '陈江川', 'sex': '0', 'birthday': date(1988, 9, 9), 'education': '1', 'title': '3',
     'department_id': '1001', 'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 180102, 'name': '李小平', 'sex': '0', 'birthday': date(1993, 8, 17), 'education': '2', 'title': '2',
     'department_id': '1001', 'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 180103, 'name': '赵希明', 'sex': '1', 'birthday': date(1988, 3, 28), 'education': '3', 'title': '4',
     'department_id': '1001', 'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 180104, 'name': '张红', 'sex': '1', 'birthday': date(1995, 6, 15), 'education': '1', 'title': '1',
     'department_id': '1001', 'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    # 医学院
    {'id': 180201, 'name': '吴小龚', 'sex': '1', 'birthday': date(1988, 4, 20), 'education': '2', 'title': '2',
     'department_id': '1002', 'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 180202, 'name': '张进明', 'sex': '0', 'birthday': date(1989, 10, 29), 'education': '1', 'title': '1',
     'department_id': '1002', 'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
    {'id': 180203, 'name': '李历宁', 'sex': '0', 'birthday': date(1996, 3, 19), 'education': '1', 'title': '3',
     'department_id': '1002', 'hashed_password': '$2b$12$EsrfvsiGll/jeEEo8oSt5e/QcXr5dU2dm9GUbkd/PKXF8X.Ukj2lO'},
]

courseData = [
    {'id': 1101, 'name': '计算机导论', 'credit': 2, 'period': 16},
    {'id': 1102, 'name': '计算机网络', 'credit': 2, 'period': 16},
    {'id': 1103, 'name': 'Java', 'credit': 4, 'period': 16},
    {'id': 1104, 'name': 'C语言', 'credit': 4, 'period': 16},
    {'id': 1201, 'name': '基础化学', 'credit': 2, 'period': 16},
    {'id': 1202, 'name': '生理学', 'credit': 3, 'period': 16},
    {'id': 1203, 'name': '中医药基础', 'credit': 4, 'period': 64},
    {'id': 1301, 'name': '有机化学实验', 'credit': 2, 'period': 32},
    {'id': 1302, 'name': '方剂学', 'credit': 4, 'period': 64},
    {'id': 1303, 'name': '药用化学', 'credit': 2, 'period': 32},
    {'id': 1401, 'name': '马克思主义基本原理概论', 'credit': 2, 'period': 32},
    {'id': 1402, 'name': '大学生心理健康教育', 'credit': 2, 'period': 32},
    {'id': 1403, 'name': '职业生涯与发展规划', 'credit': 1, 'period': 16},
    {'id': 1404, 'name': '形式与政策', 'credit': 1, 'period': 16},
]

selectCourseData = [
    {'student_id': 1810020301, 'teacher_id': 180101, 'course_id': 1201},
]

adminData = [
    {'name': 'admin', 'is_active': True,
     'hashed_password': '$2b$12$fSWir4aZ2fVI1jZLAjvltOmW/S0XV5s3C5VeoYlKYtkpBmDQipPJa'},
]
