# -*- coding: UTF-8 -*-

import modify_count
import modify_rows
import FileUtil
import ResultUtil

def do():
    # data = []

    # sort_li = modify_count.getResult()
    # for item in sort_li:
    #     data.append(ResultUtil.change_count_tuple(item))

    # sort_li = modify_rows.getResult()
    # for item in sort_li:
    #     data.append(ResultUtil.change_rows_tuple(item))

    # FileUtil.append("data2.txt", '\n'.join(data))

    #生成文件修改次数记录表
    fileds = ['文件路径','修改次数']
    FileUtil.import_count_excel(fileds,modify_count.getResult())

    # 生成文件修改行数记录表
    # fileds = ['文件路径','总增加行数','总删除行数','总修改行数']
    # FileUtil.import_rows_excel(fileds, modify_rows.getResult())