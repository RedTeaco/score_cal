import os

import calculate
from pdf2excel import *


def main():
    if not os.path.exists(getRootPath()+"\\output"):
        os.mkdir(getRootPath()+"\\output")
    filename: list = input("请输入放置在项目根目录下的pdf文件名\n如果需要输入多个，中间以空格隔开:").split(' ')
    start = input("请输入需要计算的学年(以秋季学期为准,纯数字即可):")
    for pdf in filename:
        if os.path.isabs(pdf):
            execute(pdf, start)
        else:
            execute(getRootPath() + "\\" + pdf, start)


def execute(pdf_path, start):
    print("开始处理文件:")
    excel_path = executePdf(pdf_path)
    print("文件输出已完成 (1/2)\n\n开始计算学分")
    terms = [start[0:4] + "学年秋季学期", str(int(start[0:4]) + 1) + "学年春季学期"]
    score = calculate.excelCal(excel_path, terms[0], terms[1])
    print("".join(
        ["计算完成(2/2)\n", "文件", pdf_path.split('\\')[-1],'中 ', terms[0], " 至 ", terms[1], "的课程加权平均分为:\n",
         str(score), '\n\n']))


if __name__ == '__main__':
    main()
