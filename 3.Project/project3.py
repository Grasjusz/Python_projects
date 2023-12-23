"""Importing"""
import os

"""Main program"""
def main():

    list_images_src = []
    listed = []
    extensions_list = ["jpg", "jpeg", "png", "bmp", "gif"]
    path = str(input("folder with files, in program folder tree for eg: 'images/...' or 'images/': "))
    list_of_files = os.listdir(path)


    file_id = 0
    for file in list_of_files:
        splited = file.split(".")
        listed.append(splited)
    for one_list in listed:
        #os.rename
        if len(one_list) <= 1:
            listed.remove(one_list)
            continue
        for el in list_of_files:
            #print(f"{list_of_files[file_id]}")
            src = path + el
            list_images_src.append(src)
            os.rename(f"{list_images_src[file_id]}",f"zdj{file_id:03d}.{one_list[1]}")
            file_id += 1



if __name__ == "__main__":
    main()