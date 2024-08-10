
    # Learn_Top_Words
    #### Video Demo:  https://youtu.be/p28r-9qGEh4
    #### Description:

        # A program for learning the most frequently used words in a selected language. (Polish, English, German).

        ## The program allows you to choose one of three main languages ​​in which communication will take place: Polish, English, German.

        After selecting the guide language, the user can choose one of two languages ​​to learn:
        1. For Polish, learning English, German
        2. For English, learning Polish, German
        3. For German, learning English, Polish

        After selecting the language to learn, the program starts printing words to translate.
        If the answer is correct, a printout with the current score will appear, e.g.; _"Your actual score 45 out of 100 points"_
        If the answer is false, the correct translation of the word will be printed and the program will continue entering another word.
        Once all words have been answered correctly, a message with the actual score (maximum score) will be displayed and the printout will indicate that all words have been translated and the program will close.

        At any level running program, you are able to exit program, just type __"exit program".__

        #TO RUN THE PROGRAM
        1. Run program in terminal by executing "run in terminal" or by typing "python project.py" (remember to be in the same level folder).
        2. Choose your language by typing in terminal.
        3. Choose language to learn by typing in terminal.
        4. Program will start printing words to translate.
        5. To end the program type >"exit program"

        Program includes:
        __project.py__ - main program.
        __lang_engine.py__ - code for printing words, printing actual score, etc - engine of essential program.
        __test_project.py__ - testing cases.
        __level1.csv__ - list of 100 top words in three languages to study.
        __test.csv__ - list of 3 test words for testing.

        __project.py__ - main execution program with base functionalities:
            - main - main run the program, handling exceptions, erros, choosing language.
            - check_language - setting user interface language, if mistaken, program will prompt again with communicate in three languages in which, shall communicate with user.
            - chosen_lang - function checking if learning language is in allowed list and return proper file with list of words to practice.
            - lang_selection - depends on which languages user want to learn, function is calling external file and running proper function (main translating engine).
            - exit_program - printing succesfully exited program and return exit code _0_ meaning exited OK.

        __lang_engine.py__ - the longest in code, but fairly simple. Printing, counting, shuffling, essentialy the engine.
            - main - debugging purposes.
            - exit_program - printing succesfully exited program and return exit code _0_ meaning exited OK.
            - pol_lang - first it will randomly shuffle the word list, next print the word to be translated, if successful, print the points gained, continue with another word. If false, prints the translated word and goes to another word in the list. If all words in the list have been translated, a message will be displayed that all words have been translated and the program will automatically exit. __Designed for polish language user interface.__
            - eng_lang - first it will randomly shuffle the word list, next print the word to be translated, if successful, print the points gained, continue with another word. If false, prints the translated word and goes to another word in the list. If all words in the list have been translated, a message will be displayed that all words have been translated and the program will automatically exit. __Designed for english language user interface.__
            - de_lang - first it will randomly shuffle the word list, next print the word to be translated, if successful, print the points gained, continue with another word. If false, prints the translated word and goes to another word in the list. If all words in the list have been translated, a message will be displayed that all words have been translated and the program will automatically exit. __Designed for german language user interface.__

        __test_project.py__ - testing chosen functions for proper or invalid input.
            - test_exit - testing if exiting is a SystemExit and if the value code is "0".
            - test_check_language - testing if output is in proper language.
            - test_check_language_error - checking handling error if entered word, numbers, blank.
            - test_chosen_lang - testing base of words if specyfied file.
            - test_lang_selection_different_input - test if different input return value or None (as should).

        __level1.csv__ - this is a CSV data file, the CSV file type chosen for its flexibility and better program update and word list update.

        __test.csv__ - file with 3 example words for testing purposes.

     ### Program is partitioned in two parts _project.py_ - main program, _lang_engine.py_ - program for printig and counting words to translate.

     I have chosen this way of structure for better readability and less messy code in one file. Main functions and program goes with project.py.
     lang_engine is the "engine" for proper printing and counting words.

