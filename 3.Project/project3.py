"""Importing"""
import os


def main():
    """Main program without functions"""

    list_images_src = []
    listed = []
    path = str(input("""path to folder with files, in program folder tree for eg:
                     'images/...' or 'images/': """))
    naming_pattern = str(input("Pattern to name all files for eg: 'photos', 'vacation', 'kitty', etc..: "))
    list_of_files = os.listdir(path)

    file_id = 0
    for file in list_of_files:
        splited = file.split(".")
        listed.append(splited)
    for one_list in listed:
    #↓ ↓ ↓ If there is a file without extension, will be omitted and removed from list ↓ ↓ ↓
        if len(one_list) <= 1:
            print(one_list)
            for el_remove in one_list:
                print(el_remove)
                list_of_files.remove(el_remove)
        #Rename only photos, graphic files etc.
        if one_list[1] not in ["jpg", "jpeg", "gif", "png"]:
            print(one_list)
            together = f"{one_list[0]}.{one_list[1]}"
            print(together)
            list_of_files.remove(together)
            continue
        for el in list_of_files:
        #↓ ↓ ↓ If file is a directory, will be omitted and removed from list,↓ ↓ ↓
        #↓ ↓ ↓ checking if file or directory and final renaming↓ ↓ ↓
            is_file = os.path.isfile(f"{path}{el}")
            print(f"{path}{el}-{is_file}")
            if is_file is True:
                src = path + el
                list_images_src.append(src)
                print(f"""{list_images_src[file_id]} changed name to:,
                      {path}{naming_pattern}{file_id:03d}.{one_list[1]}""")
 #               os.rename(f"{list_images_src[file_id]}",f"{path}zdj{file_id:03d}.{one_list[1]}")
                list_of_files.remove(el)
                file_id += 1
                break
            else:
                list_of_files.remove(el)
if __name__ == "__main__":
    main()
    