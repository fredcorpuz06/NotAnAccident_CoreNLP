def hello():
    print "hello world"

hello()

d = {'abc':'abc','def':{'ghi':'ghi','jkl':'jkl'}}
for ele in d.values():
    if isinstance(ele,dict):
       for k, v in ele.items():
           print(k,' ',v)


import pandas as pd
help(pd.DataFrame)