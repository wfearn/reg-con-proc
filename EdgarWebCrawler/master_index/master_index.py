COMPANY = 1
URL = 4
DATE = 3

class MasterIndex:
    def __init__(self, master_index_file):
        self.master_index = []

        self.current_index = 0

        for line in master_index_file:
            if self.contains_8k(line):

                line = line.split('|')

                #url has new line character that makes it invalid.
                url = line[URL].strip('\n')

                self.master_index.append( (line[DATE], url, line[COMPANY]) )

    def contains_8k(self, line):
        line = line.split('|')

        for word in line:
            if word == '8-K':
                return True

        return False

    def get_8ks_at_current_index(self):
        for i in range(self.current_index, len(self.master_index)):

            self.current_index = i

            yield self.master_index[i]

    def get_8ks_from_beginning(self):
        for i in range(0, len(self.master_index)):

            self.current_index = i

            yield self.master_index[i]


    def get_8ks_from_index(self, index):
        for i in range(index, len(self.master_index)):

            self.current_index = i

            yield self.master_index[i]

    def get_current_index(self):
        return self.current_index
