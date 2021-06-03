import pandas as pd
import csv

#기본 읽기
# df = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s1.csv')
# print(df)

#행 스킵
# df = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s1.csv', skiprows=[0])
# print(df)
#
#행 스킵, 헤더 생략
# df = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s1.csv', skiprows=[0],header=None)
# print(df)

# #헤더 정의
# df = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s1.csv', skiprows=[0],header=None, names=["Month",2020,2021,2022])
# print(df)
#
#인덱스 컬럼 정의
# df = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s1.csv', skiprows=[0],header=None, names=["Month",1958,1959,1960], index_col=[0])
# print(df)
#
#특정 값 치환
# df = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s1.csv', skiprows=[0],header=None, names=["Month",1958,1959,1960], na_values=["JAN"])
# print(pd.isnull(df))
# print(df)
#
# #실습 정리 및 인덱스 재 정의
# df = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s1.csv', skiprows=[0],header=None, names=["Month",1958,1959,1960])
# print(df)
# # print(list(df.index))
#
# print(df.rename(index=lambda x : x+1))
# print(df.rename(index=lambda x : x+1).index)

# print(df.index.values)
# print(df.index.values.tolist())
#
# #읽기

# df2 = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s2.csv',sep=';', skiprows=[0], header=None, names=["First name", "Test1", "Test2", "Test3", "F'inal", "Grade"])
df2 = pd.read_csv('/Users/devpomme/Desktop/development/web-crawling/python_create_app_1/section4/csv_s2.csv', sep=';', skiprows=[0], header=None, names=['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])

# print(df2)
#
#Columns 값 수정
df2['Grade'] = df2['Grade'].str.replace('"', ' ')

# #평균 컬럼 추가
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1) # 가로 방향 (세로방향은 axis=0)
#
#합계 컬럼 추가
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)

print(df2)
