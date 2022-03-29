import pandas
import json

df=pandas.read_excel('/home/sohansagar/Documents/automate/128_2022-03-2415-23-25.946218.xlsx',sheet_name='Sheet')
df_json=df.to_json()
df_d=json.loads(df_json)
print(df_d)
print(df_d["Qantity"]["0"])
