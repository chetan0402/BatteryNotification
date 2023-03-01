import time
from os import remove


class Logger:
    def __init__(self):
        self.log_file = None
        self.filename = f"batteryNotifi-{int(time.time())}.log"

    def createFile(self):
        self.log_file = open(self.filename, "a+")

    def closeFile(self):
        if self.log_file is None:
            raise "createFile() not runned first."
        else:
            self.log_file.close()

    def writeFile(self, towrite):
        if self.log_file is None:
            raise "createFile() not runned first."
        else:
            self.log_file.write(f"{towrite}\n")
            self.log_file.flush()

    def info(self, infomsg):
        if self.log_file is None:
            raise "createFile() not runned first."
        else:
            self.writeFile(f"{time.asctime()} - INFO - {infomsg}")

    def deleteFile(self):
        try:
            self.log_file.close()
            remove(self.filename)
        finally:
            pass
