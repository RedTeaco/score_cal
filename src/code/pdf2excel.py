import pdfplumber
from openpyxl import Workbook
import pandas as pd
from getPath import getRootPath

wb = Workbook()
ws = wb.active
def pdf2Excel(pdf_path: str):
    """
    将文本pdf文件转换为Excel
    :param pdf_path: pdf路径
    :return: 输出的文件路径
    """
    pdf = pdfplumber.open(pdf_path)
    print('开始读取数据\n')
    time = ''
    for page in pdf.pages:
        for table in page.extract_tables():
            for row in table:
                row_list = str(row).replace(" ", "").replace("[", "").replace("]", "").replace("'", "").replace("\\n",
                                                                                                                "").split(
                    ",")
                if "学年" in str(row_list[0]):
                    time = str(row_list[0])
                if row_list[-1] == '':
                    row_list[-1] = time
                ws.append(row_list)
    pdf.close()
    end_file = getRootPath() + "\\output\\" + pdf_path.split("\\")[-1][0:-4] + ".xlsx"
    wb.save(end_file)
    wb.close()
    return end_file


def process_pdf(end_file: str):
    """
    优化表格数据:删除None及体育课相关数据
    :param end_file: 需要处理的excel表格的路径
    :return: void
    """
    # 使用pandas库读取excel表
    df = pd.read_excel(end_file)
    # 删除重复行，保留第一个
    df = df.drop_duplicates(keep='first')
    # 删除成绩列中包含字符None的行

    pe_list = ['体育（1）', '体育（2）', '体育（3）', '体育（4）']

    try:
        df = df[~df['None'].isin([' None', 'None'])]
        df = df[~df['课程名称'].isin(pe_list)]
    except KeyError:
        print("\n")

    # 将改动后的数据表重新写回源文件
    try:
        pd.DataFrame(df).to_excel(end_file, sheet_name='Sheet', index=False, header=False)
        print("文件优化完成")
    except PermissionError:
        print("文件正在打开状态,请关闭文件后再试")


def executePdf(pdf_path: str) -> str:
    output_path = pdf2Excel(pdf_path)
    process_pdf(output_path)
    return output_path
