import pandas as pd
import numpy as np


def excelCal(excel_path: str, *terms: str):
    data = pd.read_excel(excel_path, usecols=['学分', '成绩', '备注'])
    data = pd.concat([data[data['备注'] == terms[0]], data[data['备注'] == terms[1]]])
    score = data.values[:, 1]
    weight = data.values[:, 0]
    score_plus = np.multiply(score, weight).sum()
    weight_plus = weight.sum()
    result = score_plus / weight_plus
    return result