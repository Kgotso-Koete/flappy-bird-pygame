import sys
from cx_Freeze import setup, Executable

# with help from :https://stackoverflow.com/a/72324127/6556133
# with help from: https://stackoverflow.com/a/29671106
# with help from :https://pythonprogramming.net/converting-pygame-executable-cx_freeze/
build_exe_options = {
    "include_files": [
        "flappy_bird_pygame.py",
        "04B_19.TTF",
        "README.md",
        "./assets",
        "./sound",
    ]
}

base = sys.platform if sys.platform.lower() == "windows" else None

setup(
    name="flappy_bird_pygame",
    version="0.1",
    description="",
    options={"build_exe": build_exe_options},
    executables=[Executable("flappy_bird_pygame.py", base=base)],
)  # Program name
