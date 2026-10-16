import unittest
from password_checker import analyze_password


class TestPasswordChecker(unittest.TestCase):

    def test_common_password_is_very_weak(self):
        result = analyze_password("password123")
        self.assertEqual(result["rating"], "Very Weak")

    def test_empty_password(self):
        result = analyze_password("")
        self.assertEqual(result["rating"], "Very Weak")
        self.assertEqual(result["length"], 0)

    def test_short_password_is_very_weak(self):
        result = analyze_password("Ab1!")
        self.assertEqual(result["rating"], "Very Weak")

    def test_predictable_sequence_is_detected(self):
        result = analyze_password("abcd1234")
        self.assertTrue(
            any("sequence" in item.lower()
                for item in result["feedback"])
        )

    def test_repeated_characters_are_detected(self):
        result = analyze_password("aaaaB1!")
        self.assertTrue(
            any("repeated" in item.lower()
                for item in result["feedback"])
        )

    def test_long_mixed_password_receives_high_rating(self):
        result = analyze_password("River!Cloud7Tiger#Moon")
        self.assertIn(result["rating"], ["Strong", "Very Strong"])

    def test_score_stays_within_valid_range(self):
        result = analyze_password("ExampleTest123!")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 8)


if __name__ == "__main__":
    unittest.main()
