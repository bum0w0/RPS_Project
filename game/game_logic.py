import random
from game.user_input import get_user_choice
from utils.messages import result_message
import sys

def play_game():
    choices = ['가위', '바위', '보', '종료']

    while True:
        user_choice = get_user_choice(choices)  # 5초 동안 사용자 입력 받기

        if user_choice == "replay" or user_choice == "종료":
            # 잘못된 입력이 있을 경우
            print("게임을 종료합니다.")
            sys.exit()  # 프로그램 종료


        if user_choice is None:
            # 5초 이내에 입력을 받지 못한 경우
            result_message("시간 초과! 컴퓨터 승리 (안내면 진다!)")
            return  # 게임 종료

        computer_choice = random.choice(choices)
        print(f"컴퓨터의 선택: {computer_choice}")

        if user_choice == computer_choice:
            result_message("무승부")
        elif (user_choice == '가위' and computer_choice == '보') or \
            (user_choice == '바위' and computer_choice == '가위') or \
            (user_choice == '보' and computer_choice == '바위'):
            result_message("사용자 승리!!!!!!!\n\n")
        else:
            result_message("컴퓨터 승리!!!!!!!\n\n")