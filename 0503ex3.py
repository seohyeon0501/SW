'''
2023-05-03
백서현
#문제정의
1~입력받은 숫자까지의 합계 구하기
#문제분석
   1.변수선언 num에 정수 입력
   total=0
   2.논리(반복)
       (조건) for i in range(1,num+1):
#알고리즘`

'''

#for반복문
num=int(input("합계 구할 숫자:"))
total=0 #합계

for i in range(1,num+1): #조건
    total=total+i #합계

print('1~{}까지의 합계는 {}'.format(num,total))
