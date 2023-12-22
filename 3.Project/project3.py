from pathlib import Path
import glob
import sys

#regex: ^[^*,'%$^&.@#!~\r\n]{1,30}\.(?:gif|png|jpe?g|bmp|webp)$


def main():
    
    path = "images/*.*"
    list_of_files = glob.glob('images/*.*')
    print(list_of_files)

    for file in glob.glob(path):
        print(file)

#to do: slice to obtain only file name

#change name all files in pattern





if __name__ == "__main__":
    main()