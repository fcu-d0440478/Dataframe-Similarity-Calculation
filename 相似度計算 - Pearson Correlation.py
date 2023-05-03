import pandas as pd

# from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle

# ! input:  各個結果/MODEL的 ALL TF_IDF table.pickle
# ! output: 各個前處裡差別結果的 Pearson相關係數矩陣 Pickle & Excel

# region 檔案讀取 tf_idf | problem_list

# TF-IDF TABLE
model_list = [
    "討論區TAG",
    "討論區TAG_題目主題篩選",
    "討論區TAG_單詞拆解前處裡",
    "討論區TAG_前處理後保留片語結構",
    "題目基本資料_Related Topics",
]
matrix_type = "Pearson Correlation"

# file_location = (
#     f"G:/我的雲端硬碟/課業相關 研究所/Leetcode資料區/程式中途結果輸出/{model_list[1]}"
# )
# tf_idf = pd.read_pickle(f"{file_location}/ALL TF_IDF table.pickle")

# 測試用EXCEL
tf_idf = pd.read_excel(
    f"G:/我的雲端硬碟/課業相關 研究所/Leetcode資料區/程式中途結果輸出/程式測試用Excel.xlsx",
    sheet_name="Test",
    index_col=0,
)
print(tf_idf)

np_matrix = tf_idf.to_numpy()
# np_matrix = tf_idf.drop(["Hyper Link"], axis=1).to_numpy()
print(np_matrix)

# endregion

# region Pearson Correlation 矩陣產出

np.seterr(invalid="ignore")  # 錯誤抑制，0的跳過
# rowvar=True就是計算row和row間的關聯(題目和題目)，反之就算是column和column間的(TAG與TAG)
pearson_correlation_matrix = np.corrcoef(np_matrix, rowvar=True)

# 從Numpy轉回DataFrame
pearson_correlation_matrix = pd.DataFrame(
    pearson_correlation_matrix, index=tf_idf.index, columns=tf_idf.index
)
print(pearson_correlation_matrix)

# pearson_correlation_matrix.to_excel(f"{file_location}/{matrix_type}.xlsx")
# pearson_correlation_matrix.to_pickle(f"{file_location}/{matrix_type}.pickle")
# endregion


# region 模組測試地帶
# x_simple = np.array([4, 3, 4, 4, 0])
# y_simple = np.array([3, 3, 2, 5, 4])
# my_rho = np.corrcoef(x_simple, y_simple)

# print(my_rho)
# endregion
