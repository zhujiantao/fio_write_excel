#!/usr/bin/env python
#coding: utf-8

import os

def transform_bw(bw_value):
    if "KB/s" in bw_value:
        return float(bw_value[0:-4])
    else :
        return float(bw_value[0:-3])/1000

def transform_lat(lat_value):
    if lat_value.endswith("K"):
        return float(lat_value[0:-1])
    else:
        return float(lat_value)/1000

#参数1 filename
#参数2 shell filer content
#返回：带宽 iops 时延 dict
def get_bw_iops_lat_dict(filename, filter_content, bw_iops_line_num, clat_line_num,):
    # cmd = "cat fio.txt | grep -A3 'rand-100r0w-4kb: (groupid=0, jobs=1)'"
    cmd = "cat " + filename + " | grep -A3 '" + filter_content + "'"
    result_file = os.popen(cmd)
    all_lines = result_file.readlines()
    bw_iops = all_lines[bw_iops_line_num]
    bw_iops_lat_dict = {}
    for b_tmp in bw_iops.split(":")[1].split(","):
        title_value = b_tmp.split("=")
        title = str(title_value[0]).strip()
        value = str(title_value[1]).strip()
        if title=="bw":
            bw_iops_lat_dict[title] = transform_bw(value)
        if title=="iops":
            bw_iops_lat_dict[title] = int(value)

    clat = all_lines[clat_line_num]
    for c_tmp in clat.split(":")[1].split(","):
        title_value = c_tmp.split("=")
        title = str(title_value[0]).strip()
        value = str(title_value[1]).strip()
        if title=="min" or title=="max" or title=="avg":
            bw_iops_lat_dict[title] = transform_lat(value)
    return bw_iops_lat_dict

# print get_bw_iops_lat_dict("fio.txt", "rand-100r0w-4kb: (groupid=0, jobs=1)", 1, 3)