import os


# 获取项目根目录
def getRootPath() -> str:
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = cur_path[:cur_path.find('Score') + len('Score')]  # Score:项目名称
    return root_path