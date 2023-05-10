'''
2023-05-10
백서현
#문제정의
    입력받은 숫자의 합이 1000이상이면 합계와 평균 출력
#문제분석
    변수-합계(sum),입력횟수(snt),평균(avg),정수,(num)
#알고리즘
    1.변수 초기화 
      num 키보드로 입력
      sum=0,cnt=0,avg=0
    2.논리(반복안에 선택 포함)
       (반복) while True: #무한반복
             num 키보드로 입력
             cnt 1증가
             sum에 더하기
             (선택) if sum>=1000:
                       break
'''
sum=0
cnt=0
avg=0

while True:#무한반복
    num=int(input("숫자입력:"))#정수입력
    cnt+=1 #cnt 1증가
    sum+=num #합계
    if sum>=1000: #선택 조건
        break #반복 종료

avg=sum/cnt #평균 계산

print("1000을 넘는 수:%d"%sum,end="")
print("평균:%.2f"%avg)