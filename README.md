# Software to manage chess tournament
## Project 4 OpenClassRooms (application with MVC pattern and POO architecture)
This script allow users to manage a chess tournament
## Installation
```sh
"git clone https://github.com/LeChat76/Projet4OC.git"
"cd Projet4OC"
Create virtual environment :
* "python -m venv .venv"
* activate environment :
    * for Linux "source .venv/bin/activate"
    * for Windows ".\.venv\Scripts\activate"
Install all needed libraries by typing : "pip install -r requirements.txt"
```
## Execution
```sh
Simply launch the script by typing "py main.py" and follow instruction :
* this project is in progress so be patient ;-)
```
## How to use
```sh
- Create somes users            (menu 1-1)
- Create tournament             (menu 2-1)
- Start tournament              (menu 2-3)
- Display reports               (menu 3  )

Menu branches :
1 ) manage players              (menu 1)
    |_ create players           (....-1)
    |_ display created players  (....-2)
    |_ delete players           (....-3)
2 ) manage tournaments          (menu 2)
    |_ create tournaments       (....-1)
    |_ display tournaments      (....-2)
    |_ start tournament         (....-3) 
    |_ resume tournament        (....-4)
3 ) reporting                   (menu 3)
    |_ display scores           (....-1 & ....-2)
    |_ display players          (....-3 & ....-4)
    |_ display tournaments      (....-5)
    |_ display detailled tourn. (....-6)
```
## Generate new flake8 report
```sh
-In this projet I do not use default line lenght(79) so you need to modifiy this value in the config file
 located in ".venv\Lib\site-packages\flake8" folder file named "defaults.py". Use your favorite text editor
  to modify the line "MAX_LINE_LENGTH = 79" by "MAX_LINE_LENGTH = 119". Otherwise you will only see errors
  about line lenght.
- From Projet4OC folder, launch "flake8 models controllers views --format=html --htmldir=flake-report".
- The HTML report will be generated in the "flake-report" folder, file "index.html".
```
## Features
```sh
- data persistence (stored in json file)
- resume tournament
```
## Features to come 
```sh
 - graphical interface (with tkinter)
```