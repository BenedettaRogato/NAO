# ANaoRhythm
**Nao Planning Challange - 2021**

This Progect focuses on planning a Dance Coreography given constraints on:
- the total time of the coreography 
- mandatory moves that need to be executed.

I tried implementing a Search Algorithm subsampling an infinite tree of Feasible Solutions while also trying to optimize the number of Beat matching moves (moves that start on the first beat of a 4/4 bar).

**Group Members:**
- Stefano Ciapponi

**Windows implementation and new features**
- Chiara Cippitelli
- Benedetta Rogato

# Setup:

This project is excecutable on Windows and Unix. Instructiones for Windows can be found in README_WIN

To be able to excecute the project Python3 and Python2 must be installed. This project is tested on Python2 v. 2.7.14 and Python3 v. 3.7.0.

To download and extract naoqi, follow this [guide](http://doc.aldebaran.com/2-5/dev/community_software.html#retrieving-software)

- Clone The repository:
```
git clone https://github.com/drchapman-17/anaorhythm
```
- Create a Python Virtual Enviroment.
```
python3 -m venv [name]
```
- Access it running the "activate" script in the Bin folder.
```
source [name]/bin/activate
```
- Use PIP to install the requirements
```
pip install -r requirements.txt
```
# To run the Code:
- Open Coreographe->Edit->Preferences and Select the **NAO H25 (V40) Robot Model**.
- Run The Code:
```
python3 main.py
```
- Write NaoRobot's IP and Port.

- Follow the instructions. If you want another song, you need to add it in the "Music" folder as a .wav file.

- Enjoy the coreography!

# Resources:

- [Treelib](https://treelib.readthedocs.io/en/latest/)
- [DuoNao Repo (For The NaoMoves Folder)](https://github.com/ProjectsAI/NAO_Planning_Challenge/tree/main/2020-2021/duonao)
