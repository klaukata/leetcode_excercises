# 2877. Create a DataFrame from List - https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # student_id = []
    # age = []
    # for x in student_data:
    #     student_id.append(x[0])
    #     age.append(x[1])
    # d = {'student_id': student_id, 'age': age}
    # return pd.DataFrame(data=d)
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

#2878 - https://leetcode.com/problems/get-the-size-of-a-dataframe/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [len(players), len(players.columns)]