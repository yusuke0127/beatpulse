import os
import csv

class Base:
    @classmethod
    def empty_file(cls, file_path):
        return os.stat(file_path).st_size == 0

    @classmethod
    def file_exists(cls, file_path):
        return os.path.isfile(file_path)
