# -*- coding: utf-8 -*-

class Data():
    login = "login"
    email = "username"
    passwd = "password"
    new_pass = "newPasswd"
    conf_pass = "cnfPasswd"
    change_pass_btn = "btn"
    homeicon = "home"
    logout = "logout"
    fieldReq = "/html/body/app-root/app-login/div[1]/div[2]/div[2]/form/div[2]/div/label"
    Grade = "grades"
    Subject = "subjects"
    loginbtn = "//button[@type='submit']"
    # admin login
    home ="homeBtn"
    userlist="user"
    userlisttable="//tr/td"
    cuser ="crtUsr"
    cpass ="//a[2]"
    dashboard_options = "//a/div/td[2]"
    back_btn ="//div[@class='col-sm-6']/a"
    createusericon ="//img[@alt='addUser']"
    dots = "leaflet-interactive"
    SAR_Details = "//div[@class='row']/div[@class='col-sm-4']/span"
    hyper_link = "//p/span"
    directory = "//p[contains(text(),' Semester report for:')]/span"
    Download = "download"
    Download_scator ='download'
    s3bucket_select1 ="//*[@id='table']/thead[2]/tr[2]/td[1]/input"
    summ ="//*[@id='summary']/div/td[2]"
    # Dash board
    Dashboard = "menu"
    header = "//h4"
    # Data Replay
    data_replay_icon_id = "replay"
    data_source_select_box_id = "dataSources"
    data_replay_submit_button_css_selector = "div > button:first-of-type"
    data_replay_cancel_button_css_selector = "div > button:last-of-type"
    data_replay_select_year_class = "time"
    # school_infra_Report
    # school_infra = "si"
    infro_dist = "//select[@name='myDistrict']/option"
    infro_block = "//select[@name='myBlock']/option"
    infro_cluster = "//select[@name='myCluster']/option"

    sel_districts = "//select[@name='myDistrict']/option"
    sel_blocks = "//select[@name='myBlock']/option"
    sel_clusters = "//select[@name='myCluster']/option"

    sc_district = "//select[@name='myDistrict']/option[2]"
    sc_block = "//select[@name='myBlock']/option[2]"
    sc_cluster = "//select[@name='myCluster']/option[2]"

    #udise
    udise_drop ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/div/mat-nav-list[8]/mat-list-item/div/mat-icon"
    udise_report ="udiseReport"

    # patchart
    question_id="question_id_allDistricts_"
    indicator_id="indicator_allDistricts_"

    # hyper     ="//*[@id='dist_level']/span"
    hyper = "//p/span"
    dist_hyper = "//*[@id='block']/span[1]"
    # school_hyper = "//*[@id='school']/span[5]"
    block_hyper = "//*[@id='cluster']/span[3]"
    cluster_hyper = "//*[@id='school']/span[5]"


    x = "x_axis"
    y = "y_axis"
    s_dist = "//select[@name='myDistrict']/option[2]"
    # sc_Reportmap
    School_infra = "//*[@id='sideNav']/div/div[1]/div/div/mat-nav-list/div/mat-nav-list[1]/mat-list-item/div/mat-icon"
    Reportmap = "mapReport"
    Report = "tblReport"

    scm_block = "blockbtn"
    scm_cluster = "clusterbtn"
    scm_school = "schoolbtn"

    sc_choosedist = "//select[@id='choose_dist']/option"
    sc_chooseblock = "//select[@id='choose_block']/option"
    sc_choosecluster = "//select[@id='choose_cluster']/option"
    sc_infrascores = "//select[@id='choose_infra']/option"
    sc_no_of_schools = "footer"

    diksha ="//*[@id='sideNav']/div/div[1]/div/div/mat-nav-list/div/mat-nav-list[3]/mat-list-item/div/mat-icon"
    tpds ="//*[@id='sideNav']/div/div[1]/div/div/mat-nav-list/div/mat-nav-list[2]/mat-list-item/div/mat-icon"
    diksha_graph ="chrtReport"
    diksha_table = "dtblReport"
    tpd_progress ="tpd-cp"
    tpd_percentage ="tpd-tp"
    col_course ="clmnReport"
    col_text ="ut"
    content_textbook ="utc"
    exception_click ="//*[@id='sideNav']/div/div[1]/div/div/mat-nav-list/div/mat-nav-list[5]/mat-list-item/div/mat-icon"
    sem_exception = "SemException"
    ener_textbook="//*[@id='sideNav']/div/div[1]/div/div/mat-nav-list/div/mat-nav-list[3]/mat-list-item/div/mat-icon"


    sem_exe ="SemExp"

    scm_dist = "//select[@id='choose_dist']/option[2]"
    scm_blk = "//select[@id='choose_block']/option[2]"
    scm_clust = "//select[@id='choose_cluster']/option[2]"

    Dash_head = "//h4"
    d_names = "//th[contains(text(),'district')]"
    t_head = "//th[contains(text(),'District Name')]"
    login_in = "//span[@class='span']"
    SAR = "stdReport"
    teacher="thrReport"
    Logout = "logout"
    Home_icon = "//i[@id='home']"
    select_district = 'myDistrict'
    select_blocks = 'myBlock'
    select_clusters = 'myCluster'
    select_month = 'month'
    select_year = 'year'
    # login = "//button[@type='submit']"
    select_sem_district = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]'
    select_sem_blocks = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]'
    select_sem_clusters = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]'

    CRC_Districts = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[3]/div[2]/select[1]/option"
    # User_option
    user_options = "//button[@id='usr']/span/mat-icon"
    u_create = "crtUsr"
    p_change = "chPass"

    No_schools = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]'
    No_sem_schools = '/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[4]/div[2]'
    SR_Blocks_btn = "block"
    SR_Clusters_btn = "cluster"
    SR_Schools_btn = "school"
    Download_icon = "//i[@id='download']"
    # user_creation

    create_headtext = "//h2"
    fname = "//input[@name='firstname']"
    mname = "//input[@name='middlename']"
    lname = "//input[@name='lastname']"
    male = "//input[@name='gender'][1]"
    female = "//input[@name='gender'][2]"
    mail = "//input[@name='email']"
    designation = "//input[@name='Designation']"
    confpass = "//input[@name='cnfpass']"
    rolesoptions = "//select/option"
    admin = "//select/option[2]"
    drc = "//select/option[3]"
    drv = "//select/option[4]"
    Adoc = "//select/option[5]"
    Demission = "//select/option[6]"
    changepwd = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list/div/a[2]/div/span"
    new_pwd = "//input[@name='newPasswd']"
    conf_pwd = "//input[@name='cnfpass']"
    submit = "//button[@type='submit']"
    errormsg = "//p"

    # for SAR_2
    SAR_Blocks_btn = "blockbtn"
    SAR_Clusters_btn = "clusterbtn"
    SAR_Schools_btn = "schoolbtn"
    # footer
    schoolcount = "schools"
    students = "students"
    DateRange = "dateRange"

    #management ids
    period = "period"


    SAR_Dnames = "//*[@id='choose_dist']/option"
    SAR_Bnames = "//*[@id='choose_block']/option"
    SAR_cnames = "//*[@id='choose_cluster']/option"

    # semester
    no_schools = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]/span"
    no_students = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[1]/span"
    zoom_in = "//a[@title='Zoom in']"
    zoom_out = "//a[@title='Zoom out']"
    dash_name = "//h4"
    # list of names
    SR_Dnames = "//*[@id='choose_dist']/option"
    SR_Bnames = "//*[@id='choose_block']/option"
    SR_cnames = "//*[@id='choose_cluster']/option"

    crcdist = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[2]/div[2]/select[1]/option"

    year = "//select[@id='year']/option[1]"
    monthnames = "//select[@id='month']/option"
    august = "//select[@id='month']/option[2]"
    Sept = "//select[@id='month']/option[3]"
    Oct = "//select[@id='month']/option[4]"
    blockslist = "//select[@name='myBlock']/option"
    clusterlist = "//select[@name='myCluster']/option"
    back = "//a"
    reg_user = "//a"
    details = "//div[@class='col-sm-4']/span"
    # Dash board
    TAR = "tar"
    SR = "sr"
    CRC = "crcReport"

    # xpath of Dashboard

    crcvisits = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[1]/span"
    totalschools = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[2]/span"

    visited = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[3]/span"
    notvisited = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[4]/span"

    range = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[5]/span"

    # Table in CRC
    crc_districtwise_csv = "//*[@id='select']/select/option[2]"
    crc_clusterwise_csv = "//*[@id='select']/select/option[4]"
    # rowby data
    distrows = "//tr[@class='odd']/td"
    headers = "//tr[@role='row']/th"
    footer = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-crc-report/div[1]/div[5]/div/span"

    crc_districtlist = "//*[@id='dist']/option"
    crc_blocklist = "//*[@id='block']/option"
    crc_clusterlist = "//*[@id='cluster']/option"

    # select_type
    distwise = "//select[@name='downloadType']/option[2]"
    blkwise = "//select[@name='downloadType']/option[3]"
    clusterwise = "//select[@name='downloadType']/option[4]"
    schoolwise = "//select[@name='downloadType']/option[5]"

    crcdistrict = "//select[@name='myDistrict']/option"
    selecttype = "//*[@id='select']/select/option"

    Notemsg = "//div[@class='col-sm-12']/p/b"
    value2 = "Anand"
    # semester Infra_Table_Report
    srDist = "//select[@class='ng-untouched ng-pristine ng-valid']/option"
    srcluster = "//select[@class='ng-pristine ng-valid ng-touched']/option"
    srblock = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]/option"
    sr_students = "students"
    sr_schools = "schools"

    # Semester

    SRD1 = "//*[@id='choose_dist']/option[2]"
    SRB1 = "//*[@id='choose_block']/option[2]"
    SRC1 = "//*[@id='choose_cluster']/option[2]"

    # CRC

    CRD1 = "//*[@id='dist']/option[2]"
    CRB1 = "//*[@id='block']/option[2]"
    CRC1 = "//*[@id='cluster']/option[2]"



    #student Attendance Infra_Table_Report
    sar_hyper_link = "state"
    sar_year = "year"
    sar_month = "month"
    sar_download = "download"

    sar_district ="choose_dist"
    sar_block ="choose_block"
    sar_cluster="choose_cluster"
    column_report ="clmnReport"
    completion ="cmplnErr"
    compl_download ="//button[contains(text(),'Download')]"
   #semester Infra_Table_Report
    sr_by_xpath = "//*[@id='sr']"
    sr_by_id = "sr"
    sr_block_btn= "blockbtn"
    sr_cluster_btn = "clusterbtn"
    sr_schools_btn = "clusterbtn"
    block_btn ="blockbtn"
    cluster_btn="clusterbtn"
    schoolbtn="schoolbtn"
    sr_district = "choose_dist"
    sr_block = "choose_block"
    sr_cluster = "choose_cluster"
    sr_dist_hyper = "//*[@id='block']/span[1]"
    sr_school_hyper = "//*[@id='school']/span[5]"
    sr_cluster_hyper = "//*[@id='cluster']/span[3]"

    #Dashboards
    telmetry_report ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav/div/mat-nav-list/div/mat-nav-list[7]/mat-list-item/div/mat-icon"
    attendance = "//*[@id='sideNav']/div/div[1]/div/div/mat-nav-list/div/mat-nav-list[6]/mat-list-item/div/mat-icon"
    semester_sel = "//*[@id='sideNav']/div/div[1]/div/div/mat-nav-list/div/mat-nav-list[4]/mat-list-item/div/mat-icon"
    crc_report = "//*[@id='crcReport']/div/div[1]"



    crc_sel2 ="//*[@id='select']/select/option[2]"
    crc_sel3 ="//*[@id='select']/select/option[3]"
    crc_sel4 ="//*[@id='select']/select/option[4]"
    crc_sel5 = "//*[@id='select']/select/option[5]"

    #admin console
    createuser_icon ="//*[@id='crtUsr']/img"
    changepassword ="chPass"
    logs_icon ="//*[@id='logs']/img"
    summary ="//*[@id='summary']/img"
    monitor= "//*[@id='moniter']/a/img"

    #views
    infra_location ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div/p"
    view_composite ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/p"
    view_udise ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[1]/div[1]/div[2]/div[3]/div/div/div[2]/div/p"
    view_compo="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/p"
    view_profile ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/p"
    view_location ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/p"
    view_content ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/p"
    view_crc ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/p"
    view_semester="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div/p"
    view_pat="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/div/p"
    view_exception="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[3]/div[2]/div[2]/div[1]/div/div/div[2]/div/p"
    view_completion ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/div/p"
    view_student ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[4]/div[1]/div[2]/div[1]/div/div/div[2]/div/p"
    view_teacher="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/div/p"
    view_telemetry="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-dashboard/div/div[1]/div[4]/div[2]/div[2]/div/div/div/div[2]/div/p"

    #Pat-heatchart
    district_dropdown="district"
    blocks_dropdown="block"
    cluster_dropdown="cluster"
    exam_dates ="examDate"
    view_by="viewBy"
    year_select ="year"
    grade ="grade"
    subjects ="subject"

    #LPD Reports
    timeperiods ="timePeriod"
    district_sel ="district"
    block_sel ="block"
    cluster_sel ="cluster"

    #Admin_Console
    create_user ="crtUsr"
    change_pass ="//a[@id='Chpass']"
    userlst = "//a[@id='user']"
    logfiles ="//a[@id='logs']"
    s3downloads ="//a[@id='downloads']"
    summarystat ="//a[@id='summary']"
    nifischedular="//a[@id='nifi']"
    #icons
    adduser ="addUser"
    chpass_icon ="//div[@id='chPass']"
    userprofiles ="//div[@id='user']"
    log_icon ="//div[@id='logs']"
    summary_icon ="//div[@id='summary']"
    s3files_icon ="s3dwn"
    nifi_Sch ="//div[@id='nifi']"

    #TPD Enrollement and Completion
    coursetype="choose_enroll"
    coll_names ="coll_name"

    # Health card report
    levels="level"
    submt ="button"

    search="myInput"
    itags="//div[@id='div3']/div/span"
    access_report="//p/a"
    access_infra ="//p[@id='infraLink']/a"
    access_student="//p[@id='attdLink']/a"
    access_semester="//p[@id='semLink']/a"
    access_pat="//p[@id='patLink']/a"
    access_crc="//p[@id='crcLink']/a"
    access_udise="//p[@id='udiseLink']/a"

    home_Std = "attdLink"
    home_sem = "semLLink"
    home_pat = "patLink"
    home_infra = "infraLink"
    home_udise = "udiseLink"
    home_crc = "crcLink"

    report_stdcard ="stdHealthCard"
    report_semcard="semHealthcard"
    report_crccard="crcHealthcard"
    report_infracard="infraHealthcard"
    report_patcard="patHealthcard"
    report_udisecard="udiseHealthcard"

    #districtwise health card
    District_name = ""
    # Blockwise
    Block_name = ""

    #clusterwise
    Cluster_name=""
    #Schoolwise
    School_name="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-health-card/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[14]/td[3]/strong"

    state_student="//*[@id='stdAttendance']/div[2]/div/table/tbody/tr/td"
    state_semester="//*[@id='semPer']/div[2]/div/table/tbody/tr/td"
    state_pat ="//*[@id='pat']/div[2]/div/table/tbody/tr/td"
    state_infra=""
    state_udise="//*[@id='udise']/div[2]/div/table/tbody/tr/td"
    state_crc="//*[@id='crc']/div[2]/div/table/tbody/tr/td"



