import os

amount = 0
now_dir = os.getcwd()

categories = [
        "banana",
        "bulb",
        "calculator",
        "carrot",
        "clock",
        "crecent",
        "diamond",
        "icecream",
        "strawberry",
        "t-shirt",
    ]

for category in categories:
    if os.path.isdir("/home/jenkins/workspace/test/backend/media/dataset/success/"+category) :
        amount += os.listdir("/home/jenkins/workspace/test/backend//media/dataset/success/"+category)

print(now_dir)

# C:\Documents\Newsletters\Summer2018