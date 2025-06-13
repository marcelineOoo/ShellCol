# ShellCol

## 🔍 What's it ?
A simple CLI color converter (RGB, Hex, HSL, HSV).  
I made it because I was bored and annoyed by having to visit a website or ask an AI just for a simple color conversion.  
So I decided to build my own lightweight tool.

## 📥 Installation

Installation is simple — just go to the [releases directory](./releases/) and choose your operating system.  
For Linux, it should work on all x86_64 Linux distributions.  
For Windows, it works on all x86_64 Windows versions (tested on Windows 11 Pro).  
It has also been tested on Ubuntu LTS and Arch Linux.

I can't build it for macOS, so if any macOS user wants to give it a try, feel free! 😉

## ⚒️ How to use it?

It’s simple:

- **On Linux:** Open a terminal, navigate to the directory where the program is located, and run:
```bash
./main
```
- **On Windows (cmd):** Open cmd, navigate to the directory where the program is located, and execute:
```
main.exe
```
**On Windows (PowerShell):** Open PowerShell, navigate to the directory where the program is located, and run:
```
.\main.exe
```

Next, just follow the prompts — it’s simple!  
Choose the color format you want to convert from by entering a number (for example, enter 1 for Hex).  
Then choose the output format (for example, enter 2 for RGB).  
After that, enter the color code (with or without the `#` for Hex).  
Press Enter, and voilà!  

Important:  
- Don’t include parentheses `()` in your input.  
- For RGB, HSL, and HSV formats, be sure to include commas `,` between values.  

The script will keep running even if you make input mistakes — only an internal error or pressing `Ctrl+C` will stop it.

## ⚙️ Requirements
Both of these scripts are compiled with PyInstaller, which means the program runs without requiring you to install anything on your system.  

However, if you want to modify the script, you will need Python 3.12 (which I used), along with the `colormath` library and PyInstaller to compile it yourself.  

You can find the source code [here](main.py) and the dependencies listed in [requirements.txt](./requirements.txt).

## 📝 Contribution
Contributions, bug reports, and suggestions are warmly welcomed! Feel free to [open an Issue](https://github.com/marcelineOoo/ShellCol/issues) or submit a Pull Request.

## 📜 License

See [LICENSE](./LICENSE) for license details (MIT).