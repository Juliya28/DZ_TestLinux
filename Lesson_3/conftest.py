import random
import string
import subprocess
from datetime import datetime

import pytest
import yaml

from checkout import checkout_positive

with open('config.yaml') as f:
    data = yaml.safe_load(f)
# or from conftest import data


@pytest.fixture()
def make_folders():
    # create all path in dir
    return checkout_positive("mkdir {} {} {} {} {}".format(data['folder_in'], data['folder_out'], data['folder_ext'], data['folder_badarx'],
                                                           data['folder_ext2']), "")


@pytest.fixture()
def clear_folders():
    # remove all in dir /* all contains
    return checkout_positive("rm -rf {}/* {}/* {}/* {}/* {}/*".format(data['folder_in'], data['folder_out'], data['folder_ext'], data['folder_badarx'],
                                                                      data['folder_ext2']), "")


@pytest.fixture()
def make_files():
    # create random named(letters and numbers, length k =5) files which return as list
    list_off_files = []
    for i in range(data['count']):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(
                "cd {}; dd if=/dev/urandom of={} bs={}M count=1 iflag=fullblock".format(data['folder_in'],
                                                                                        filename, data['size_of_file']), ""):
            list_off_files.append(filename)
    return list_off_files
# bs={}M size from config

@pytest.fixture()
def make_subfolder():
    # create random named(letters and numbers, length k =5) files and folders which return as list
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive("cd {}; mkdir {}".format(data['folder_in'], subfoldername), ""):
        return None, None
    if not checkout_positive(
            "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data['folder_in'], subfoldername,
                                                                                      testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_bad_arx(make_folders, clear_folders, make_files):
    checkout_positive("cd {}; 7z a {}/arx1.7z".format(data['folder_in'], data['folder_badarx']),
                      "Everything is Ok"), "Test bad Fail"
    return checkout_positive("truncate -s {}/badarx.7z".format(data['folder_badarx']), ""), "test FAIL"


@pytest.fixture(autouse=True)
def print_time():
    time = ("Time: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    return time


@pytest.fixture()
def create_file_txt(print_time):
    for i in range(1, 200):
        filename = '{}stat.txt'.format(i)
    if checkout_positive("cd {}; touch {}".format(data['folder_in'], filename), ""):
        return filename
    else:
        return None
    with open(filename, 'a', encoding='utf-8') as f:
        f.writelines('\n'.join(print_time, data['count'], data['size_of_file']))