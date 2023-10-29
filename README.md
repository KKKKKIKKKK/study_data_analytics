<details>
<summary>Titanic from Disaster</summary>

#### DDA
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| survival | Survival | 0 = No, 1 = Yes | 범주형(명목형), 생존 여부는 숫자가 아닌 특정의미를 가지기에 범주형으로 분류되는 것으로 확인됨  |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형(순서형), 티켓 클래스는 객실 등급을 표시하며 숫자가 아닌 특정의미를 나타내기에 범주형으로 분류되는 것으로 확인됨 |
| sex | Sex | | 범주형(명목형), 성별은 "남성" OR "여성" 두가지 카테고리로 분류되며 비교나 계산이 불가능하기에 범주형으로 분류되는 것으로 확인됨|
| Age | Age in years | | 수치형(이산형), 나이는 숫자로 표현되기에 수치형으로  분류되는 것으로 확인됨 |
| sibsp | # of siblings / spouses aboard the Titanic | | 범주형(순서형), 형제자매 범주로 분류되는 것으로 확인됨|
| parch | # of parents / children aboard the Titanic | | 범주형(순서형), 부모 OR 자녀의 수를 표현하는데 값들 간 순서를 나타내는 것으로 확인됨|
| ticket | Ticket number | | 범주형(명목형), 티켓번호는 문자열을 나타내는 것으로 확인됨 |
| fare | Passenger fare | | 수치형(순서형), 승객요금은 숫자로 표현되는 것으로 확인됨 |
| cabin | Cabin number | | 범주형(순서형), 객실번호는 문자와 숫자의 조합으로 표현되는 것으로 확인됨|
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형(명목형), 승선한 항구는 범주형태로 표현되는 것으로 확인됨|

※수치형 변수는 숫자

※범주형 변수는 카테고리 OR 범주를 표시 

</details>


### 

<details>
<summary>TypeofContractChannel</summary>

#### DDA

| Field            | Data                                          | Comment                                  |
|------------------|-----------------------------------------------|------------------------------------------|
| id               | 1                                             | -    수치형(이산형) /계약고유식별자로 정수값으로 구성                                   |
| type_of_contract | 렌탈                                          | -     범주형(명목형)     /계약 유형을 나타내는 카테고리                                  |
| type_of_contract2| 일반                                          | -      범주형(명목형)    /계약서 종류를 나타내는 카테고리 값                              |
| channel          | 온라인                                       | -      범주형(명목형)  /계약 진행 방법을 나타내는 카테고리                                |
| datetime         | 2023-08-08 14:30                            | -      수치형(연속형)      /날짜와 시간으로 구성되며 연속적인 값                             |
| Term             | 12 개월                                      | -     범주형(명목형)   /계약 사용 기간을 나타내는 카테고리 값                                  |
| payment_type     | 월 렌탈료                                    | -     범주형(순서형)    /결제 유형을 나타내며 순서와 의미를 가지는 카테고리 값                               |
| product          | Sedan A                                      | -        범주형(명목형)   /렌탈한 제품의 모델명을 나타내는 카테고리 값                              |
| amount           | $500                                         | -     수치형(연속형)   /지급 금액으로 연속적인 실수 값으로 구성                                |
| state            | 활성                                         | -   범주형(명목형)    /계약 상태를 나타내는 카테고리                                  |
| overdue_count    | 2 회                                         | -        수치형(이산형)       /신청 후 취소 횟수로 이산적인 정수 값으로 구성                          |
| overdue          | 아니오                                       | -   범주형(명목형)   /연체 여부를 나타내는 카테고리 값                                  |
| credit rating    | 3.5%                                         | -      수치형(연속형)  /신용 등급에 따른 이자율을 나타내는 연속적인 값을 표현                               |
| bank             | ABC 은행                                     | -   범주형(명목형)     /결제 계좌 은행을 나타내는 카테고리 값                                |
| cancellation     | 아니오                                       | -      범주형(명목형)  /계약 취소 여부를 나타내는 카테고리 값                                |
| age              | 30                                           | -          수치형(이산형)    / 고객의 나이로 정수 값으로 표현                     |
| Mileage          | 15000                                        | -   수치형(이산형) / 차량 주행 마일리지로 정수 값으로 표현
</details> 

### 📃 Data analytics 
- 데이터 분석

#### 1️⃣ 사용 기술 



