class LoggerRateLimiter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logger_dict = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.logger_dict and self.logger_dict[message] + 10 > timestamp:
            return False
        self.logger_dict[message] = timestamp
        return True

    # Your Logger object will be instantiated and called as such:
    # obj = Logger()
    # param_1 = obj.shouldPrintMessage(timestamp,message)
