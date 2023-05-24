'''
2023-05-24
백서현
#문제정의
    난수를 발생시켜 num.txt 파일을 만들고, 이파일을 이용해서 각 학생의 평균을 구한다음 avg.txt파일에 저장하기
'''

import random #난무 모듈추가
with open("c:/data/num.txt","w") as f: #파일 객체
    for i in range(5): #줄반복
         for j in range(5): #랜덤 수 찍기 반복
              f.write(str(random.randint(1,100)))#랜덤 수 파일에 쓰기
              f.write('') #숫자 다음 공백
    f.write('\n')#줄 바꿈

with open("c:/data/num.txt",'r') as f1: #읽기 파일 객체
    with open("c/data/num.txt","w") as f2: #쓰기 파일 객체
        j=0 
        while True: #무한반복
            j=j+1
            score=f1.readline() #num,txt 한 줄 읽어 오기
            if score=='': #내용이 없으면
                break
            scorelist=score.split() #읽어 온 한 줄을 공백 기준 리스트로

            sum=0 #합계
            for i in range(5): #한 학생당 5과목의 점수 더하기
                sum=sum+int(scorelist[i]) #리스트의 항목 더하기
            print("번 학생의 평균:",sum/5,file=f2)#결과파일에 작성

