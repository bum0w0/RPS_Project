# RPS_Project
오픈소스SW의 이해 깃헙 프로젝트 (8조)
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/bum0w0">
        <img src="https://avatars.githubusercontent.com/bum0w0" width="100px;" alt="bum0w0"/>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/chanyoung1256">
        <img src="https://avatars.githubusercontent.com/chanyoung1256" width="100px;" alt="chanyoung1256"/>
      </a>
    </td>
	  <td align="center">
      <a href="https://github.com/krdevdory">
        <img src="https://avatars.githubusercontent.com/krdevdory" width="100px;" alt="krdevdory"/>
      </a>
    </td>
      <td align="center">
      <a href="https://github.com/pgw2001">
        <img src="https://avatars.githubusercontent.com/pgw2001" width="100px;" alt="pgw2001"/>
      </a>
    </td>
  </tr>
  <t>
    <td align="center">
      <b>김진범</b>
    </td>
	 <td align="center">
      <b>김찬영</b>
    </td>
    <td align="center">
      <b>안봉근</b>
    </td>
       <td align="center">
      <b>박건웅</b>
    </td>
  </tr>
</table>

# 가위 바위 보 !
### 재미있는 가위바위보를 해봅시다~

이 프로젝트는 간단하지만 재미있는 **가위바위보 게임**을 구현한 Python 기반의 프로그램으로, <br>
사용자는 컴퓨터와 대결하며, 결과에 따라 승리, 패배, 무승부를 확인할 수 있습니다. 😄  

## 주요 기능 ✨
- **가위바위보 대결**  
  사용자와 컴퓨터 간 가위바위보 대결을 진행하며, 결과를 즉시 출력합니다.

- **게임 로직 분리**  
  게임 로직과 사용자 입력 처리를 별도의 파일로 나누어 코드 유지보수를 쉽게 했습니다.

- **타임아웃 기능 추가**  
  주어진 시간 안에 내지 않으면 패배하는 가위바위보 게임 규칙을 추가 했습니다.

- **잘못된 입력 처리**  
  유저가 가위, 바위, 보 중 하나를 입력하는지 추적하고 잘못된 입력을 처리합니다.

- **무한 반복 기능 추가**  
  가위바위보 게임을 이어서 플레이 할 수 있는 기능을 추가 했습니다.

## 파일 구조 📁
```
rock_paper_scissors/
├── main.py                    # 메인 실행 파일 (게임 실행)
├── game/
│   ├── game_logic.py          # 가위바위보 게임 로직 관련 코드
│   └── user_input.py          # 사용자 입력 처리 코드
├── utils/
│   └── messages.py            # 메시지 출력 및 유틸리티 함수 모음
├── tests/
│   ├── test_game_logic.py     # 게임 로직에 대한 테스트 코드
│   └── test_user_input.py     # 사용자 입력 처리에 대한 테스트 코드
│
├── README.md
├── requirements.txt           # 프로젝트에 필요한 패키지 목록 
```

## 실행 방법 🚀
이 프로젝트는 **Python 3.10 이상**에서 동작합니다.  
Python이 설치되어 있지 않다면 [Python 공식 웹사이트](https://www.python.org/downloads/)에서 다운로드하고 설치해주세요.

별도 설치 없이 CLI(명령줄 인터페이스)에서 바로 실행되며, 간단한 입력만으로 게임을 즐길 수 있습니다.
1. 터미널에서 아래 명령어를 입력하여 프로젝트를 클론하고 루트 폴더로 이동합니다.
```
git clone https://github.com/bum0w0/RPS_Project.git
cd RPS_Project
```
2. CLI(명령줄 인터페이스)에서 아래 명령어를 입력하여 가위바위보 게임을 실행합니다.
```
python main.py
```
3. 게임이 실행되면 아래와 같은 메시지가 출력됩니다. 상대를 이겨보세요!
```
안 내면 진다! 가위, 바위, 보! : 
```