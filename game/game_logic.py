import random
from game.user_input import get_user_choice
from utils.messages import result_message

def play_game():
  choices = ['가위', '바위', '보']
  user_choice = get_user_choice(choices)
  computer_choice = random.choice(choices)

  print(f"컴퓨터의 선택: {computer_choice}")

  if user_choice == computer_choice:
    result_message("무승부")
  elif (user_choice == '가위' and computer_choice == '보') or \
     (user_choice == '바위' and computer_choice == '가위') or \
     (user_choice == '보' and computer_choice == '바위'):
    result_message("사용자 승리!!!!!!!")
  else:
    result_message("컴퓨터 승리!!!!!!!")