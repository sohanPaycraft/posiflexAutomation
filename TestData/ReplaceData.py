import pandas
import json

class Replace_Data:


    def conv_dict(self,re):
        print(re)
        df = pandas.read_excel('/home/sohansagar/Documents/automate/replace.xlsx',
                                       sheet_name =re)
        df_json = df.to_json()
        df_d = json.loads(df_json)
        data_take =[]

        print(len(df_d))
        b=[]
        c=[]
        d=[]
        e=[]
        col_len=0
        t=0
        for x,y in df_d.items():
            col_len=len(y)
            b.append(x)

            for m,n in y.items():
                print(t)
                print(m,n)
                if t<col_len:
                    c.append(n)
                    t=t+1
                elif t< col_len*2:
                    d.append(n)
                    t = t + 1
                else:
                    e.append(n)
                    t = t + 1

        print(b,c,d,e)

        for n in range(0,col_len):
            a = {}
            a["Qty"]="1"
            a[b[0]] = c[n]
            a[b[1]] = d[n]
            a[b[2]]= e[n]
            a["flow"]=re
            a["Amt"]=""
            data_take.append(a)

        print(data_take)
        return data_take






