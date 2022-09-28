from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate() # GuessNumbers 클래스의 generate 함수를 실행
        print(g.update_date)
        print(g.lottos)

        # 실제 Test case (OK or FAILED)
        # default로 6개 숫자 x 5set = 30개의 숫자가 생성됨을 확인
        self.assertTrue(len(g.lottos) > 20)

# TDD (Test-Driven Development) # 테스트케이스를 먼저 써놓고
# 테스트케이스를 충족시키는 방향으로 코드를 짠다
