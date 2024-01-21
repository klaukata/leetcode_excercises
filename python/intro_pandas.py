# 2877. Create a DataFrame from List - https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     # student_id = []
#     # age = []
#     # for x in student_data:
#     #     student_id.append(x[0])
#     #     age.append(x[1])
#     # d = {'student_id': student_id, 'age': age}
#     # return pd.DataFrame(data=d)
#     return pd.DataFrame(student_data, columns=['student_id', 'age'])

#2878 - https://leetcode.com/problems/get-the-size-of-a-dataframe/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# def getDataframeSize(players: pd.DataFrame) -> List[int]:
#     # return [len(players), len(players.columns)]
#     return list(players.shape)

#2879 = https://leetcode.com/problems/display-the-first-three-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.head(3)

#2880 - https://leetcode.com/problems/select-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# def selectData(students: pd.DataFrame) -> pd.DataFrame:
#     return students.query('calories == 420').loc[:, ['duration', 'age']]


#2881 - https://leetcode.com/problems/create-a-new-column/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     return employees.assign(bonus=employees.duration.map(lambda p: p * 2))

# 2882 - https://leetcode.com/problems/drop-duplicate-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
# def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
#     return customers.drop_duplicates(subset='age')

# 2883 - https://leetcode.com/problems/drop-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset='age')


data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "age": [20, None, 20]
}
df = pd.DataFrame(data)
print(dropMissingData(df))
