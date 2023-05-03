import pandas as pd
from similaritymeasures import Similarity

# ! input:  各個結果/MODEL的 ALL TF_IDF table.pickle
# ! output: 各個前處裡差別結果的 Euclidean Distance 距離矩陣 Pickle & Excel

# region 檔案讀取 tf_idf | problem_list

# TF-IDF TABLE
model_list = [
    "討論區TAG",
    "討論區TAG_題目主題篩選",
    "討論區TAG_單詞拆解前處裡",
    "討論區TAG_前處理後保留片語結構",
    "題目基本資料_Related Topics",
]
matrix_type = "Euclidean Distance"

file_location = f"G:/我的雲端硬碟/課業相關 研究所/Leetcode資料區/程式中途結果輸出/{model_list[3]}"
tf_idf = pd.read_pickle(f"{file_location}/ALL TF_IDF table.pickle")
# endregion

measures = Similarity()
euclidean_df = measures.euclidean_distance(tf_idf)

# 存檔
euclidean_df.to_excel(f"{file_location}/{matrix_type}.xlsx")
euclidean_df.to_pickle(f"{file_location}/{matrix_type}.pickle")
