import unittest
from main import coin_toss

class TestCoinToss(unittest.TestCase):
    def test_output(self):
        for _ in range(100):
            result = coin_toss()
            self.assertIn(result, ["Heads", "Tails"])

if __name__ == "__main__":
    unittest.main()
