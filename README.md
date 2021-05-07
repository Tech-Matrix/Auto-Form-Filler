# Auto-Form-Filler
The use of automation and automated processes are consistently increasing, and in next 10-15 years, adoption of automation linked with other technologies like AI will transform the workplace and will increase higher productivity, GDP  growth, improved corporate performance, reduced factory lead times.

AUTO FORM FILLER which is made using python, is a small initiative, a project that aims to automate the form filling process and all it requires is the link of the form. 


# Interface 
The current interface of the form filler is, when the user enters the link of the form, it gets all the questions present in form and shows it to the use.
Th user can choose how many questions or which questions to fill and the form can be submitted anytime on the user's command.

# Working of the AUTO FORM FILLER
The form filler currently works with 3 python libraries :
1) selenium: it automates the web-browser, the filling of answers to the respective questions and submission of the form.
2) requests: it gets the complete contents and information of the site(form in this case).
3) BeautifulSoup: used for scraping the website and acquring the contents of the form.

4)In some cases, few websites and webbrowsers restrict the working and access to the selenium automation bot hence the user agent of the form filler has also been changed to prevent any restrictions.

# Libraries to install for the working
1) pip install requests
2) pip install beautifulsoup4
3) before installing selenium make sure you have chocolatey(used for working of chromedriver) installed, then install selenium: pip install selenium

# Contribute to make it better..!
Auto form filler is still in development phase and all your contributions are warmly welcomed.
Few contribution suggestions are as follows:
1)An improved gui interface.
2)Improvements for form filler to work for any kind of form containing any sort of questions.(currently works only for short answer type questions).
3)A better algorithm for web scraping and filling of answers.
