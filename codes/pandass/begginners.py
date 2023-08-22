import pandas as pd
double_list = [
             [1000, '과자','2019-12-31','반품'],
             [2000, '음료', '2020-03-02', '정상'],
             [3000, '아이스크림', '2020-02-03','정상'],
             [1000,'과자','2019-12-31','반품']
            ]
pd.DataFrame(data=double_list)
double_columns = ['가격','종류','판매일자','반품여부']
df_saledays = pd.DataFrame(data=double_list, columns=double_columns)
print(df_saledays)

#apply() 단일변수 처리 
#def는 형태만 - cell_value- 750의 값이 들어감.= 1000원 결과값 출력 
def mean_subtraction(cell_value) :
    result = 1750 - cell_value  # 가격 평균 - 개별값
    return result 

mean_subtraction(750)


df_saledays['가격'].apply(mean_subtraction)# 각 cell 당 평균 차이 

# 3.다변수 처리 with apply()
def calculate_sum(row):
    result = row['가격'] * 20
    return result

df_saledays ['가격합']= df_saledays.apply(calculate_sum, axis='columns')
print(df_saledays)

# regexpress(정규식)
data = {'Names': ['김지수', '박지민', '이태용', '최수영']}

df_Name = pd.DataFrame(data)

print(df_Name)

# 패턴을 문자열로 만든 것 regualr expression
pattern = r'^[가~힣]' 

df_Name['Names'].str.extract(pattern)


