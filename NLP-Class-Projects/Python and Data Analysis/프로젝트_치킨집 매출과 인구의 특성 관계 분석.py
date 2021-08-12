print('1669063 국제 이송')
'''인구수와 치킨집 매출수에는 관계가 있을까?

1. 구별 인구와 치킨집 주문의 상관관계
가정: 인구수와 치킨 주문은 비례한다.
2. 연령과 치킨집 주문의 상관관계
가정: 연령대가 어릴 수록 치킨을 많이 시켜먹는다
'''

#라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


##############시작#####################
#두 분석 중 하나를 선택하기. 입력값을 받는다
print('인구와 치킨집 주문량의 관계를 파악하는 프로젝트입니다.\n어떤 메뉴를 선택하시겠습니까?\n\n')
n = int(input('1. 구별 인구와 치킨집 주문의 상관관계\n2. 연령과 치킨집 주문의 상관관계: '))

#모델 1, 2에서 공통적으로 사용하는 코드를 함수로 묶음
def Function(x):
    #메뉴 1, 2에서 같이 사용하는 함수이다
    #치킨 데이터에서 필요한 열을 추출하는데, x값에 따라서 출력되는 데이터프레임의 열이 달라진다

    global df_gu #df_gu가 정의되지 않아서 계속 에러를 일으켰다. 이를 해결하기 위해 전역 변수 설정을 한다.
    global list1
    global categ

    # <1> 치킨 데이터 불러오기
    list_x = ['시군구', '연령대']
    df = pd.read_csv('CALL_CHICKEN_09MONTH.csv', encoding='UTF-8', thousands=',')  #PANDAS 사용: 서울시 치킨 판매업종 이용 통화량 데이터 불러오기
    x = n #사용자로부터 n값을 입력받을 때 x 받아서 함수 내 과정을 수행한다

    # <2> 치킨 데이터에서 필요한 특정 열과 치킨 주문 전화량 열 추출하기
    categ = np.unique(df[list_x[x-1]])  #NUMPY 사용: 중복된 성분을 제외한 유니크한 값만 반환
    list1 = []  # '전화량'을 저장할 리스트
    for i in categ: #list의 요소와 일치하는 전화량을 더하여 list1에 추가한다
        j = np.sum(df[list_x[x-1]] == i) #NUMPY 사용
        list1.append(j) #전화량 리스트
    df_gu = pd.DataFrame({list_x[x-1]: categ , '전화량': list1})  # PANDAS 사용: 구와 전화량으로 이루어진 데이터프레임을 만든다
    print('*치킨 데이터에서 '+list_x[x-1]+'과 전화량 열로 만든 데이터프레임')
    print(df_gu.head()) #PANDAS: 시군구/연령대와 전화량열로 만든 데이터프레임입니다
    print('\n')

