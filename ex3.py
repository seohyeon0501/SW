'''
2023-05-10
백서현
#문제정의
'''

num=int(input("사용자 입력:"))
sum=0 #합계
cnt=0 #3의 배수의 갯수
i=0

while True:
    i=i+3
    sum=sum+i
    cnt=cnt+1
    if sum>num:
        break

print("{}를 넘었을 떄 숫자:{}".format(num,i))
print("{}를 넘었을 떄 까지의 합계:{}".format(num,sum))
print("{}를 넘었을 떄 까지 몇 번쨰 3의 배수인가:{}".format(num,cnt))

