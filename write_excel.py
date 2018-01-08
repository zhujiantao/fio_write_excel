#!/usr/bin/env python
#coding: utf-8

import xlsxwriter

import sys
reload(sys)
#设置utf-8编码
sys.setdefaultencoding('utf8')
from const import *

storage_name = "超融合"

def getWorkbook():
        workbook = xlsxwriter.Workbook(xlsx_file_name) # 建立文件
        return workbook


def closeWorkbook(workbook):
    workbook.close()

#用来写入一些固定内容
def writeHeaderToExcel(workbook, io_mode_value):
    worksheet = workbook.add_worksheet(io_mode_value)
    worksheet.merge_range('A1:A{0}'.format(fiofile_count+3), storage_name) #A1到A9合并后写入sandstone
    worksheet.merge_range("B2:B{0}".format(fiofile_count+1), io_mode_value)      #B2到B7写入4k随机读
    #C1到G1分别对应写read_header
    row = 0
    column = 2
    for title in read_header.keys() :
        worksheet.write(row, column, read_header.get(title))
        row = row
        column = column + 1

#用来写入从fio文件获取的值
def writeToExcel(workbook, io_mode_value, begin_row, begin_column, bw_iops_lat_dict):
    row = begin_row
    column = begin_column
    worksheet = workbook.get_worksheet_by_name(io_mode_value)
    for title in bw_iops_lat_dict.keys() :
        worksheet.write(row, column, bw_iops_lat_dict[title])
        row = row
        column = column + 1

def setSum(workbook=None, io_mode_value=None):
    row = fiofile_count + 1
    worksheet = workbook.get_worksheet_by_name(io_mode_value)

    for col_num in range(2, read_header_len+2):
        worksheet.write(row, col_num, '={0}({1}{2}:{3}{4})'.format(funciton, chr(ord('A') + col_num), 2, chr(ord('A') + col_num), row))

#worksheet.write('A1', 'Hello world')
