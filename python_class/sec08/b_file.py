'''
  인코딩 , 디코딩 : 서로다른 형식간에 데이터 변환시 사용되는 프로세스
  인코딩  : 텍스트 또는 문자열 등을 원래 형식으로 (ex:유니코드 utf-8, utf-16...)의 특정코드로 지정 하는 것
  디코딩  :  특정코드로 지정 하는 것을 원래 문자열 또는 텍스트로 되돌리는 것 (인코딩된 바이트를 다시 문자열로 변환된다. )
   *인코딩의 선택은 응용프로그램의 요구 사항과 지원되는 문자집합에 따라 다르다
       문자열  -> 인코딩 [특정코드변환]  -> 디코딩 [복원]  -> 문자열
'''
import base64 #python 표준 인코딩 모듈
if __name__ == '__main__':
    #문자열  -> 인코딩 [특정코드변환]  -> 디코딩 [복원]  -> 문자열
    text  ="hello python!!"
    encoding_text  = text.encode('utf-8')
    print( encoding_text)

    encoding_text = b"hello python!!"  #인코딩된 문자열
    decoded_text = encoding_text.decode("utf-8")
    print(decoded_text)

    o_text  ="hello python!!"
    en_text = base64.b64encode( o_text.encode('utf-8')) #바이트 문자열로 인코딩
    print(en_text)

    de_text   = base64.b64decode(en_text).decode('utf-8') #원본으로 디코딩
    print(de_text)
    '''
    base64 : 1)바이너리 데이터를 Ascii문자로 인코딩 하는데 사용된다.  
             2)이미지, 오디오,영상 파일 또는 바이너리 문서와 같은 데이터를 처리하는 용도로 사용한다.  
             3) 3바이트 이진을 4개의 Ascii로 관리하는 것  
               ->(이진데이터 -> 24비트 시퀀스 -> 4개의 6비트 청크분할 -> 6비트 10진수 Ascii )  
             4) 이메일(첨부파일 인코딩) , http통신 (Json 페이로드 = 이미지, 이진파일 ) , 암호화 등 
    '''
