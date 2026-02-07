import time
print("카트라이더를 다운로드하시겠습니까?")
카라플_다운_1 = input("(yes/no)")
if 카라플_다운_1 == "yes":
    print("카트라이더 다운로드를 진행합니다")
    for i in range(10,-1,-1):
        print(f"남은시간 : {i}초 입니다")
        time.sleep(1)
        i -= 1
    print("카트라이더 rush+ 를 다운 완료했습니다")
    print("카트라이더를 실행하시겠습니까")
    카라플_실행_1 = input("(yes/no)")
    if 카라플_실행_1 == 'yes':
        print("카트라이더에 접속합니다")
        print("실행중")
        for i123 in range(50):
            time.sleep(0.5)
            print('\r' + " " * i123 + '🛬' , end="", flush = True)
        print("카트라이더가 실행되었습니다")
    elif 카라플_실행_1 == "no":
        print("카트라이더 다운로더를 종료합니다")
elif 카라플_다운_1 == "no":
    print("카트라이더 다운로더를 종료합니다")
    print("감사합니다")