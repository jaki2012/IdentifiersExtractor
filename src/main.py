from file_module import getFile
from c_module import getCIdentifiers
from cpp_module import getCppIdentifiers
#from cs_module import  getCSIdentifiers
from java_module import getJavaIdentifiers
#from js_module import getJavaScriptIdentifiers
#from go_module import getGoIdentifiers
from py_module import getPython3Identifiers
import os
import sys
import re
from antlr4 import *
import codecs

user = 'michaelliao'
repo = 'learn-python3'
branch = 'master'
type = 'py'

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
    iden_list_f = getPython3Identifiers.get_py3_identifiers_list(f)
    print(iden_list_f.keys())
    iden_list = dict(iden_list, **iden_list_f)
sep = '\n'
fl=open('iden_list_py3.txt', 'w')
fl.write(sep.join(iden_list.keys()))
fl.close()
print(iden_list.keys())

