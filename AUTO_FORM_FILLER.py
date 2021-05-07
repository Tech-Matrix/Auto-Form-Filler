from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import time

from bs4 import BeautifulSoup
import requests

import pyautogui


def autoformfiller():
    print('\n')
    opts = Options()
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
    opts.add_argument('user-agent=' + user_agent)

    print('WELCOME TO THE AUTO-FORM-FILLER\n')



    link = input("Enter the Google form's link: ")

    print('\n')

    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')

    title = soup.find('title').text
    print('Title of the form: ', title.upper())

    print('\n')

    print('->These are the information to be filled: ')
    i = 1

    ques = []
    ans = []
    ques_numbers = []
    for question in soup.find_all('div',class_='freebirdFormviewerComponentsQuestionBaseTitle exportItemTitle freebirdCustomFont'):
        ques.append(question.text)
        print(i, ')', question.text.upper())
        i += 1

    print('\n')
    ques = list(enumerate(ques, 1))

    def p(l):
        m = []
        for i, j in l:
            m.append(str(str(i) + ':' + j))
        return '\n'.join(m)

    ques_ans = ques.copy()

    print('\n')

    while len(ques) > 0:
        ques_no = int(input('\nEnter the question number you want to fill (Enter 0 to SUBMIT the Form): '))
        print('\n')

        if ques_no == 0:
            web_chrome = webdriver.Chrome(options=opts)
            web_chrome.get(link)
            time.sleep(3)

            for numbers, ans_q in zip(ques_numbers, ans):
                x_path = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{numbers}]/div/div/div[2]/div/div[1]/div/div[1]/input'
                form1 = web_chrome.find_element_by_xpath(x_path)
                form1.send_keys(ans_q)

            time.sleep(3)



            form_submit = web_chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
            form_submit.click()

            web_chrome.close()

            print('\nTHANK YOU FOR USING THE AUTOFORM FILLER, YOUR FORM HAD BEEN SUCCESSFULLY SUBMITTED..!')

            pyautogui.hotkey('ctrl', 'c')




        else:
            ques_numbers.append(ques_no)
            for i in ques:
                if i[0] == ques_no:
                    m = i[1]

            print('Enter:', m.upper())
            answer = input()
            ans.append(answer)
            ques.pop(ques.index((ques_no, m)))
            if len(ques) > 0:
                print('\nQuestions left to fill:\n',p(ques))

    print('\n')
    user_sub = input('Do you wish to submit the form: \n1) YES\n2)NO\n')
    if user_sub == '1':
        web_chrome = webdriver.Chrome(options=opts)
        web_chrome.get(link)
        time.sleep(3)

        for numbers, ans_q in zip(ques_numbers, ans):
            x_path = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{numbers}]/div/div/div[2]/div/div[1]/div/div[1]/input'
            form1 = web_chrome.find_element_by_xpath(x_path)
            form1.send_keys(ans_q)

        time.sleep(3)

        form_submit = web_chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        form_submit.click()

        time.sleep(3)

        web_chrome.close()

        print('\nTHANK YOU FOR USING THE AUTOFORM FILLER, YOUR FORM HAD BEEN SUCCESSFULLY SUBMITTED..!')

    else:
        autoformfiller()

autoformfiller()

