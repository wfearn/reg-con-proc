import os

class File:
    def __init__(self, file_path):
        self.path = file_path

    def get_file_path(self):
        return self.path

    def get_file_name(self):
        return os.path.split(self.path)[1]
