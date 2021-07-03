
cQube Release-2.0

Prerequisites:
  To Run Selenium python scripts ,Install pycharm in your system
  Google Chrome need to be installed in the server or local machine.
  Chrome driver need to be downloaded and placed in the cQubeTesting-2.0/Driver folder
Steps to install the google chrome

  Open the terminal (Ctrl+Alt+t) in the ubuntu
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  sudo apt install ./google-chrome-stable_current_amd64.deb
  Check chrome brower version using command -> google-chrome -version
  	
Steps to Download the chrome driver 
Note: Based on chrome browser version need to download chrome driver 
   https://sites.google.com/a/chromium.org/chromedriver/downloads

Steps to execute the test script
	1.Open the Terminal (Ctrl+Alt+t) in the ubuntu
	2.Clone the cQubeTesting-2.0 project from github i.e git clone [repository url] 
	2.sudo apt update
	3.sudo apt install python3-pip
	4.Execute the Requirement.txt in the terminal (Requirement.txt file present in the cQubeTesting-2.0 Folder) [mandatory]
	    sudo pip3 install -r Requirement.txt 
	5.Fill the config.ini file (config.ini file present in the cQubeTesting-2.0 Folder).
	        Mandatory fields for installation and upgradation of backend configuration and also to check the json files in the s3 output bucket
		
                    [config]
                    domain=
                    username=
                    password=
                    basedirpath= # installation directory provided in the config.yml file ex:/opt
                    host=localhost
                    port=5432
                    database= # db name which is provided in the config.yml file
                    user= # db user which is provided in the config.yml file
                    db_password= # db user which is provided in the config.yml file
    6. Before running Regression and System suites please fill the data_sources.ini file to run customized suite run

    Execution of automation testscripts for both installation and upgradation of backend configuration

            python3 -m unittest TestSuites/cQubeBackendConfiguration/run_configuration.py

    Mandatory fields for cQube UI application
                  [config]
                  domain= #Enter the url of the cqube application ex: https://<domainname>/ or http://<ip>:4200
                  username= #Enter the username of report viewer
                  password= #Enter the password of report viewer
                  admin_username = #Enter the admin user name
                  admin_password = #Enter the admin password
                  createadmin= #for creating new admin user provide name of admin
                  adminpassword= # Enter password for new admin
                  createviewer= #for creating new admin user provide name of reportviewer
                  viewerpassword= # Enter password for new viewer
                  createemission= #for creating new admin user provide name of emission user
                  emissionpassword= # Enter password for new emission user

	    
    Navigate to cQubeTesting-2.0 Directory in the terminal (ex cd /home/ubuntu/cQubeTesting-2.0)
            For Regression:
                python3 -m unittest TestSuites/Regression_suite/regression_map_reports.py
                python3 -m unittest TestSuites/Regression_suite/regression_chart_table_reports.py
                python3 -m unittest TestSuites/Regression_suite/regression_diksha_tpd_reports.py
                python3 -m unittest TestSuites/Regression_suite/regression_exception_reports.py
                python3 -m unittest Admin_console/admin_console_regression_testing.py
            
	    For System Testing:
                python3 -m unittest TestSuites/System_testing_suite/system_testing_suite.py
                python3 -m unittest TestSuites/System_testing_suite/system_suite_2.py
                python3 -m unittest Admin_console/admin_console_system_testing.py
           
	   For Smoke Testing:
                python3 -m unittest TestSuites/SmokeTestSuite/smoke_test_map_reports.py
		python3 -m unittest TestSuites/SmokeTestSuite/smoke_test_chart_table_reports.py
		python3 -m unittest TestSuites/SmokeTestSuite/smoke_test_exception_reports.py
                python3 -m unittest Admin_console/Admin_smoke_testsuit.py

    if any errors like : ImportError: bad magic number in : b'\x03\xf3\r\n' then use this command and again restart execution
                sudo find . -name "*.pyc" -exec rm -f {} \;

    VPN CONNECTION:To navigate to Admin console page please fallow steps

    Please follow the steps for run testscripts for admin console
            1> open vpn based url in browser
               click on advanced --> open unsecured link --> login to openvpn access server
            2> click on user-profile and starts downloading client.ovpn
            3> open terminal with directory of client.ovpn is located
            4> check version of openvpn ,if not exist use command to install : sudo apt-get install openvpn
            5> sudo openvpn --config client.ovpn
            6> provide author userid and password
            7> note: dont close terminal , just open browser and navigate to cQube application
            8> login with admin user and password , admin can access both cQube reports and admin console

    After execution of scripts ,the report will be generated and present in Reports folder


