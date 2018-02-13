import re

def length_filter(identifier_list, minlength, maxlength):
    list = []
    for iden in identifier_list:
        if(len(iden)>= minlength and len(iden)<=maxlength):
            list.append(iden)
    return list
