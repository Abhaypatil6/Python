# It create the folder


import os
# if(not os.path.exists("data")):
#     os.mkdir("data")
# for i in range(1,101):
#     os.mkdir(f"data/Day {i}")

#if u want to change the name of folder

# for i in range(1,101):
#     os.rename(f"data/Day {i}",f"data/Tutorial {i}")

# for i in range(1,101):
#     os.rename(f"data/Tutorial{i}",f"data/Tutorial {i}")

# folders=os.listdir("data")
# print(folders)
print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))  # folder madhla pn kay aahe display hotay