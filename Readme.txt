README.md
cQube
Prerequisites:
  Google Chrome 84.0.4147.135 need to be installed in the server or local machine.
  Chrome driver 84.0.4147.30 need to be downloaded 
  cQubeTesting project need to be cloned from the github.
  
Steps to install the google chrome

  Open the terminal (Ctrl+Alt+t) in the ubuntu
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  sudo apt install ./google-chrome-stable_current_amd64.deb
 
Steps to Download the chrome driver 

   https://sites.google.com/a/chromium.org/chromedriver/downloads
   Unzip the chrome driver and place it in /usr/bin or /usr/local/bin.
   
Steps to Download the selenium Grid 
   
   https://www.selenium.dev/downloads/
   Download the latest stable selenium grid
   Open the terminal and navigate to the selenium grid jar
   Run the command in the terminal : java -jar selenium-server-standalone

Note : Java jdk1.8 need to be already installed in the machine


Steps to execute the test script

	1.Open the Terminal (Ctrl+Alt+t) in the ubuntu
	2.sudo apt update
	3.sudo apt install python3-pip
	4.Execute the Requirement.txt in the terminal (Requirement.txt file present in the cQubeTesting Folder)
	    pip3 install -r Requirement.txt
	5.Fill the config.ini file (config.ini file present in the cQubeTesting Folder)

	  [config]
	  domain=   #Enter the url of the cqube application ex: https://<domainname>/ or http://<ip>:4200
	  username= #Enter the username of report viewer  
	  password= #Enter the password of report viewer
	 
	  admin_domain=     #Enter the url of vpn based admin cQube url
	  admin_username=   #Enter the username of admin  
	  admin_password=   #Enter the password of admin	 
	  
note: 
Before running pytest ,please start the selenium grid by using command: java -jar selenium-server-standalone-3.14.jar  
For Executing the Regression Test suites using pytest 
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/student_attendance_regression_testing.py
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/crc_report_regression_testing.py
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/semester_report_regression_testing.py
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/School_Map_regression_testing.py
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/School_report_regression_testing.py
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/diksha_table_regression_testing.py
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/diksha_chart_Regression_testing.py
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/telemetry_regression_testing.py
	pytest -n <no of testscripts count> --html = Regression.html --self-contained-html pytest_regression_testing/exception_regression_testing.py

For Executin the Smoke Test suites
	pytest -s -v --html=smoke_test.html --html-contained-html TestSuites/SmokeTestSuite/Smoke_Testing.py
	  
	  please fallow the steps for run testscripts for admin console
	  	1> open vpn based url in browser 
		   click on advanced --> open unsecured link --> login to openvpn access server  
		2> click on user-profile and starts downloading client.ovpn 
		2> open terminal with directory of client.ovpn is located
		3> check version of openvpn ,if not exist use command to install : sudo apt-get install openvpn
		4> sudo openvpn --config client.ovpn 
		5> provide author userid and password 
		6> note: dont close terminal , just open browser and navigate to cQube application 
		7> login with admin user and password , admin can access both cQube reports and admin console
	
	6.To Run the Test scripts
	    Navigate to cQubeTesting Directory in the terminal (ex cd /home/ubuntu/cQubeTesting)

	7.To Run Functionality Testing Suite:

		python3 -m unittest TestSuites/FunctionalTestSuite/Run_crc.py
		python3 -m unittest TestSuites/FunctionalTestSuite/Run_SchoolInfraMap.py
		python3 -m unittest TestSuites/FunctionalTestSuite/Run_SchoolInfraReport.py
		
	8.To Run Regression Testing Suite

		python3 -m unittest TestSuites/RegressionTestSuite/Run_Login_And_LandingPage.py
		python3 -m unittest TestSuites/RegressionTestSuite/Run_StudentAttendance.py
		python3 -m unittest TestSuites/RegressionTestSuite/Run_Crc.py
		python3 -m unittest TestSuites/RegressionTestSuite/Run_Semester_Report.py
		python3 -m unittest TestSuites/RegressionTestSuite/Run_SchoolInfraMap.py
		python3 -m unittest TestSuites/RegressionTestSuite/Run_SchoolInfraReport.py

	9.To Execute Smoke Testing suite

		python3 -m unittest TestSuites/SmokeTestSuite/Smoke_Testing.py
		
Note :
Each Single scripts takes more than 4 to 5 hours, you can execute the multiple test scripts by opening the terminal and navigating to the cQubeTesting folder and running the above testing suite.





















