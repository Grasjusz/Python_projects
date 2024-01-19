Program for renaming image names.

Program have a few updates like "anti misstyped path", if you type path: "test'" program will change path to "test/".
If you type something unusual like "test." program will stop and close, printing "Typed path is wrong, please try again".
Supported formats: "jpg", "jpeg", "png", "bmp", "gif"

Program will print not changed names due to unsupported extensions
and will print changed name "test/old_name.jpg changed name to: test/new_name.jpg"

++++++++++ USAGE ++++++++++
1. Run program in terminal.
2. Type your path to folder where images are, for path is meant to be located in folder where code is.
    [code file], [|folder_name_images| [image], [image] ], [other folders]

    In this case you can just provide path: "folder_name_images/"

3. Next step is to type pattern to change names, typed "new_file" will be renamed to "new_file000.ext", "new_file001.ext"...
4. Program will replace old name with new name in the same folder counting and adding following number, 000, 001, 002....
5. Updates in future.