#1. 구별 인구와 치킨집 주문의 상관관계를 입력하였을 때 실행한다
if n == 1:
    print('\n\n1. 구별 인구와 치킨집 주문의 상관관계를 실행하겠습니다')
    print('\n')

    print('# 1. 치킨 데이터 가공하기')
    Function(n)  # n = 1, 2번인 경우 공통적으로 사용하는 코드를 함수로 만듦.
    # <1> 치킨 데이터 불러오기
    # <2> 치킨 데이터에서 필요한 특정 열과 치킨 주문 전화량 열 추출하기

    # <3> 변형한 데이터의 열을 iloc로 나눠서 각각 리스트로 저장
    list_gu = list(df_gu.iloc[:, 0]) #PANDAS: iloc를 사용하여 df_gu의 첫 열(구별)을 리스트로 저장
    list_call = list(df_gu.iloc[:, 1]) #PANDAS: iloc를 사용하여 df_gu의 두 번째 열(전화량)을 리스트로 저장
    print('*인구 데이터에서 추출한 구별 인구수 리스트')
    print(list_gu) #구별 인구수 리스트
    print('\n')
    print('*인구 데이터에서 추출한 전화량 리스트')
    print(list_call) # 전화량 리스트
    print('\n')

    print('#2. 인구 데이터 활용하기')
    #<1> 인구 데이터 불러오기
    df = pd.read_csv('age.csv', encoding='cp949', thousands=',') #PANDAS 사용: 판다스로 age.csv파일을 불러온다.
    # 추후 계산을 쉽게 하기 위해서 숫자에서 ,를 제거하는 thousands=','를 추가하였다

    #<2> 인구 데이터에서 필요한 구별 인구수 데이터 추출하기
    df_popul = df.loc[:'서울특별시 강동구 둔촌제2동(1174070000)', ['행정구역', '2019년02월_계_총인구수']] #PANDAS: loc로 df에서 필요한 행열을 뽑아냈다
    long = [1, 19, 35, 52, 70, 86, 101, 118, 139, 153, 168, 188, 205, 220, 237, 256, 277, 293, 304,
                   323, 339, 361, 380, 403, 431] #df3에서 필요한 행(각 구별 데이터)만 뽑아오기 위해서 만든 리스트
    df_pop = df_popul.iloc[long] #PANDAS: iloc로 필요한 행을 뽑아낸다
    df_pop = df_pop.reset_index() #PANDAS: 원래는 행정구역이 인덱스였는데, 이를 자유롭게 활용하고자 인덱스를 새롭게 만들어주었다
    print('*인구 데이터에서 추출한 구별 인구수 데이터프레임')
    print(df_pop.head()) #PANDAS: 구별 인구수 데이터프레임을 프린트한다
    print('\n')

    # <3> 구별 인구수 변형한 것을 리스트로 저장
    df_pop2 = list(df_pop.iloc[:, 2]) #PANDAS 사용: iloc로 구별 총 인구수를 뽑아냈다
    list_pop2 = list(map(int, df_pop2)) #추후에 치킨 데이터의 전화횟수와 계산을 하기 위해 int값으로 바꾸고 리스트로 만들었다
    print('*인구 데이터에서 추출한 구별 총 인구수 리스트')
    print(list_pop2) #int값으로 이루어진 리스트로 만들어진 구별 인구수
    print('\n')

    print('#3. 치킨 전화량과 구별 인구수 비교 및 계산')
    clist =[]
    b = 0
    d = 0
    for i in range(25): #list_call과 list_call 리스트 안 요소가 25개이므로 25번 반복문을 반복한다
        d = float(list_call[i] / list_pop2[i])*10000 #인구수와 치킨 주문량이 비례하는지 알기 위해서 나누기를 하고 숫자가 작아서 10000을 곱한다
        d = int(d) #정수로 바꾼다
        clist.append(d)
        b += d #평균값 계산을 위해 요소들의 총합을 구한다
    print('*총 인구수에 따른 치킨 주문 비율 리스트')
    print(clist)  # 인구수에 따른 치킨 주문량을 프린트한다
    print('\n')
    b = int(b / len(list_call)) #matplotlib에서 사용할 요소들의 평균값 구하기

    print('#4. 치킨 전화량과 구별 인구수의 plot그래프 그리기')
    #MATPLOTLIB 사용
    font_name = fm.FontProperties(fname='C:\\Users\\user\\Downloads\\NanumBarunGothic.ttf', size=50).get_name()
    plt.rc('font', family=font_name)  # 한글 글씨체 설정
    plt.title('구별 인구수와 치킨 주문량의 상관관계')
    plt.style.use('ggplot') #격자무늬 배경
    plt.bar(list_gu, clist, color='gold') #x축을 구 리스트, y축을 위에서 구한 비율값으로 한다
    plt.axhline(y=b, color='brown') #$Matplotlib 사용: plt.bar에서 y=상수 함수로 표현하여 어느 구가 인구수에 비해 치킨을 많이 먹고
    #어느 구가 적게 먹는지를 알 수 있다.
    plt.show()

    print('----------------------------------------------------------------------------------------------\n',
          '결론: 치킨 주문 횟수는 인구수에 비례하지 않는다.\n\n',
          '만약 주문 횟수가 인구수에 비례한다면 바 그래프가 모두 같은 높이를 취해야 한다.\n',
          '하지만 높낮이 차이가 있는 것으로 보아 주문 횟수는 인구수에 비례하지 않는다고 할 수 있다.\n',
          '----------------------------------------------------------------------------------------------',)

#2. 연령대와 치킨집 주문의 상관관계를 알려드리겠습니다.
if n == 2:
    print('2. 연령대와 치킨집 주문의 상관관계를 알려드리겠습니다.')
    print('\n')
