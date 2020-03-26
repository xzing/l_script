#!/bin/bash
for (( i = 1; i < 12; i++ ))
do
  echo "开始$1"
  you-get https://www.bilibili.com/video/av27122140?p=$i -o /Users/zing/Downloads/Docker/ &
  wait
done
echo "结束"

