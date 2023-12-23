"""Importing"""
import os




def main():
    
    list_images = []
    listed = []
    extensions_list = ["jpg", "jpeg", "png", "bmp", "gif"]
    path = str(input("folder with files, in program folder tree for eg: 'images/...' or 'images/': "))
    list_of_files = os.listdir(path)
    
    count = 0
    for file in list_of_files:
        splited = file.split(".")
        listed.append(splited)
    for one_list in listed:
        #os.rename
        if len(one_list) <= 1:
            continue
        print(f"zdj{count:03d}.{one_list[1]}")
        count += 1




if __name__ == "__main__":
    main()