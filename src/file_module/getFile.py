from urllib import request
import zipfile
import shutil
import fnmatch
import os
import re

def classify(path, pattern, type_dir):
    pattern = fnmatch.translate(pattern)
    for path, dir, filelist in os.walk(path):
        for name in filelist:
            m = re.search(pattern, name)
            if m:
                shutil.copy(path + '/' + name, type_dir)

def get_file(user, repo, branch, type):
    tmp_dir = './'+ repo + '-' + branch
    repo_dir = './'+ os.path.join(user, repo)
    type_dir = './'+ os.path.join(user, repo, type)
    zip_path = './'+ os.path.join(user, repo + '.zip')

    if not os.path.exists(user):
        os.mkdir(user)

    if not os.path.exists(repo_dir):
        os.mkdir(repo_dir)

    if not os.path.exists(type_dir):
        os.mkdir(type_dir)

    if not os.path.exists(zip_path):
        with request.urlopen('https://github.com/' + user + '/' + repo + '/archive/' + branch + '.zip') as download:
            with open(zip_path, 'wb') as outfile:
                outfile.write(download.read())

    zip_file = zipfile.ZipFile(zip_path)
    zip_file.extractall()

    classify(tmp_dir, "*." + type, type_dir)
    shutil.rmtree(tmp_dir)
    # os.remove(zip_path)
