"""Importing"""
import os


def main():
    """Main program without functions"""

    list_images_src = []
    listed = []
    path = str(input("folder with files, in program folder tree for eg: 'images/...' or 'images/': "))
    list_of_files = os.listdir(path)

    file_id = 0
    for file in list_of_files:
        splited = file.split(".")
        listed.append(splited)
    for one_list in listed:
        #os.rename
        if len(one_list) <= 1:
            copied_list = listed.copy()
            copied_list.remove(one_list)
            continue
        for el in list_of_files:
            src = path + el
            list_images_src.append(src)
            os.rename(f"{list_images_src[file_id]}",f"{path}zdj{file_id:03d}.{one_list[1]}")
            file_id += 1

#++++++++++++++TODO  implement not to change catalog names#++++++++++++++

if __name__ == "__main__":
    main()
    