# 1. 치킨 데이터 불러오기
    Function(2)

    print('#2. 인구 데이터 활용하기')

    # <1> 인구 데이터 불러오기
    df_age = pd.read_csv('age.csv', encoding='cp949', thousands=',')  #PANDAS: 판다스로 age.csv파일을 불러온다.

    # <2> 인구 데이터에서 필요한 연령별 인구수 데이터만 보관한다
    df_age = df_age.iloc[0]  #PANDAS: 서울특별시의 전체 인구 데이터가 있는 행만 쓴다
    del  df_age['행정구역'],  df_age['2019년02월_계_총인구수'],  df_age['2019년02월_계_연령구간인구수'] #PANDAS사용: 판다스로 필요 없는 열을 삭제
    #print('*인구 데이터에서 추출한 0-100세까지의 인구수 리스트')
    #print(df_age.head())
    #print('\n')

    b = df_age
    number = 0
    list2 = []
    r = 0
    rr = 0
    for j in range(1,7):  # 10대부터 60대까지 6번 반복된다
        for i in range(1, 11):  # 각 연령대별로 10살씩 나눠져있으므로 10번 돈다
            rr = 9+i+r
            number += b[rr]  # numpy array에 있는 인구수를 연령대별로 더해서 number에 넣는다.
        r += 10
        list2.append(number)  # 연령대별로 더해진 총합을 미리 만들어둔 리스트에 넣는다. 10대부터 60대까지이므로 리스트 안 요소가 6개이다.
    # list2는 10대부터 60대까지 연령대별 인구수를 담은 리스트
    print('*인구 데이터에서 추출한 10대-60대까지 연령대별 인구수 리스트')
    print(list2)
    print('\n')
    list2 = list(map(int, list2)) #numpy.float64에서 int로 바꾸었다

    print('# 3. 치킨 전화량과 연령별 인구수 비교 및 계산')
    #그래프에서 사용할 연령대별 인구 대비 전화량의 수치를 구한다
    per = 0
    list3 =[]
    for i in range(6): # 각 연령대별 치킨 주문 비율
        per = (list1[i]/list2[i])*10000 # 각 연령대별 치킨 주문 비율을 전화량/연령대별 인구수로 구하고 숫자가 너무 작아서 10000을 곱하였다
        per = int(per)
        list3.append(per)  # per값을 리스트에 추가하여 추후에 그래프 그릴 때 쓴다
    list3 = np.round(list3, 2)  #NUMPY사용: numpy를 이용하여 소숫점 2자리 수까지 반올림하였다
    print('*연령대별 인구 대비 전화량의 비율을 구하고 10000을 곱한 리스트')
    print(list3)
    print('\n')


    print('# 4. 치킨 전화량과 연령별 인구수의 pie그래프 그리기')
    #MATPLOTLIB 사용
    plt.style.use('ggplot')  # 격자무늬 배경

    import matplotlib.font_manager as fm

    font_name = fm.FontProperties(fname='C:\\Users\\user\\Downloads\\NanumBarunGothic.ttf', size=50).get_name()
    plt.rc('font', family=font_name)  # 한글 글씨체 설정
    plt.rcParams['axes.unicode_minus'] = False  # 한글이 깨지지 않도록 설정
    color = ['orange', 'yellow', 'gold', 'goldenrod', 'wheat', 'lemonchiffon']  # 색상 지정
    plt.pie(list3, labels=categ, autopct='%.1f%%', colors=color, startangle=90)  # 각 연령대별 치킨 주문 비율를 파이차트로 표현하였다
    plt.axis('equal')  # 파이차트를 동그란 원으로 표현하기
    plt.title('연령대별로 보는 치킨 주문 비율')
    plt.show()  # 파이차트를 출력하기 위해 필요함
    print('----------------------------------------------------------------------------------------------\n',
        '결론: 연령대가 낮을 수록 치킨을 많이 시켜먹는다.\n\n',
        '10대-60대까지 내림차순으로 비율이 감소하는 것을 보았을 때 치킨 소비량은 나이가 어릴 수록 많다는 것을 알 수 있다.\n',
        '특히 10-20대의 비율이 과반수를 넘었다는 것을 알 수 있다.\n',
          '----------------------------------------------------------------------------------------------',
    )

elif n != 1 and n!=2: #n이 1이나 2가 아니라면 경고한다
    print('1과 2 중 하나를 선택해야 합니다.')
