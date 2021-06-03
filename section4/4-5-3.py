import pandas as pd
import numpy as np

#랜덤으로 DataFrame 생성
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns= ['ONE', 'TWO', 'THREE', 'FOUR'])
#df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
df2 = df.rename(index=lambda x : x+1)


#CSV 쓰기
df2.to_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/result.csv',index=False)
#df.to_csv('c:/section4/result.csv',index=False,header=False)
  
