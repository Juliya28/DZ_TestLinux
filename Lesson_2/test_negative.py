from checkout import checkout

path_dir = '/home/user/tst'
path_arch: str = 'arx2.7z'
path_to_dir = '/home/user/out'


def test_step5():
    # test 5
    assert checkout('cd {}; 7z e arx2.7z -o{}'.format(path_dir, path_to_dir),
                    "ERROR: "), "Test5 Fail"


def test_step6():
    # test 6
    assert checkout('cd {}; 7z t {}'.format(path_dir, path_arch), "Everything is OK"), "Test6 Fail"
