import subprocess

def update():
    print("업데이트 시작")
    subprocess.run('mkdir test',shell=True)
    print("업데이트 끗")