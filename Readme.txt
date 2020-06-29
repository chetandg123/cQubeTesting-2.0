wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

google-chrome --version

config file need to be filled go to cQubeTesting Folder -> config.ini
[config]
domain=
username=
password=

python3 -m unittest TestSuites/Run_Smoke_Testing.py
python3 -m unittest TestSuites/Run_Functional_Testing.py
python3 -m unittest TestSuites/Run_Regression_Testing.py
python3 -m unittest TestSuites/Run_Sanity_Testing.py

sudo apt update
sudo apt install python3-pip
pip3 --version


pip3 install HTMLTestRunner-Python3
pip3 install pandas
pip3 install selenium
pip3 install configparser
pip3 install pathlib









