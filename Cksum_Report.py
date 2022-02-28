# Importing difflib
import difflib

"""
with open('dev_repo_cksumreport_with_pomandjar.txt') as file_1:
    file_1_text = file_1.readlines()

with open('repo_cksumreport_with_pomandjar.txt') as file_2:
    file_2_text = file_2.readlines()

# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='dev_repo_cksumreport_with_pomandjar.txt',
        tofile='repo_cksumreport_with_pomandjar.txt', lineterm=''):
    print(line)
"""
'''
file_dev_true = open('True_data_dev_directory.txt', 'w')
file_dev_false = open('False_data_dev_directory.txt', 'w')
file_repo_true = open('True_data_repo_directory.txt', 'w')
file_repo_false = open('False_data_repo_directory.txt' , 'w')

with open('dev_repo_cksumreport_with_pomandjar.txt') as f_a, open('repo_cksumreport_with_pomandjar.txt') as f_b:
    a_lines = set(f_a.read().splitlines())
    b_lines = set(f_b.read().splitlines())
print(a_lines)

for line in a_lines:
 #   print(line, '->', line in b_lines)
    if line in b_lines :
        file_dev_true.write(line + "\n")
    else :
        file_dev_false.write(line + "\n")

for line in b_lines:
    if line in a_lines:
        file_repo_true.write(line + "\n")
    else:
        file_repo_false.write(line + "\n")

file_repo_false.close()
file_repo_true.close()
file_dev_false.close()
file_dev_true.close()
'''


file_output = open('output_file.csv', 'a')

with open('dev_path_cksum.txt') as file_dev, open('repo_path_cksum.txt') as file_repo:
    dev_content = ",".join(file_dev.read().split())
    dev_list = list(dev_content.split(","))
    repo_content = ",".join(file_repo.read().split())
    repo_list = list(repo_content.split(","))

print(dev_list)
print(repo_list)

# Python program to Convert a list to dictionary
def Convert(lst):
    res_dct = {lst[i+1]: lst[i] for i in range(0, len(lst), 2)}
    return res_dct

# code
dev_dict = Convert(dev_list)
repo_dict = Convert(repo_list)

dev_key_set = dev_dict.keys()
repo_key_set = repo_dict.keys()

master_list = list(dev_key_set | repo_key_set)

for value in master_list:
    if value in list(dev_dict.keys()) and value in list(repo_dict.keys()):
        if dev_dict.get(value) == repo_dict.get(value):
            file_output.write(value + ", same Cksum in both repo. \n")
        else:
            file_output.write(value + ", Different Cksum in both repo. \n")
    if value in list(dev_dict.keys()) and value not in list(repo_dict.keys()):
        file_output.write(value + ", present in dev directory. \n")
    if value in list(repo_dict.keys()) and value not in list(dev_dict.keys()):
        file_output.write(value + ", present in repo directory. \n")


file_output.close()
