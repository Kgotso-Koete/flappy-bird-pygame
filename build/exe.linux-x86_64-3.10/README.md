# About the project

### Description of the project

This is a clone of the video game [Flappy Bird](https://en.wikipedia.org/wiki/Flappy_Bird) built while following the [Clear Code tutorial part 1](https://youtu.be/UZg49z76cLw) and [Clear Code tutorial part 2](https://youtu.be/XRw1FUEsSv4). [Flappy Bird](https://en.wikipedia.org/wiki/Flappy_Bird)is a mobile game developed by Vietnamese video game artist and programmer Dong Nguyen (Vietnamese: Nguyễn Hà Đông), under his game development company .Gears. The game is a side-scroller where the player controls a bird, attempting to fly between columns of green pipes without hitting them

---

### Click here for the [demo](https://replit.com/@KgotsoKoete/Flappy-Bird-Pygame?v=1)

---

### Technology stack

1. Python 3.10.4
2. Pygame 2.1.2

---

### Install the project on Linux or Windows:

1. Download this codebase
2. Install Python 3.10.4 on your machine
3. Install Pygame 2.1.2 (Linux `python3 pip install pygame`) (Windows `python3 -m pip install pygame`)

### 3: Run project

1. Run locally: Navigate to the project folder and run `python3 flappy_bird_pygame.py` to start the game.
2. Run in an an in-browser IDE: Visit the [Replit](https://replit.com/@KgotsoKoete/Flappy-Bird-Pygame?v=1) and run in full screen mode for the best experience.

### Build project executable

Follow the instructions below to build an executable file for Ubuntu Linux

1. Install executable builder `pip install cx_freeze`
2. Build the Linux executable by running the following command `python3 setup.py build`
3. The [Linux executable file](./build/exe.linux-x86_64-3.10/flappy_bird_pygame) will in the following folder `./build/exe.linux-x86_64-3.10`

Follow the instructions below to build an executable file for Windows

1. Ensure that the [set.py](./setup.py) Executable function has the additional argument `base="Win32GUI"` to stop the command window from opening every time the executable is running.
2. Install executable builder `pip install cx_freeze`
3. Build the Windows executable by running the following command `python3 setup.py build`
4. The [Windows executable file](./build/exe.win-amd64-3.10/flappy_bird_pygame.exe) will in the following folder `./build/exe.win-amd64-3.10`. The executable must contain all supporting files in this folder to run.

---

### Acknowledgements

Special thanks to [Clear Code](https://www.youtube.com/c/ClearCode) for a great tutorial. The tutorial was explained very well, brief and very impactful in showing the basics of Pygame.

The tutorial also has a link to the the [original image files](https://github.com/samuelcust/flappy-bird-assets) and the [original sound files](https://www.sounds-resource.com/mobile/flappybird/sound/5309/). The github repo for the actual tutorial can be found [here](https://github.com/clear-code-projects/FlappyBird_Python)
<br/>
<br/>

---

### License

The codebase is MIT licensed unless otherwise specified. Feel free to fork or download this code and use as specified in the license.

#

To be modified further by Kgotso Koete
<br/>
September 2022
