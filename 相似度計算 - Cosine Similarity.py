import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import math
import pickle

# ! input:  各個結果/MODEL的 ALL TF_IDF table.pickle | 20210712-problemset_lst 問題清單 index
# ! output: 各個前處裡差別結果的 cosine相似矩陣 Pickle & Excel

# region 檔案讀取

# TF-IDF TABLE
model_list = [
    "討論區TAG",
    "討論區TAG_題目主題篩選",
    "討論區TAG_單詞拆解前處裡",
    "討論區TAG_前處理後保留片語結構",
    "題目基本資料_Related Topics",
]
matrix_type = "Cosine Similarity"

file_location = f"G:/我的雲端硬碟/課業相關 研究所/Leetcode資料區/程式中途結果輸出/{model_list[0]}"
tf_idf = pd.read_pickle(f"{file_location}/ALL TF_IDF table.pickle")

# 測試用EXCEL
# tf_idf = pd.read_excel(
#     f"G:/我的雲端硬碟/課業相關 研究所/Leetcode資料區/程式中途結果輸出/程式測試用Excel.xlsx",
#     sheet_name="Test",
#     index_col=0,
# )
print(tf_idf)

np_matrix = tf_idf.to_numpy()
# np_matrix = tf_idf.drop(["Hyper Link"], axis=1).to_numpy()
print(np_matrix)


# 問題清單 index
source_file = "C:/Users/yungy/OneDrive - 逢甲大學/文件/project leetcode/20210712"
with open(f"{source_file}/problemset_lst.pickle", "rb") as f:
    problem_sets = pickle.load(f)
problem_list = []
for question in problem_sets:
    problem_list.append(question["titleSlug"])

# endregion

# region Cosine similarity 距離矩陣產出
cosine_sim = cosine_similarity(tf_idf)
cosine_sim = pd.DataFrame(cosine_sim, index=problem_list, columns=problem_list)
print(cosine_sim)


# cosine_sim.to_excel(f"{file_location}/{matrix_type}.xlsx")
# cosine_sim.to_pickle(f"{file_location}/{matrix_type}.pickle")
# ? Special Case
cosine_sim.to_excel(f"{file_location}/{matrix_type} 10 times.xlsx")
cosine_sim.to_pickle(f"{file_location}/{matrix_type} 10 times.pickle")
# endregion
