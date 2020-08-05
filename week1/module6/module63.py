import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, new_value):
        lst = super(LoggableList, self).append(new_value)
        self.log(new_value)
        return lst
