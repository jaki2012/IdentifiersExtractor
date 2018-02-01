from file_module import getFile
from c_module import getCIdentifiers
import os
import sys
import re
from antlr4 import *
import codecs

user = 'wenjun1055'
repo = 'c'
branch = 'master'
type = 'c'

getFile.get_file(user, repo, branch, type)
file_path = os.path.join(user,repo,type)
file_list = os.listdir(file_path)
iden_list = {}
for file in file_list:
    path = os.path.join(file_path, file)
    print('-----------------------', file)
    f = codecs.open(path, encoding='utf-8')
    f = f.read()
    f = re.sub(r'[^\x00-\x7F]+', ' ', f.__str__())
    fh = open(path, 'w')
    fh.write(f)
    fh.close()
    f = FileStream(path)
    iden_list_f = getCIdentifiers.get_c_identifiers_list(f)
    iden_list = dict(iden_list, **iden_list_f)
sep = '\n'
fl=open('iden_list.txt', 'w')
fl.write(sep.join(iden_list.keys()))
fl.close()
print(iden_list.keys())

