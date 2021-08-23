from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import pymongo
from pymongo import MongoClient

def pymongo():
    cluster = MongoClient("mongodb+srv://RohitSingh:f8.ApphSJBi$KKs@cluster0.ufq4p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["autoform"]
    collection = db["entries"]
# pymongo()
cluster = MongoClient("mongodb+srv://RohitSingh:f8.ApphSJBi$KKs@cluster0.ufq4p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["autoform"]
collection = db["entries"]


import time

from bs4 import BeautifulSoup
import requests

import pyautogui

opts = Options()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
opts.add_argument('user-agent=' + user_agent)

print('\nWELCOME TO THE AUTO-FORM-FILLER\n')

print('\n')

link = input("PLEASE ENTER THE LINK OF THE FORM: ")

source = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')

title = soup.find('title').text
print('Title of the form: ', title.upper())

print('\n')

print('->These are the information to be filled: ')

_id = 0
count = 0
write = 0
dict_mongo = {}

dict_mongo_check = {}

i = 1
dict_a = {}
ques = []
ques_numbers = []
ans = []
mcq_ans = []

for data in soup.find_all('div',class_='m2'):
    questions = data['data-params'].split(',')[1].strip('"')
    print(i,')',questions)
    ques.append(questions)
    mcq_ques_null = data['data-params'].split(',')[3]
    if mcq_ques_null == '2':
        a = data['data-params'].split(',')
        a.reverse()
        a2 = a[20:]
        a2.reverse()
        dict_a[i] = []
        for k in range(5, len(a2), 5):
            dict_a[i].append(a2[k].strip('["'))
    elif mcq_ques_null == '0':
        dict_a[i] = 'short'
    else:
        dict_a[i] = 'long'
    i += 1

ques_file = ques.copy()
dict2 = {}
dict2_index = 1
ids = []
for data in soup.find_all('div',class_='appsMaterialWizToggleRadiogroupEl exportToggleEl isDisabled'):
    ids.append(data['id'])

id_indexes = 0
id_i = 0
for num7,opts9 in dict_a.items():
    if type(opts9) == list:
        dict2[dict2_index] = []

        len_opts9 = len(opts9)
        tuple_index = 1
        while len_opts9 !=0:
            tuple_pair = [tuple_index,ids[id_indexes]]
            tuple_index+=1
            dict2[dict2_index].append(tuple(tuple_pair))
            id_indexes +=1
            len_opts9 -=1
        dict2_index += 1
    else:
        dict2[dict2_index] = 'x'
        dict2_index+=1


ques = list(enumerate(ques,1))

def p(l):
    m = []
    for i, j in l:
        m.append(str(str(i) + ':' + j))
    return '\n'.join(m)

ques_ans = ques.copy()

def add_db():
    global check1,dict_new,match_max,results_final,dict_new2,dict_not,dict_new,dict_new3,dict_not3,count_n
    check1 = collection.find_one({})
    dict_new = [(i, j) for i, j in list(dict_mongo.items()) if (i, j) in list(check1.items())]

    match_max = len(dict_new)
    results_final = collection.find({})

    for resu in results_final:

        dict_new2 = [(i, j) for i, j in list(dict_mongo.items()) if (i, j) in list(resu.items())]
        dict_not = [(i, j) for i, j in list(dict_mongo.items()) if (i, j) not in list(resu.items())]
        if len(dict_new2) > match_max:
            dict_new = dict_new2
            match_max = len(dict_new)

            dict_not = [(i, j) for i, j in list(dict_mongo.items()) if (i, j) not in list(resu.items())]
    
    dict_new3 = dict(dict_new)
    dict_not3 = dict(dict_not)
    count_n = len(dict_new)

def append_db():
    global dict_mongo,id_mongo,results_finale
    if count_n != count:
        id_mongo = 0
        results_finale = collection.find({})
        for aj in results_finale:
            id_mongo += 1
        dict_mongo = list(dict_mongo.items())
        dict_mongo.insert(0, ("_id", id_mongo))
        dict_mongo = dict(dict_mongo)

        collection.insert_one(dict_mongo)
    elif count_n == count and len(dict_not3) > 0:
        collection.update_one(dict_new3, {'$set': dict_not3})
    elif count_n == count and len(dict_not3) == 0:
        pass

def copy_file():
    global ques_file,ans,dict_a,file_name,file1

    for ques_c,ans_c in list(dict_a.items()):
        if ans_c==list:
            file1.write(ques_file[ques_c-1]+'\n')
            file1.write(ans_c[ans[ques_c-1]-1])
            file1.write('\n'+'\n')
        else:
            file1.write(ques_file[ques_c-1]+'\n')
            file1.write(str(ans[ques_c-1]))
            file1.write('\n'+'\n')

    file1.close()

while len(ques) > 0:
    ques_no = int(input('\nEnter the question number you want to fill (Enter 0 to SUBMIT the Form): '))
    print('\n')

    if ques_no == 0:

        write_file2 =   input("DO YOU WISH TO WRITE TO A FILE?\n1) YES\n2)NO\n")
        if write_file2=='1':
            file_name = input("WHAT SHOULD BE FILE NAME:")
            file1 = open(file_name, "w")
            copy_file()
        add_db()
        append_db()
        web_chrome = webdriver.Chrome(options=opts)
        web_chrome.get(link)
        time.sleep(3)

        for numbers, ans_q in list(zip(ques_numbers, ans)):
            if dict_a[numbers] == 'short':
                x_path = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{numbers}]/div/div/div[2]/div/div[1]/div/div[1]/input'
                form1 = web_chrome.find_element_by_xpath(x_path)
                form1.send_keys(ans_q)

            elif dict_a[numbers] == 'long':
                x_path = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{numbers}]/div/div/div[2]/div/div[1]/div[2]/textarea'
                form1 = web_chrome.find_element_by_xpath(x_path)
                form1.send_keys(ans_q)

            elif type(dict_a[numbers]) == list:
                answer_mcq = dict2[numbers][ans_q - 1][1]
                x_path = f'//*[@id="{answer_mcq}"]/div[3]/div'
                form1 = web_chrome.find_element_by_xpath(x_path)
                form1.click()

        time.sleep(5)

        form_submit = web_chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        form_submit.click()

        time.sleep(3)

        web_chrome.close()

        print('YOUR FORM HAVE BEEN SUBMITTED SUCCESSFULLY..\nTHANK YOU FOR USING AUTO-FORM-FILLER')

        pyautogui.hotkey('ctrl', 'c')



    else:
        ques_numbers.append(ques_no)
        for i2 in ques:
            if i2[0] == ques_no:
                m_ques = i2[1]
                m_num = i2[0]






        if type(dict_a[m_num]) == list:
            print('question: ', m_ques)
            i_opt = 1
            for options in dict_a[m_num]:

                print(i_opt,')',options)
                i_opt+=1

            answer = int(input())
            ans.append(answer)
            mcq_ans.append(answer)#
            ques.pop(ques.index((ques_no, m_ques)))

            if len(ques) > 0:
                print('\nQuestions left to fill:\n', p(ques))

        else:
            print('question: ', m_ques.upper())
            n_bool = 0
            results = collection.find(dict_mongo_check)
            flag = 1

            for re in results:
                if flag==0:
                    break
                # m_question = m_ques.strip(' ')
                for cat,op in list(re.items()):
                # if bool(m_ques.lower() in re) == True:
                    pos = 0
                    if cat.lower()==m_ques.lower():

                        pos = 1
                        flag = 0
                        count+=1
                        write = re[m_ques.lower()]
                        pyautogui.write(write.upper())
                        break

            answer = input()

            result_2 = collection.find({m_ques.lower():answer.lower()})
            num100 = len(list(result_2))
            if answer.lower() != write and pos==1 and num100==0:
                count=-1
            if answer.lower()==write and pos==1 and num100>0:
                dict_mongo_check[m_ques.lower()] = answer.lower()
            if answer.lower()!=write and pos==1 and num100>0:
                dict_mongo_check[m_ques.lower()] = answer.lower()
            dict_mongo[m_ques.lower()] = answer.lower()
            ans.append(answer)
            ques.pop(ques.index((ques_no, m_ques)))

            if len(ques) > 0:
                print('\nQuestions left to fill:\n', p(ques))

