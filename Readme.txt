wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

google-chrome --version


mkdir Downloads

cd cQubeTesting
source venv/bin/activate

python -m unittest TestSuites/Smoke_Testing.py
python -m unittest TestSuites/Functional_Testing.py
python -m unittest TestSuites/Regression_Testing.py
python -m unittest TestSuites/Sanity_Testing.py

sudo apt update
sudo apt install python-pip
pip --version


pip install HTMLTestRunner-Python3
pip install pandas
pip install selenium






