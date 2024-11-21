import unittest
from unittest.mock import patch
from game.user_input import get_user_choice

class TestUserInput(unittest.TestCase):
  @patch('builtins.input', side_effect=['가위'])
  def test_get_user_choice_valid(self, mock_input):
    self.assertEqual(get_user_choice(['가위', '바위', '보']), '가위')

if __name__ == '__main__':
  unittest.main()