print('\n')


add_db()


user_sub = input('All questions have been filled...\nDo you wish to submit the form: \n1) YES\n2)NO\n')
if user_sub == '1':

    write_to_file = input("DO YOU WISH TO WRITE TO A FILE?\n1) YES\n2)NO\n")
    if write_to_file == '1':
        file_name = input("WHAT SHOULD BE FILE NAME:")
        file1 = open(file_name, "w")
        copy_file()
    append_db()

    web_chrome = webdriver.Chrome(options=opts)
    web_chrome.get(link)
    time.sleep(3)

    for numbers, ans_q in list(zip(ques_numbers,ans)):
        if dict_a[numbers] == 'short':
            x_path = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{numbers}]/div/div/div[2]/div/div[1]/div/div[1]/input'
            form1 = web_chrome.find_element_by_xpath(x_path)
            form1.send_keys(ans_q)

        elif dict_a[numbers] == 'long':
            x_path = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{numbers}]/div/div/div[2]/div/div[1]/div[2]/textarea'
            form1 = web_chrome.find_element_by_xpath(x_path)
            form1.send_keys(ans_q)

        elif type(dict_a[numbers]) == list:
            answer_mcq = dict2[numbers][ans_q-1][1]
            x_path = f'//*[@id="{answer_mcq}"]/div[3]/div'
            form1 = web_chrome.find_element_by_xpath(x_path)
            form1.click()

    time.sleep(5)

    form_submit = web_chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    form_submit.click()

    time.sleep(3)

    web_chrome.close()

    print('YOUR FORM HAVE BEEN SUBMITTED SUCCESSFULLY..\nTHANK YOU FOR USING AUTO-FORM-FILLER')

















