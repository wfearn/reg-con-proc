import os

DEFAULT_PATH = '/local/wfearn/Documents/NLPLab/edgar_data/8k_forms/{}/{}/master.txt'

BASE_8K_PATH = '/net/perplexity/wfearn/Documents/NLPLab/lab_scripts/reg-con-proc/EdgarWebCrawler/edgar_data/8k_forms/{}/QTR{}/{}'

class FileSaver:
    def save_files(self, files):
        for key, value in files.items():
            path = key.split('/')

            q = path[len(path) - 2]
            year = path[len(path) - 3]

            new_file = DEFAULT_PATH.format(year, q)
            print ("\n\nSaving to new file: %s" % (new_file))
            f = open(new_file, 'w')

            out = value.splitlines()

            for s in out:
                print ('saving %s to file' % s)
                f.write(s.decode('utf-8', 'ignore') + '\n')

    def save_8k_file(self, year, quarter, doc, date, company):
        new_file_name = date + '|' + company + '.txt'

        new_file_path = BASE_8K_PATH.format(year, quarter, new_file_name)
        print('Saving new file to %s' % new_file_path)

        f = open(new_file_path, 'w')

        doc = doc.splitlines()

        for line in doc:
            f.write(line.decode('utf-8', 'ignore') + '\n')
