import unittest

from src.transform import summarize_todo


class TestSummarizeTodo(unittest.TestCase):
    def test_happy_path(self):
        sample = {"id": 7, "title": "Write tests", "completed": True}
        self.assertEqual(summarize_todo(sample), "[DONE] #7: Write tests")

    def test_missing_title_defaults(self):
        sample = {"id": 2, "completed": False}
        out = summarize_todo(sample)
        self.assertIn("[TODO] #2", out)
        self.assertIn("Untitled", out)

if __name__ == "__main__":
    unittest.main()
