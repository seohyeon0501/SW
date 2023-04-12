'''
2023-04-12
백서현
두 정수 입력 후
모두 짝수이면 "모두 짝수" 출력
모두 홀수이면 "모두 홀수" 출력
아니면 "홀수,짝수 섞여 있음"출력
#문제분석
     변수 - 정수1(num1),정수2(num2)
     수식 - num1%2==0 (num1은 짝수)/ num1%2!=0 (num1은 홀수)
#알고리즘 
     1.변수선언
          -num1,num2에 정수 입력
     2.논리(선택 if~elif~else)
          if num1%2==0 and num2%2==0:
            (조건1 참)"모두 짝수"
          elif num1%2==1 and num2%2==0:
             (조건2 참)"첫 번쨰 숫자가 짝수"
          elif num1%2==0 and num2%2==1:
             (조건2 참)"두 번쨰 숫자가 짝수"
          else 
              "두 숫자 모두를 짝수로 입력하세요."


'''



num1=int(input("첫 번쨰 정수 입력"))
num2=int(input("두 번쨰 정수 입력"))

if num1%2==0 and num2%2==0:
   print(num1,"+",num2,"=",num1+num2)

elif num1%2==1 and num2%2==0:
   print("첫번쨰 정수를 짝수로 입력하세요")
elif num1%2==0 and num2%2==1:
   print("두번쨰 정수를 짝수로 입력하세요")
else:
   print("두 숫자 모두를 짝수로 입력하세요.")