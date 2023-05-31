'''
2023-05-31
백서현
#문제정의
    튜플안에 있는 숫자들의 종류와  반복 갯수 분석하기
#문제분석
    변수-빈리스트(num_list)
#알고리즘
   1.튜플정의
   2.빈 리스트 생성
   3.중복된 숫자 리스트에 넣기

'''
num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
num_list=[] #빈 리스트

print("생성된 튜플:",num)

for i in range(len(num)): #튜플 길이 만큼 반복
    if num[i] not in num_list:#리스트에 없는 경우
        num_list.append(num[i])#리스트에 추가
        print(num[i],"개수:",num.count(num[i]))#개수 출력
