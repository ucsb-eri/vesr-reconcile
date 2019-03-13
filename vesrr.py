#!/usr/bin/env python
import argparse
import csv

parser = argparse.ArgumentParser(description='Process two tab delim files.')
parser.add_argument('files', nargs=2,help='files to process - authorize file followed by drupal file')
args = parser.parse_args()

# need to strip out \r from the files
# need to filter out

class tabDelim(object):
    def __init__(self,file):
        print "Reading file:",file
        self.readData(file)

    def readData(self,path):
        with open(path) as f:
            reader = csv.reader(f, delimiter="\t")
            self.data = list(reader)

class drupClass(tabDelim):
    # 5 is email
    # 6 is phone
    def __init__(self,file):
        super(self.__class__,self).__init__(file)
        for record in self.data:
            print record[5]

class authClass(tabDelim):
    # 23 is email
    # 7 is invoice
    def __init__(self,file):
        super(self.__class__,self).__init__(file)
        for record in self.data:
            print record[7],record[8],record[23]
            pass

d = drupClass(args.files[1])
a = authClass(args.files[0])

#  ./vesrr.py ../Download20190312-093951.txt  ../vesr-drupal.txt
#print a.data
