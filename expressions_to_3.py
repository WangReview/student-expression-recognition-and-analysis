# -*- coding:utf-8 -*-


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import ast
import os


# face_detect, norm_scores, expressions_3_result, column_expressions_3_sums
def read_from_excel(sheet_name='Sheet1.xlsx'):
    try:
        data = pd.read_excel(sheet_name)
        print(f"succeed {sheet_name} reading data")

        face_detect = data['face_detect'].tolist()
        norm_scores = data['norm_scores'].tolist()
        expressions_3 = data['expressions_3'].tolist()
        # ['[3, 26, 0]', '[13, 27, 3]', '[9, 26, 4]']  [[3, 26, 0], [13, 27, 3], [9, 26, 4]]
        expressions_3_result = [ast.literal_eval(item) for item in expressions_3]
        column_expressions_3_sums = [sum(col) for col in zip(*expressions_3_result)]


        return face_detect, norm_scores, expressions_3_result, column_expressions_3_sums
    except Exception as e:
        print(f"Error: {e}")
        return None


face_detect, norm_scores, expressions_3_result, column_expressions_3_sums = \
    read_from_excel(sheet_name='data/B206-5-14_2.xlsx')

columns_3_expressions = [list(col) for col in zip(*expressions_3_result)]
# positive_expression = np.array(columns_3_expressions[0])
# detect_num = len(positive_expression)
positive_expression = columns_3_expressions[0]
neutral_expression = columns_3_expressions[1]
negative_expression = columns_3_expressions[2]



def write_to_excel(positive_expression, neutral_expression, negative_expression, sheet_name='Sheet1'):
    data = {
        'positive_expression': positive_expression,
        'neutral_expression': neutral_expression,
        'negative_expression': negative_expression
    }

    df = pd.DataFrame(data)

    df.to_excel(excel_writer=sheet_name, index=False)

    print(f"succeed write {sheet_name}")


current_path = os.getcwd()  
write_to_excel(positive_expression, neutral_expression, negative_expression, sheet_name='expressions_3B206-5-14-480_2.xlsx')
# write_to_excel(face_num, monment_avg_scores, expressions_3_monment, sheet_name='B206-5-14-480_2.xlsx')










