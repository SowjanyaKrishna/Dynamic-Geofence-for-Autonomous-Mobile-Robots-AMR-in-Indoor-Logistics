# Flask Backend of Synergieregion Project
Backend Installation
syn_back folder is the backend of the Dynamic Geofence Application, implemented in flask microframework. Below mentioned figure shows the overview of it.


![image](https://github.com/SowjanyaKrishna/Dynamic-Geofence-for-Autonomous-Transport-Robots-AGV-in-Indoor-Logistics/assets/128833366/a28bb23a-3be0-4dc0-b38c-442d72c3dfe0)


Above mentioned software can be installed on a PC by following below mentioned steps:
1. Clone the source code from GitHub by cloning the repository or downloading the .zip file (link)
2. Open the application in any chosen IDE (Visual studio code or pycharm)
3. Open the terminal (on a chosen IDE) and run the command:
  pip install -r requirements.txt
This installs all the required packages mentioned in the requirements.txt file.
4. The virtual environment files are stored in the name venv and can be found in the project directory.
5. The system needs to use this virtual environment. To activate the virtual environment, use the following command:
For linux machine-
  $ source *syn_back folder location*/venv/bin/activate
Eg: $ source /Users/’Username’/Downloads/syn_back/venv/bin/activate
For windows machine-
  $ *syn_back folder location* \venv\Scripts\activate
Eg: C:\Users\'Username'\venv\Scripts\activate
6. Flask needs to be told how to import it, by setting the FLASK_APP environment variable:
(venv)$ export FLASK_APP=syn_back.py
