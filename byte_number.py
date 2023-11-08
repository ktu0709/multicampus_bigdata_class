# 문자열에서 숫자만 걸러낸 후 합계를 구함(byte형태로 변환)
if __name__ == '__main__':
 a= '우리나라 대한민국, 2023년 11월 08일'
 b= a.encode()
 number_b = bytearray()
 #print(b)

 for element in b:
    if element >= 48 and element <= 57:
     number_b.append(element)

 print(number_b.decode())
 c= number_b.decode()

 sum = 0
 for value in c:
  sum = sum + int(value)

 print(sum)
