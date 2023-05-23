'''
2023-05-23
백서현
#문제정의
    키보드로 입력받은 내용을 리스트에 저장하고 파일(out,txt)에 출력하기
#문제분석
    변수-입력값 저장할 리스트(enter),키보드 입력 내용 저장(txt)
#알고리즘
    1.변수 초기화
        enter=[]
    2.파일 객체 생성(쓰기)
    3.파일 처리
         3.1 (반복) while True:
                      text=.문장 입력
                      (선택) if text=='':
                                 break
                       text를 enter(리스트변수)추가
        3.2 파일에 결과 출력
    4.파일 닫기
'''

enter=[] #리스트 변수 생성

f=open("c:/data/out.txt","w") #파일 객체 쓰기

while True: #무한반복
    text=input("문장입력(끝:엔터키):") #문자열 입력
    if text=='': #입력내용이 없으면
        break #반복 종료
    enter.append(text) #입력 내용 리스트에 추가

f.writelines(enter) #리스트자료형을 파일에 출력

print("입력될 리스트",enter)
print("out.txt파일이 생성되었습니다.")