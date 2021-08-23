# Auto-Form-Filler
The use of automation and automated processes are consistently increasing, and in next 10-15 years, adoption of automation linked with other technologies like AI will transform the workplace and will increase higher productivity, GDP  growth, improved corporate performance, reduced factory lead times.

AUTO FORM FILLER which is made using python, is a small initiative, a project that aims to automate the form filling process and all it requires is the link of the form. 


# Interface 
The current interface of the form filler is, when the user enters the link of the form, it gets all the questions present in form and shows it to the user.
The user can choose how many questions or which questions to fill and the form can be submitted anytime on the user's command. The form works with a database which has all the information and entries previously filled by the users, stores their data in a user specific format and as a result optimises the user's experience while filling the form by automatically filling the answers of repititive questions.

# Working of the AUTO FORM FILLER
The form filler currently works with 3 python libraries :
1) selenium: it automates the web-browser, the filling of answers to the respective questions and submission of the form.
2) requests: it gets the complete contents and information of the site(form in this case).
3) BeautifulSoup: used for scraping the website and acquring the contents of the form.
4) MongoDB: used for storing the entries in a user specific format and automatically filling the repititive questions.
5)In some cases, few websites and webbrowsers restrict the working and access to the selenium automation bot hence the user agent of the form filler has also been changed to prevent any restrictions.
5)Also provides the user an option to save the answers of the form.

# Libraries to install for the working
1) pip install requests
2) pip install beautifulsoup4
3) before installing selenium make sure you have chocolatey(used for working of chromedriver) installed, then install selenium: pip install selenium
4) pip install pymongo

# Contribute to make it better..!
Auto form filler is still in development phase and all your contributions are warmly welcomed.
Few contribution suggestions are as follows:
1)An improved gui interface.
2)Currently the form filler works with short answer, long answer and MCQ type questions but is aimed to function beyond any such restrictions.
3)A better algorithm for web scraping and filling of answers.
