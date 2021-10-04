import subprocess

def update():
    print("업데이트 시작")
    subprocess.run('sudo mkdir /home/jenkins/workspace/test/backend/crontab',shell=True)
    print("업데이트 끗")