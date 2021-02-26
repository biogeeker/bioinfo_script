#!/usr/bin/env python

"""根据fasta序列长度过滤内容，保留长度以下序列并返回结果"""

import sys
import argparse


def dict_seq(input_fa):
    """字典化fasta序列"""
    output = {}
    with open(input_fa, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(">"):
                seq_name = line.strip()
                seq = ""
            else:
                seq += line.rstrip()
                output[seq_name] = seq
        return output


def cal_len_fa(seq_len, output):
    """根据fasta序列长度进行过滤，保留长度以下序列"""
    filter_result = {}
    for key, value in output.items():
        if len(value) <= int(seq_len):           
            filter_result[key] = value
        else: pass
    return filter_result


def dict_convert_fa(filter_result, out_fa):
    """将过滤的字典转变为fasta文件"""
    for key, value in filter_result.items():
        with open(out_fa, "a") as f:
            f.write(key + "\n" + value + "\n")
    return f


def get_opt():
    """创建解析器对象，命令行参数格式化"""
    parser = argparse.ArgumentParser(description="Function: FASTA File Length Filter")
    parser.add_argument("-i", "--input", type=str, required=True,
                        help="FASTA input file before filtering")
    parser.add_argument("-l", "--length", type=int, required=True,
                        help="Filter sequences below length")
    parser.add_argument("-o", "--output", type=str, default="out_fa.fasta",
                        help="FASTA output file after filtering")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_opt()
    # i 报错AttributeError: 'Namespace' object has no attribute 'i'
    # 使用长参数名
    output = dict_seq(args.input)
    filter_result = cal_len_fa(args.length, output)
    dict_convert_fa(filter_result, args.output)
