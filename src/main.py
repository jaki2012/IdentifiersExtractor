from file_module import getFile
from c_module import getCIdentifiers
from cpp_module import getCppIdentifiers
#from cs_module import  getCSIdentifiers
from java_module import getJavaIdentifiers
#from js_module import getJavaScriptIdentifiers
#from go_module import getGoIdentifiers
from py_module import getPython3Identifiers
from php_module import getPHPIdentifiers
#from swift_module import getSwift3Identifiers
from objc_module import getObjCIdentifiers
import os
import sys
import re
import random
from antlr4 import *
import codecs
import argparse
from identifiers_filtering_module import typeFilter
from identifiers_filtering_module import lengthFilter

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--owner', type=str, default = None)
parser.add_argument('--repository', type=str, default = None)
parser.add_argument('--branch', type=str, default = 'master')
parser.add_argument('--file-type', type=str, default = None)
parser.add_argument('--file-name', type=str, default = 'identifiers_list.txt')
parser.add_argument('--identifier-type', type=str, default = 'mixed')
parser.add_argument('--minlength', type=int, default = 2)
parser.add_argument('--maxlength', type=int, default = 25)
parser.add_argument('--number', type=int, default = 500)


args = parser.parse_args()

'''
user = 'antlr'
repo = 'grammars-v4'
branch = 'master'
type = 'm'
'''
user = args.owner
repo = args.repository
branch = args.branch
type = args.file_type
if (type != 'c') and (type != 'cpp') and (type != 'java') and (type != 'py') and (type != 'php') and (type != 'm'):
    print('The type of ',type,' file is not supported.')
    print('c, cpp, java, py, php, m are supported currently.')
    exit()
if (not args.file_name.endswith('.txt')):
    print('The name of file is not end with \'.txt\'')
    exit()
if (args.identifier_type != 'singlecase') and (args.identifier_type != 'camelcase') and (args.identifier_type != 'separator') and (args.identifier_type != 'containdigits') and (args.identifier_type != 'mixed'):
    print('The type of identifier',args.identifier_type,'is not supported.')
    print('singlecase, camelcase, separator, containdigits, mixed are supported currently.')
    exit()
if (args.maxlength < args.minlength or args.maxlength <= 0):
    print('The length of identifier is illegal.')
    exit()


getFile.get_file(user, repo, branch, type)
file_path = os.path.join(user,repo,type)
file_list = os.listdir(file_path)
iden_dic = {}
for file in file_list:
    path = os.path.join(file_path, file)
    print('-----------------------', file)
    f = codecs.open(path, encoding='UTF-8')
    f = f.read()
    f = re.sub(r'[^\x00-\x7F]+', ' ', f.__str__())
    fh = open(path, 'w')
    fh.write(f)
    fh.close()
    f = FileStream(path)
    iden_dic_f = {}
    if (type == 'c'):
        iden_dic_f = getCppIdentifiers.get_cpp_identifiers_list(f)
    elif(type == 'cpp'):
        iden_dic_f = getCppIdentifiers.get_cpp_identifiers_list(f)
    elif(type == 'java'):
        iden_dic_f = getJavaIdentifiers.get_java_identifiers_list(f)
    elif (type == 'py'):
        iden_dic_f = getPython3Identifiers.get_py3_identifiers_list(f)
    elif (type == 'php'):
        iden_dic_f = getPHPIdentifiers.get_php_identifiers_list(f)
    elif (type == 'm'):
        iden_dic_f = getObjCIdentifiers.get_objc_identifiers_list(f)
    iden_dic = dict(iden_dic, **iden_dic_f)

iden_list = iden_dic.keys()
iden_list = typeFilter.type_filter(iden_list, args.identifier_type)
iden_list = lengthFilter.length_filter(iden_list, args.minlength, args.maxlength)
random.shuffle(iden_list)
if len(iden_list)>args.number:
    iden_list = iden_list[0:args.number]
else:
    print('The total number of identifiers extracted from the repository is ', len(iden_list), ', which is less than ',args.number)
sep = '\n'
fl=open(args.file_name, 'w')
fl.write(sep.join(iden_list))
fl.close()


