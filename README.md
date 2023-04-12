# Minecraft External Mod-Loader (MEM-L)
Minecraft External Mod-Loader, also known as MEM-L, is developed by BJune.


## Table of Contents
- [1. What is it?](#what-is-it?)
- [2. Installation](#installation)
- [3. Usage](#usage)
- [4. Final Note](#final-note)

## 1. What is it?
MEM-L is used for easily loading and unloading Minecraft mods in an easy to use CLI format. It does **not** provide or limit what mods the user wants to load. **You assume all risks**. In doing this, it is MEM-L is very hands off. It does not start the game automatically, meaning you should use any launcher you want giving more options for the user.
### It's Mission:
- create a modloader that does not impair on what mods *you* want 
- to not infringe on however you want to start the game
- to be a flexible platform for people to use and love.
- to be fully open source, *always*
## 2. Installation
**Made in Python version 3.11.3. USE THIS VERSION OR LATER**

Download the `.zip` file under: Code, Download ZIP. Once you have the file where you want it to be, unzip it and open its contents. Open a terminal and `cd` to the location of the folder. then, type the command: 
```terminal
python3 setup.py
```
or open the file manually.
Please then refer to `requirements.txt` to install the proper pip libraries.
```terminal
pip install <name>==<version>
```
example:
```terminal
pip install pandas==1.3.4
```

## 3. Usage
You will then be prompted to open the Minecraft Launcher, or to press `s` to get started after opening file.

When you make a modpack, it will create a folder in the directory `ModPacks`. Then open the folder, and put the files into the folder. **This is an important step! The program will not be able to load the mods if the mods are not in the proper folder!**

documentation on commands is accessed by running the command: `help`.

## 4. Final Note
MEM-L is made by one person, me! Some things might be a bit weird or clunky until I can get them fixed and committed. Until then, try your best! I love you all, and to have as much fun using this as I did making it. :heart:
