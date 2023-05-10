'''
2023-05-10
백서현
#문제정의
     입력받은 숫자만큼 줄 반복 하면서 별찍기
#문제분석
     변수-숫자(num)
#알고리즘
    1.변수 초기화
        num변수에 정수 입력
    2.논리(중첩 반복)
       (반복) for i in range(1,num+1):#줄반복
              (반복) for j in range(1,i+1): #별찍기 반복
                  별찍기
'''

num=int(input("숫자입력:"))
for i in range(1,num+1): #줄 반복
    for j in range(1,i+1):#별 찍기 반복
        print("+",end="")
        print() #줄 바꿈

#거꾸로 출력
print("\n거꾸로 출력")

num2=int(input("숫자입력:"))
for i in range(1,num2+1):
    for j in range(i,num2+1):
       print("*",end="")
       print() #줄바꿈

      