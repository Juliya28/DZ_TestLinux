from checkout import checkout
from  checkout import  crc32

path_dir = '/home/user/tst'
path_arch: str = '/home/user/arx2'


def test_step1():
    assert checkout('cd {}; 7z a {}'.format(path_dir, path_arch), "Everything is OK"), "Test1 Fail"


def test_step3():
    assert checkout('cd {}; 7z u {}'.format(path_dir, path_arch), "Everything is OK"), "Test3 Fail"


def test_step4():
    assert checkout('cd {}; 7z d {}'.format(path_dir, path_arch), "Everything is OK"), "Test4 Fail"


def test_step7():
    assert checkout("cd {}; 7z l {}".format(path_dir, path_arch), "Everything is OK"), "Test7 Fail"


def test_step8():
    assert checkout("cd {}; 7z x arx2.7z -o{}".format(path_dir, path_arch), "Everything is OK"), "Test8 Fail"


def test_step9(b=None):
    if crc32(b, 'h_crc') == checkout('7z h {}'.format(path_arch), "Everything is OK"):
        return True
    else:
        return False
