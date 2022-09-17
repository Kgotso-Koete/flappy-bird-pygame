from cx_Freeze import setup, Executable

# with help from :https://pythonprogramming.net/converting-pygame-executable-cx_freeze/
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

setup(
    name="flappy_bird_pygame",
    version="0.1",
    description="",
    options={"build_exe": build_exe_options},
    executables=[Executable("flappy_bird_pygame.py")],
)  # Program name
