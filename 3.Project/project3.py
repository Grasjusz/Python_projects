"""Importing"""
import os

list_images_src: list = []
listed: list = []
Naming_Pattern: str = ""
List_Of_Files = ""

def main():
    """Main program without functions"""
    global path
    global Naming_Pattern
    global List_Of_Files
    
    path = str(input("""path to folder with files, in program folder tree for eg:
                     'images/...' or 'images/': """))
    Naming_Pattern = str(input("Pattern to name all files for eg: 'photos', 'vacation', 'kitty', etc..: "))
    List_Of_Files = os.listdir(path)
    split(List_Of_Files)
    if_have_ext(listed)
    if_proper_ext(listed)
    renaming_checking(List_Of_Files)


def split(to_path):
    for file in to_path:
        splited = file.split(".")
        listed.append(splited)
    
def if_have_ext(el_list):
    for el in el_list:
    #↓ ↓ ↓ If there is a file without extension, will be omitted and removed from list ↓ ↓ ↓
        if len(el) <= 1:
            print(el)
            for el_remove in el:
                print(el_remove)
                List_Of_Files.remove(el_remove)
                listed.remove([el_remove])
        else:
            continue
                
def if_proper_ext(el_list):
    #↓ ↓ ↓Rename only photos, graphic files etc↓ ↓ ↓
    for little_list in el_list:
        if little_list[1] not in ["jpg", "jpeg", "gif", "png"]:
            print(little_list)
            not_photo = f"{little_list[0]}.{little_list[1]}"
            print(f"{not_photo} was not renamed becouse is not a graphic file.")
            List_Of_Files.remove(not_photo)
            return List_Of_Files

def renaming_checking(final_list):
    file_id = 0
    for little_list in final_list:
    #↓ ↓ ↓ If file is a directory, will be omitted and removed from list,↓ ↓ ↓
    #↓ ↓ ↓ checking if file or directory and final renaming↓ ↓ ↓
        is_file = os.path.isfile(f"{path}{little_list}")
        print(f"{path}{little_list}-{is_file}")
        if is_file is True:
            src = path + little_list
            list_images_src.append(src)
            print(f"""{list_images_src[file_id]} changed name to:
                    {path}{Naming_Pattern}{file_id:03d}.{little_list[1]}""")
 #              os.rename(f"{list_images_src[file_id]}",f"{path}zdj{file_id:03d}.{one_list[1]}")
            List_Of_Files.remove(little_list)
            file_id += 1
        else:
            List_Of_Files.remove(little_list)
if __name__ == "__main__":
    main()
    