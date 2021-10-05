import os

if os.path.isdir('./') :
    dirpath = "./"
    numbers = os.listdir(dirpath)
else :
    numbers = '없다고!!!'
print(numbers)
print(os.path.isdir('c:/2nd-project/S05P21B307/backend/paint_game'))
print(os.listdir("./"))
print(os.getcwd())
# C:\Documents\Newsletters\Summer2018