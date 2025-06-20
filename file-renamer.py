import os

directory_list = os.listdir()
new_name = ""
temp_list = []
rename_list = []
for i in directory_list:
    if not i.startswith('.'):
        if i.endswith('.name'):
            new_name = i.removesuffix('.name')
        if '.' in i and not '.name' in i and not '.py' in i:
            rename_list.append(i)
if new_name == "":
    print("please make a .name file.")
    exit()
for i in rename_list:
    for j in rename_list:
        if i.rpartition('.')[0] in j.rpartition('.')[0] and len(i)<len(j) and rename_list.index(i)>rename_list.index(j):
            rename_list.remove(i)
            rename_list.insert(rename_list.index(j), i)
index = 0
for i in rename_list:
    temp_partition = i.rpartition('.')
    temp_list = list(temp_partition)
    if (index < 10):
        temp_list[0] = "".join([new_name, "_0", str(index)])
    else:
        temp_list[0] = "".join([new_name, "_", str(index)])
    temp = "".join(temp_list)
    os.rename(i, temp)
    index = index + 1
