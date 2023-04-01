# SL-Utils

This program is meant to be a Quality of Life utility for Shatterline. Although the titles are self-explanatory, I will explain the three separate scripts here.

## bhop.py
This script is coded to be a bunnyhop script for Shatterline. If you hold down space, it spams the spacebar for you.
To use this script, you will have to know the basics to b-hopping. PierreCHT has a useful video that teaches the basics of [bhopping](https://www.youtube.com/watch?v=oo3wmAbwYig&t=49s).

### Known Issues:
Sometimes, the spacebar can get stuck down. You can resolve this when it happens by simply pressing space again. I am working on fixing this.

## orbit_perfect_ult_auto.py 
This script is meant to be used on orbit only. It detects if you are playing orbit, then if you are, allows you to press a button to ult, then dash forward. The timing is supposed to be perfect so that the ult activates fully and damages enemies around you right when you get there.

## orbit_perfect_ult_manual.py
This script is a subset of the above script, but it is manually opened and activated instead of trying to detect when you're on orbit. 

Note that this way will use slightly less resources trying to detect orbit, and can be more accurate as sometimes the automatic script can falsely detect that you are on orbit, or falsely detect when you are not. **However,** this is a sacrifice of ease of use. I would recommend trying out the automatic script, and if it does not work for you, then just use this one. 

## anti-afk.py
This script is meant to be used as an AFK tool in expedition or co-op. It is best used if you want to play 1vE (if you run this on two computers) or 2vE (running on one computer). 

# Usage

### Basic Requirements:
You will need [Python](https://www.python.org/downloads/) to allow the program to function at all.

You will need [Git](https://git-scm.com/downloads) to clone the repo.

Once Python is installed, navigate to a folder you would like this script to be in, then clone the repo with:

```
git clone https://github.com/falsetf/SL-Utils/
```

Next, run `install_requirements.bat`. Note that this will not work on Linux and I am too lazy to create a .sh version. But if you are using linux, you will most likely know what to do anyways.

When the requirements are installed, you can launch the scripts that you want. Once these are open, you can close them by right clicking the tray icon, and clicking Quit.

If you enounter any issues, please open an Issue or message me directly on discord, false#0001.
