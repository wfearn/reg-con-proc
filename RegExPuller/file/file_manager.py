import os, glob

BASE_EXTENSION = "*.{}"
NEW_FILE_BASE = "{}_{}.%s"

class FileManager:
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

        for f in glob.glob(BASE_EXTENSION.format(self.file_extension)):
            yield os.path.abspath(f)

    def save_contract_files(self, file_dictionary):
        print "Saving contract files"
        counter = 0

        for contract in file_dictionary:

            next_file_name = self.new_file_name.format("contract",
                    counter)

            counter += 1

            f = open(next_file_name, "w")
            print "Opening new file %s" % next_file_name

            previous = ""

            for string in contract:

                if string != previous:

                    f.write(string + "\n")

                previous = string



    #TODO: Consider a separate "SectionManager" class to replace the section
    #puller

