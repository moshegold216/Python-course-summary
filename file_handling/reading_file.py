import os

# for readimg the file or maybe to change the file we have -opem file (name,the act)
filename = r"C:\Users\משהגולדשטיין\OneDrive - click\Documents\MY PR\moshe.txt"
#  to write in the file and change all
with open(filename, "a", encoding="utf-8") as file:
    file.write("\nmoshe is noiy ")

    # for readimg the file or maybe to change the file we have -opem file (name,the act)
with open(filename, "r", encoding="utf-8") as file:
    print(file.read())
# not change too only added contact
# with open(filename, "r", encoding="utf-8") as file:
#     file.write("\nmoshe is noiy ")