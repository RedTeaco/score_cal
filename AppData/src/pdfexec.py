# @Auther: EdenLeaf
# @Date: 2023/8/30 11:24
# @description:
import re

from pdfplumber import open

def is_number(s):
    try:
        float(s) # 尝试将字符串转换为浮点数
        return True
    except ValueError: # 如果转换失败，说明字符串不是数字
        pass

    try:
        import unicodedata
        unicodedata.numeric(s) # 尝试将字符串转换为数字，包括Unicode数字
        return True
    except (TypeError, ValueError): # 如果转换失败，说明字符串不是数字
        pass
    return False

class pdf:
    def __init__(self, pdf_path: str, need_terms: int):

        self.name = ""
        self.pdf = pdf_path
        self.data = self.get_data()
        self.need_terms = [str(need_terms) + "学年秋季学期", str(need_terms + 1) + "学年春季学期"]
        self.G21 = self.cal()

    def get_data(self) -> dict:
        """
        从pdf文件中获取数据
        :return: dict{'name':str,terms:list...}
        """
        pdf_file = open(self.pdf)
        table = []
        for page in pdf_file.pages:
            table += page.extract_tables()[0]
        # 创建最终返回的字典
        dicts = {}
        # 获取成绩单的名字
        pattern = re.compile('(?<=姓名: ).*(?= 学号)')
        self.name = pattern.search(table[0][0]).group()

        # 分学期放入dict
        terms = None
        for l in table:
            if '学年' in l[0]:
                terms = l[0].replace(' ', '')
                dicts[terms] = []
                continue
            if terms in dicts.keys():
                if l[1] and is_number(l[3]) and is_number(l[4]) and '体育' not in l[1]:
                    dicts[terms].append(l)
        return dicts

    def cal(self) -> float:
        dicts = self.data
        score = 0
        weight = 0
        # 计算G21
        for i in range(2):
            for l in dicts[self.need_terms[i]]:
                print(l)
                score += float(l[3]) * float(l[4])
                weight += float(l[3])
        print("".join(("课程加权综合:",str(score),"学分总和:",str(weight))))
        return score / weight


def main(pdf_paths: list, terms):
    l = []
    for pdf_files in pdf_paths:
        pdfs = pdf(pdf_files, terms)
        l.append({'name': pdfs.name, 'G21': pdfs.G21})
    return l


if __name__ == '__main__':
    pdf_path = "D:\\AccountDatas\\RedTea\Downloads\\ydxscjtzd(1).pdf"
    pdfT = pdf(pdf_path, 2024)
    print(pdfT.G21)
