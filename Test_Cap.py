import unittest
import Cap


class TestCap(unittest.TestCase):

    def test_one_word_start_letter(self):
        text = "python"
        want = "Python"
        got = Cap.start_letter(want)
        self.assertEqual(
            want, got, f"want:{want} got:{got}The result doesn't match")

    def test_multiple_word_start_letter(self):
        text = "monty python"
        want = "Monty Python"
        got = Cap.start_letter(want)
        self.assertEqual(
            want, got, f"want:{want} got:{got}The result doesn't match")

    def test_one_word_middle_letter(self):
        text = "python"
        want = "pyThon"
        got = Cap.middle_letter(want)
        self.assertEqual(
            want, got, f"want:{want} got:{got}The result doesn't match")


if __name__ == "__main__":
    unittest.main()
