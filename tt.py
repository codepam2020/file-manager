import os

folder = "E:/Mirror/OneDrive - zhgate/Univ_Materials/Pharm_3_2(2021_2)/test"
file_list = os.listdir(
    "E:/Mirror/OneDrive - zhgate/Univ_Materials/Pharm_3_2(2021_2)/test"
)

count = 1
for i in file_list:
    idx = i.rfind(".")
    try:
        os.rename(folder + "/" + i, folder + "/" + "a" + i[idx:])
    except:
        os.rename(folder + "/" + i, folder + "/" + "a" + str(count) + i[idx:])
        count = count + 1

