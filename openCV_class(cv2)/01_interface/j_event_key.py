import cv2

#chr() , ord()
img = cv2.imread('../img/bg.jpg')
title = 'IMG'                   # 창 이름 
x, y = 100, 100                 # 최초 좌표
#True, False
while True:
    cv2.imshow(title, img)
    key = (cv2.waitKey(0) & 0xFF == 27 ) # 키보드 입력을 무한 대기, 8비트 마스크처리  (==주면 esc 키가 체크가 안됨)
    #8비트 마스크처리 0xFF  -> 32비트 64비트 차이를 유지하기 위한 방법,반환값이 있으면 하위 8비트값까지만 유지하고 나머지는 무시
    print(key, chr(key))        # 키보드 입력 값,  문자 값 출력
    if key == ord('h'):         # 'h' 키 이면 좌로 이동
        x -= 10
    elif key == ord('j'):       # 'j' 키 이면 아래로 이동
        y += 10
    elif key == ord('k'):       # 'k' 키 이면 위로 이동
        y -= 10
    elif key == ord('l'):       # 'l' 키 이면 오른쪽으로 이동
        x += 10
    elif key == ord('q') or key == 27: # 'q' 이거나 'esc' 이면 종료
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y )   # 새로운 좌표로 창 이동
        