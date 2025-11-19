# About the project

### Description of the project

This is a clone of the video game [Flappy Bird](https://en.wikipedia.org/wiki/Flappy_Bird) built while following the [Clear Code tutorial part 1](https://youtu.be/UZg49z76cLw) and [Clear Code tutorial part 2](https://youtu.be/XRw1FUEsSv4). [Flappy Bird](https://en.wikipedia.org/wiki/Flappy_Bird)is a mobile game developed by Vietnamese video game artist and programmer Dong Nguyen (Vietnamese: Nguyễn Hà Đông), under his game development company .Gears. The game is a side-scroller where the player controls a bird, attempting to fly between columns of green pipes without hitting them

---

### Click here for the [video demo](https://youtu.be/BIAUv-EzMqE)

### Click here for the [playable in-browser demo](https://replit.com/@KgotsoKoete/Flappy-Bird-Pygame?v=1)

1. Play it in the [in-browser game](https://replit.com/@KgotsoKoete/Flappy-Bird-Pygame?v=1) here.
2. Play it on a Windows desktop by downloading the [Windows build folder](./dist/flappy-bird-pygame.exe) and clicking on the .exe file
3. Play it on a Linux desktop by downloading the [Linux build folder](./dist/flappy-bird-pygame) and clicking on the executable file

---

# Screen shot of the application

|             Start Screen             |             Game Screen             |
| :----------------------------------: | :---------------------------------: |
| ![](/screenshots/1_start_screen.png) | ![](/screenshots/2_game_screen.png) |

---

### Technology stack

1. Python 3.12.3
2. Pygame 2.6.1

---

### Install the project on Ubuntu Linux:

1. **Download codebase:** Clone or download the source code to your local machine.

2. **Install System Dependencies:** Pygame requires the SDL2 library. Install it using the following command:

   ```bash
   sudo apt-get update && sudo apt-get install -y libsdl2-dev
   ```

3. **Create a Virtual Environment:** It's recommended to use a virtual environment to manage project dependencies. Navigate to the project's root directory and run:

   ```bash
   python -m venv .venv
   ```

4. **Activate the Virtual Environment:**

   Linux environment
   ```bash
   source .venv/bin/activate
   ```

   Windows environment
   ```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```

5. **Install Python Packages:** Install all the required packages from the `requirements.txt` file:

   ```bash
   pip install -r requirements-windows.txt
   ```

   or

   ```bash
   pip install -r requirements-linux.txt
   ```

---

### 3: Run project

1. Run locally: Navigate to the project folder and run `python flappy_bird_pygame.py` to start the game.
2. Run in an an in-browser IDE: Visit the [Replit](https://replit.com/@KgotsoKoete/Flappy-Bird-Pygame?v=1) and run in full screen mode for the best experience.

### Build a Single Executable for Distribution

To create a single executable file for distribution on platforms like itch.io, we will use `PyInstaller`.

1. **Install PyInstaller:**
   Ensure your virtual environment is active and run:

   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable:**
   Run the appropriate command for your operating system from the project root.

   **For Linux:**

   ```bash
   pyinstaller --onefile --windowed --name flappy-bird-pygame --add-data 'assets:assets' --add-data 'sound:sound' --add-data '04B_19.TTF:.' flappy_bird_pygame.py
   ```

   **For Windows:**

   ```cmd
   pyinstaller --onefile --windowed --name flappy-bird-pygame `
   --add-data "assets;assets" `
   --add-data "app;app" `
   flappy_bird_pygame.py
   ```

   After the process completes, you will find the single executable file inside the `dist` folder. This is the file you can upload for distribution.

3. **Testing the Linux Executable:**
   Before distributing, you can test the executable on Linux.

   First, make the file executable:

   ```bash
   chmod +x dist/flappy-bird-pygame
   ```

   Then, run it from the terminal:

   ```bash
   ./dist/flappy-bird-pygame
   ```

---

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
