import os, glob

class FileManager:

    BASE_EXTENSION = "*.{}"
    NEW_FILE_BASE = "/{}_{}.%s"

    def __init__(self, file_path, extension, output_path):
        self.directory = file_path
        self.file_extension = extension
        self.output_directory = output_path
        self.new_file_name = output_path + NEW_FILE_BASE % extension

    def set_file_extension(self, extension):
        self.file_extension = extension

    def set_directory(self, directory_path):
        self.directory = directory_path

    def set_output_directory(self, output_path):
        self.output_directory = output_path
        self.new_file_name = output_path + NEW_FILE_BASE % extension

    def file_gen(self):
        os.chdir(self.directory)
        for file in glob.glob(BASE_EXTENSION.format(self.file_extension)):
            yield file

    def save_files(self, file_dictionary):
        counter = 0

        for key in file_dictionary:

            next_file_name = self.new_file_name.format(key,
                    self.file_extension)

