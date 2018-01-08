#!/usr/bin/env python
#coding: utf-8
from collections import OrderedDict

read_header = OrderedDict([("bw" , "bw"), ("iops" , "iops"), ("min" , "min"), ("max" , "max"), ("avg" , "avg")])

read_header_len = len(read_header)

io_mode = OrderedDict([("rand-100r0w-4kb" , "4k随机读"),
                       ("rand-0r100w-4kb" , "4k随机写"),
                       ("rand-100r0w-8kb" , "8k随机读"),
                       ("rand-0r100w-8kb" , "8k随机写"),
                       ("rand-75r25w-8kb" , "8k混合读"),
                       ("rand-100r0w-64kb" , "64k随机读"),
                       ("rand-0r100w-64kb" , "64k随机写"),
                       ("r-75r25w-64kb" , "64k混合读"),
                       ("rand-100r0w-512kb" , "512k随机读"),
                       ("rand-0r100w-512kb" , "512k随机写"),
                       ("rand-100r0w-1Mb" , "1M随机读"),
                       ("rand-0r100w-1Mb" , "1M随机写")
                      ])

##8k 64k读写页名称
# io_mode = OrderedDict([("rand-75r25w-8kb" , "8k混合写"),
#                        ("r-75r25w-64kb" , "64k混合写")
#                         ])

fiofile_tuple = ("fio.txt.bak.226", "fio.txt.bak.227", "fio.txt.bak.228",
                 "fio.txt.bak.229", "fio.txt.bak.232", "fio.txt.bak.233",)

grep_content_tuple = (
    "'rand-100r0w-4kb: (groupid=0, jobs=1)'",
    "'rand-0r100w-4kb: (groupid=0, jobs=1)'",
    "'rand-100r0w-8kb: (groupid=0, jobs=1)'",
    "'rand-0r100w-8kb: (groupid=0, jobs=1)'",
    "'rand-75r25w-8kb: (groupid=0, jobs=1)'",
    "'rand-100r0w-64kb: (groupid=0, jobs=1)'",
    "'rand-0r100w-64kb: (groupid=0, jobs=1)'",
    "'r-75r25w-64kb: (groupid=0, jobs=1)'",
    "'rand-100r0w-512kb: (groupid=0, jobs=1)'",
    "'rand-0r100w-512kb: (groupid=0, jobs=1)'",
    "'rand-100r0w-1Mb: (groupid=0, jobs=1)'",
    "'rand-0r100w-1Mb: (groupid=0, jobs=1)'",
)

##8k 64k混合读写过滤内容
# grep_content_tuple = (
#     "'rand-75r25w-8kb: (groupid=0, jobs=1)' | grep -A6 -B1 write",
#     "'r-75r25w-64kb: (groupid=0, jobs=1)' | grep -A6 -B1 write",
# )

fiofile_count = len(fiofile_tuple)

funciton = "SUM"

bw_iops_line_num = 1
clat_line_num = 3

xlsx_file_name = "fio测试结果1.xlsx"
