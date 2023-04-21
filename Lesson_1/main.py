import subprocess

if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release\n', shell=True,
                            stdout=subprocess.PIPE, encoding='utf 8')
    out = result.stdout
    print(out)
    out_new = out.split('\n')
    # print(out_new)

    if result.returncode == 0:
        if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in out_new and 'VERSION_CODENAME=jammy' in out_new:
            print("SUCCESS")
        else:
            print("FAIL")
    else:
        print("FAIL")