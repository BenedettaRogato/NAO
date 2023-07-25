# ANaoRhythm
**Nao Planning Challange - 2021**

This Project focuses on planning a Dance Coreography given constraints on:
- the total time of the coreography 
- mandatory moves that need to be executed.


**Group Members:**
- Stefano Ciapponi

**Windows implementation and new features**
- Chiara Cippitelli
- Benedetta Rogato

#Setup
This project is excecutable on Windows and Unix. Instructions for Unix can be found in README.

To be able to excecute the project Python3 and Python2 must be installed. This project is tested on Python2 v. 2.7.14 and Python3 v. 3.7.0.

To download and extract naoqi, follow this [guide](http://doc.aldebaran.com/2-5/dev/community_software.html#retrieving-software)

1- Clone the repository

	git clone https://github.com/BenedettaRogato/NAO.git

2- Create a Python Virtual Environment 

	python3 -m venv [name]

3- Activate the Virtual Environment

	.\[name]\Scripts\activate

4- Use pip to install the requirements
	
	python3 -m pip install -r requirements.txt
	prerequisite: ffmpeg (https://www.gyan.dev/ffmpeg/builds/ (ffmpeg-git-full.7z )). 
		      To install it correctly, follow the guide: https://phoenixnap.com/kb/ffmpeg-windows
	
# To run the Code:

5- Open Coreographe->Edit->Preferences and Select the **NAO H25 (V40) Robot Model**.

6- Run The Code:

	python3 main.py

7- Write NaoRobot's IP and Port

8- Follow the instructions. If you want another song, you need to add it in the "Music" folder as a .wav file.

9- Enjoy the coreography!

