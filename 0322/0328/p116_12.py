'''
2023-03-28
백서현
윗변이 23,아랫변이 34,높이가 13인 사다리꼴의 넓이 구하기
 변수:윗변,아랫변,높이,사다리꼴의 넓이
 수식:사다리꼴의 넓이=((윗변+아랫변)*높이)/2
 알고리즘:변수선언,사다리꼴의 넓이 구하기,결과 출력
'''
upperside=23 #윗변
lowerside=34 #아랫변
height=13 #높이
trapezoid=0 #사다리꼴의 넓이

trapezoid=((upperside+lowerside)*height)/2 #사다리꼴의 넓이
print("윗변",upperside,"아랫변:",lowerside,"높이",height,"사다리꼴의 넓이",trapezoid)