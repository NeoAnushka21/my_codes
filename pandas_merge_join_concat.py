import pandas
import pandas as pd

info_01 = {'Name': ['anushka1', 'anushka2', 'anushka3'],
           'color': ['black', 'blue', 'red'],
           'Number': [111, 222, 333]}

info_02 = {'Name': ['anushka4', 'anushka5', 'anushka6'],
           'color': ['brown', 'yellow', 'green'],
           'Number': [444, 555, 666]}
info_03 = {'Name': ['anushka1', 'anushka5', 'anushka6'],
           'color': ['brown', 'yellow', 'green'],
           'Number': [444, 555, 666]}
df_01 = pd.DataFrame(info_01)
df_02 = pd.DataFrame(info_02, index=[3, 4, 5])
df_03 = pd.DataFrame(info_03)

result_01 = pd.concat([df_01, df_02])
print("result1a\n", result_01)


result_01 = pd.merge(df_01, df_03, how='right')
print("result1c\n", result_01)

result_02 = pd.concat([df_01, df_02], axis=1)
print("result2\n", result_02)

result_03 = pd.concat([df_01, df_03], axis=1, join='inner')            # 'inner' -- intersection of dataframs
print("result3\n", result_03)                                          # 'outer' -- union of dataframes
