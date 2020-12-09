from unittest import TestCase

from LoggerRateLimiter import LoggerRateLimiter


class TestLoggerRateLimiter(TestCase):
    def test_should_print_message(self):
        self.solution = LoggerRateLimiter()
        self.assertTrue(self.solution.shouldPrintMessage(1, "foo"))
        self.assertTrue(self.solution.shouldPrintMessage(2, "bar"))
        self.assertFalse(self.solution.shouldPrintMessage(3, "foo"))
        self.assertFalse(self.solution.shouldPrintMessage(8, "bar"))
        self.assertFalse(self.solution.shouldPrintMessage(10, "foo"))
        self.assertTrue(self.solution.shouldPrintMessage(11, "foo"))
