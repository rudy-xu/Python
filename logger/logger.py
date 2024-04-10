# logger.py

import logging

class MyLogger:
  _instance = None

  def __new__(cls, name=None, log_file=None, level=logging.DEBUG):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._instance.logger = logging.getLogger(name)
      cls._instance.logger.setLevel(level)

      formatter = logging.Formatter('%(asctime)s - %(name)s, %(levelname)s: %(message)s')

      # print to file
      file_handler = logging.FileHandler(log_file)
      file_handler.setLevel(level)
      file_handler.setFormatter(formatter)
      cls._instance.logger.addHandler(file_handler)

      # print to terminal
      console_handler = logging.StreamHandler()
      console_handler.setLevel(level)
      console_handler.setFormatter(formatter)
      cls._instance.logger.addHandler(console_handler)

    return cls._instance

  def getLogger(self):
    return self.logger

  def info(self, msg):
    self.logger.info(msg)

  def debug(self, msg):
    self.logger.debug(msg)

  def error(self, msg):
    self.logger.error(msg)
