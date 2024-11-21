import time
import sys
from threading import Thread

def get_user_choice(choices):
    user_input = None
    replay = "replay"  # 잘못된 입력 시 반환할 값

    def get_input():
        nonlocal user_input
        user_input = input("안 내면 진다! 가위, 바위, 보! : ").strip()

    # 입력 받는 스레드 시작
    thread = Thread(target=get_input)
    thread.daemon = True  # 메인 스레드가 종료될 때 함께 종료
    thread.start()

    start_time = time.time()
    while time.time() - start_time < 5:  # 5초 동안 입력을 기다림
        if user_input:  # 유효한 입력이 있으면
            if user_input in choices:
                return user_input
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")
                return replay  # 잘못된 입력시 replay 반환
        time.sleep(0.1)  # 너무 자주 CPU를 사용하지 않도록 잠시 대기

    return None  # 5초 동안 입력이 없으면 None 반환