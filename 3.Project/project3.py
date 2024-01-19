"""↓ ↓ ↓Importing↓ ↓ ↓"""
import os
import sys

list_images_src: list = []
listed: list = []
Naming_Pattern: str = ""
List_Of_Files: list = []
directory_path: str = ""

def main():
    """Main program"""
    global directory_path
    global Naming_Pattern
    global List_Of_Files
    try:
        directory_path = if_slash(str(input("""path to folder with files,
                                            in program folder tree for eg:
                                            'images/...' or 'images/': """)))
        if directory_path == "":
            directory_path = if_slash(str(input("""path to folder with files,
                                                in program folder tree for eg:
                                                'images/...' or 'images/': """)))
        Naming_Pattern = str(input("""Pattern to name all files for eg:
                                   'photos', 'vacation', 'kitty', etc..: """))
    except (FileNotFoundError, IndexError):
        print("Error occured, try again")
        sys.exit(0)

    List_Of_Files = os.listdir(directory_path)
    split(List_Of_Files)
    if_have_ext(listed)
    if_proper_ext(listed)
    renaming_checking(listed)
    print("Work done")

def if_slash(typed_path):
    """↓ ↓ ↓check if slash at end of path is correct - if not add one↓ ↓ ↓"""
    last_char_list = [ "]", ":", "\\","?", ";", "#", "$", "@", "%", "^", "&", "'",]
    last_slash = typed_path[len(typed_path) -1]
    if last_slash != "/":
        if last_slash in last_char_list:
            typed_path = typed_path.rstrip(typed_path[-1])
            typed_path = f"{typed_path}/"
            print(f"Attention! Path changed to: '{typed_path}' !")
            return typed_path
        if last_slash.isalpha() or last_slash.isdigit():
            typed_path = f"{typed_path}/"
            print(f"Attention! Path changed to: '{typed_path}' !")
            return typed_path
    if last_slash == "/":
        return typed_path
    else:
        print("Typed path is wrong, please try again")
        raise FileNotFoundError


def split(to_path):
    """↓ ↓ ↓split list to list to further use in extensions↓ ↓ ↓"""
    for file in to_path:
        splited = file.split(".")
        listed.append(splited)
    return listed

def if_have_ext(el_list):
    """↓ ↓ ↓ If there is a file without extension, will be omitted and removed from list ↓ ↓ ↓"""
    for el in el_list:
        if len(el) <= 1:
            for el_remove in el:
                List_Of_Files.remove(el_remove)
                listed.remove([el_remove])
        else:
            continue
    return List_Of_Files, listed

def if_proper_ext(el_list):
    """↓ ↓ ↓Rename only photos, providen graphic files ↓ ↓ ↓"""
    for little_list in el_list:
        if little_list[1] not in ["jpg", "jpeg", "gif", "png"]:
            not_photo = f"{little_list[0]}.{little_list[1]}"
            print(f"{not_photo} was not renamed because is not a proper graphic file.")
            List_Of_Files.remove(not_photo)
            listed.remove(little_list)
    return List_Of_Files, listed

def renaming_checking(final_list):
    """↓ ↓ ↓ If file is a directory, will be omitted and removed from list,↓ ↓ ↓
    ↓ ↓ ↓ checking if file or directory and final renaming↓ ↓ ↓"""
    file_id = 0
    for little_list in final_list:
        full_file_name = f"{little_list[0]}.{little_list[1]}"
        is_file = os.path.isfile(f"{directory_path}{full_file_name}")
        if is_file is True:
            src = directory_path + full_file_name
            list_images_src.append(src)
            print(f"""{list_images_src[file_id]} changed name to:
                    {directory_path}{Naming_Pattern}{file_id:03d}.{little_list[1]}""")
            os.rename(f"{list_images_src[file_id]}",
                      f"{directory_path}{Naming_Pattern}{file_id:03d}.{little_list[1]}")
            List_Of_Files.remove(full_file_name)
            file_id += 1
        else:
            List_Of_Files.remove(full_file_name)

if __name__ == "__main__":
    main()
