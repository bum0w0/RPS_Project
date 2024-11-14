def get_user_choice(choices):
  while True:
    user_input = input("가위, 바위, 보 중 하나를 선택하세요: ").strip()
    if user_input in choices:
      return user_input
    print("잘못된 입력입니다. 다시 시도하세요.")