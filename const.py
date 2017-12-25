#!/usr/bin/env python
#coding: utf-8

read_header = {"bw" : "bw", "iops" : "iops", "min" : "min", "max" : "max", "avg" : "avg"}

read_header_len = len(read_header)

io_mode = {"rand-100r0w-4kb" : "4k随机读", "rand-0r100w-4kb" : "4k随机写", "rand-100r0w-8kb" : "8k随机读"}

fiofile_tuple = ("fio.txt1.bak", "fio.txt2.bak", "fio.txt3.bak",
                 "fio.txt4.bak", "fio.txt5.bak", "fio.txt6.bak",
                 "fio.txt7.bak")

grep_content_tuple = (
    "rand-100r0w-4kb: (groupid=0, jobs=1)",
    "rand-0r100w-4kb: (groupid=0, jobs=1)",
    "rand-100r0w-8kb: (groupid=0, jobs=1)",
)

fiofile_count = len(fiofile_tuple)

funciton = "AVERAGE"

bw_iops_line_num = 1
clat_line_num = 3
