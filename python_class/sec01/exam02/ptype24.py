#\x04 : 16진수 04이고 십진수 4이다
#\x00 : 16진수 00이고 십진수 0이다

print((1024).to_bytes( 2, byteorder ='big'))
print((1024).to_bytes( 2, byteorder = 'little'))

print((-1024).to_bytes( 4, byteorder = 'big', signed = True ))
print(int.from_bytes( b'\x04\x00', byteorder = 'big') )# byte열에서 정수형 변환
print(int.from_bytes( b'\x00\x04', byteorder = 'little' ))
print(int.from_bytes( b'\xff\xff\xfc\x00', byteorder = 'big' ))
print(int.from_bytes( b'\xff\xff\xfc\x00', byteorder = 'big' , signed = True ))
print(int.from_bytes( [ 4, 0 ], byteorder = 'big' ))

print(int.from_bytes( [ 4, 0 ], byteorder = 'big' ))