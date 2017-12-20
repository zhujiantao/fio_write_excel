#!/usr/bin/env python
#coding: utf-8

from const import *
from write_excel import *
from read_fio import *

workbook = getWorkbook()
row = 1

for io_mode_key in io_mode.keys():
    io_mode_value = io_mode.get(io_mode_key)
    writeHeaderToExcel(workbook, io_mode_value)

for file_name in fiofile_tuple:
    for grep_content in grep_content_tuple:
        bw_iops_lat_dict = get_bw_iops_lat_dict(file_name, grep_content, 1, 3)
        io_mode_key = grep_content[0 : 15]
        writeToExcel(workbook, io_mode.get(io_mode_key), row, 2, bw_iops_lat_dict)
    row = row + 1

for io_mode_key in io_mode.keys():
    setSum(workbook=workbook, io_mode_value=io_mode.get(io_mode_key))

closeWorkbook(workbook)


