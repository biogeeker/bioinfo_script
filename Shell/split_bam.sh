#!/bin/bash
samtools view -h $1 | \ 
  awk -v LEN=$2 '{if ($9 <= LEN && $9 >= -(LEN) && $9 != 0 || $1 ~ /^@/) print $0}' | \ 
  samtools view -bh -o out.bam -

# :set nu! - vim 不显示行号
