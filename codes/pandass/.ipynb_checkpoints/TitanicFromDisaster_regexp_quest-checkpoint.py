import pandas as pd

# Titanic 데이터 파일 경로에 맞게 수정해야 합니다.
df_TFD = pd.read_csv('datasets/TitanicFromDisaster_train.csv')


df_TFD['Name'].unique()
# 이름 데이터

# 'Name' 열을 변수로 저장
name_column = df_TFD['Name']

# 패턴을 문자열로 만든 것 regular expression
pattern_name = r', (.+)'
pattern_marriage = r'\((.*?)\)'

# 호칭 추출을 위한 패턴
pattern_title = r'(Mrs\.|Mr\.|Miss)'

# 호칭 열 추가
df_TFD['Title'] = name_column.str.extract(pattern_title)

# 성(LastName)과 결혼 여부(Married) 정보를 추출하여 새로운 열 추가
df_TFD['LastName'] = name_column.str.extract(pattern_name)
df_TFD['Married'] = name_column.str.extract(pattern_marriage)[0].apply(lambda x: 'Mrs' if pd.notna(x) else '')

# NaN 값이 있는 행 제거
df_TFD_cleaned = df_TFD.dropna(subset=['Title', 'LastName', 'Married'])
df_TFD_cleaned['Title'] = df_TFD_cleaned['Title'].dropna()
print(df_TFD_cleaned['Title'].isnull().sum()) 

# 결과 출력 (호칭, 성, 결혼 여부 열만 선택하여 출력)
result_df = df_TFD_cleaned[['Title', 'LastName', 'Married']]

# 'Name' 열의 고유한 데이터 저장
unique_names = name_column.unique()

# 결과 출력

print(result_df)


#     Title                                    LastName Married
# 0     Mr.                             Mr. Owen Harris
# 1    Mrs.  Mrs. John Bradley (Florence Briggs Thayer)     Mrs
# 2    Miss                                 Miss. Laina
# 3    Mrs.          Mrs. Jacques Heath (Lily May Peel)     Mrs
# 4     Mr.                           Mr. William Henry
# ..    ...                                         ...     ...
# 885  Mrs.              Mrs. William (Margaret Norton)     Mrs
# 887  Miss                        Miss. Margaret Edith
# 888  Miss              Miss. Catherine Helen "Carrie"
# 889   Mr.                             Mr. Karl Howell
# 890   Mr.                                 Mr. Patrick