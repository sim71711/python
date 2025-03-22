a = int(input("입력 진수 결정(16/10/8/2): ")) #진수 입력받기
b = input("값 입력: ") #문자열 입력받기

c = int(b, a) #입력된 값을 10진수로 변환

#변환값 출력
print("16진수 ==> ", hex(c))
print("10진수 ==> ", c)
print("8진수 ==> ", oct(c))
print("2진수 ==> ", bin(c))
