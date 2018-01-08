#!/usr/bin/env python
#coding: utf-8

from const import *
from write_excel import *
from read_fio import *

workbook = getWorkbook()
row = 1

for io_mode_key in io_mode.keys():
    io_mode_value = io_mode[io_mode_key]
    writeHeaderToExcel(workbook, io_mode_value)

for file_name in fiofile_tuple:
    for grep_content in grep_content_tuple:
        bw_iops_lat_ordereddict = get_bw_iops_lat_dict(file_name, grep_content, bw_iops_line_num, clat_line_num)
        io_mode_key = grep_content.split(":")[0][1:]
        writeToExcel(workbook, io_mode.get(io_mode_key), row, 2, bw_iops_lat_ordereddict)
    row = row + 1

for io_mode_key in io_mode.keys():
    setSum(workbook=workbook, io_mode_value=io_mode.get(io_mode_key))

closeWorkbook(workbook)


