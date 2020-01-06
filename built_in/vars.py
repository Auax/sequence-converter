import colorama

# TITLE
title = f"""                                                                                              _               
                                                                                             | |              
  ___   ___   __ _  _   _   ___  _ __    ___  ___  ______  ___  ___   _ __ __   __ ___  _ __ | |_  ___   _ __ 
 / __| / _ \ / _` || | | | / _ \| '_ \  / __|/ _ \|______|/ __|/ _ \ | '_ \\\ \ / // _ \| '__|| __|/ _ \ | '__|
 \__ \|  __/| (_| || |_| ||  __/| | | || (__|  __/       | (__| (_) || | | |\ V /|  __/| |   | |_| (_) || |   
 |___/ \___| \__, | \__,_| \___||_| |_| \___|\___|        \___|\___/ |_| |_| \_/  \___||_|    \__|\___/ |_|   
                | | {colorama.Fore.GREEN}With this project you can transform a sequence of images to a video.{colorama.Fore.WHITE}
                |_| {colorama.Fore.GREEN}Also, you can transform a video to a sequence of images.{colorama.Fore.WHITE}

"""

# HELP
help = colorama.Fore.GREEN + f"""
Important{colorama.Fore.WHITE}
In the case of transforming a sequence of images, the video will be outputted
in the directory path that you opened the Terminal 


The same happens when you transform a video to a sequence of images, but the images 
will be saved in a folder called **OUTPUT** (if there's no output folder, 
a new one will be created)

---
{colorama.Fore.GREEN}
Graphic example:
Base Folder before transforming:

{colorama.Fore.WHITE}
.
├─ .main.py
├─ .README.md
├─ .built_in
└─ ...

{colorama.Fore.GREEN}
Transforming a video to a image sequence...
Base Folder after transforming:

{colorama.Fore.WHITE}
.
├─ .main.py
├─ .README.md
├─ .built_in
├─ .OUTPUT
│  ├─ frame1.jpg
│  ├─ frame2.jpg
│  └─ ...
└─ ...

{colorama.Fore.WHITE}
Any Suggestion - ryux120@gmail.com

---
© Ibai Farina - 2020"""
