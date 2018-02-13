import re

def type_filter(identifier_list,identifier_type):
    list = []
    if(identifier_type == 'singlecase'):
        pattern = re.compile('[a-z]+')
        for iden in identifier_list:
            m =pattern.match(iden)
            if m is not None and m.span()[1] == len(iden):
                list.append(iden)
    elif(identifier_type == 'camelcase'):
        pattern = re.compile('[a-zA-Z]+')
        for iden in identifier_list:
            m = pattern.match(iden)
            if m is not None and m.span()[1] == len(iden):
                list.append(iden)
    elif (identifier_type == 'separator'):
        pattern = re.compile('[a-z_$]+')
        for iden in identifier_list:
            m = pattern.match(iden)
            if m is not None and m.span()[1] == len(iden):
                list.append(iden)
    elif (identifier_type == 'containdigits'):
        pattern1 = re.compile('[0-9a-z_$]+')
        pattern2 = re.compile('[0-9A-Za-z]+')
        for iden in identifier_list:
            m = pattern1.match(iden)
            if m is not None and m.span()[1] == len(iden):
                list.append(iden)
            else:
                m = pattern2.match(iden)
                if m is not None and m.span()[1] == len(iden):
                    list.append(iden)
    elif (identifier_type == 'mixed'):
        pattern = re.compile('[0-9a-zA-Z_$]+')
        for iden in identifier_list:
            m = pattern.match(iden)
            if m is not None and m.span()[1] == len(iden):
                list.append(iden)
    return list