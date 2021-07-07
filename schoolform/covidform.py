from selenium import webdriver
from tkinter import *
import time
import requests
from bs4 import BeautifulSoup


def AUTOFORM():
    user = enterusername.get()
    passw = enterpassword.get()

    driver=webdriver.Chrome('chromedriver.exe')
    driver.get("https://ci.isu.edu.tw/prev/prev_login.asp?lang=CH&st=ISU")

    time.sleep(1)
    username = driver.find_element_by_id("loginID")
    password = driver.find_element_by_id("passID")

    username.send_keys(user)
    password.send_keys(passw)

    isulogin = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[6]/div/button[2]")
    isulogin.click()

    time.sleep(2)

    #closebut = driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[1]/button")
    #closebut.click()

    #time.sleep(2)
    formurl = "https://ci.isu.edu.tw/prev/prev_fill.asp"
    driver.get(formurl)

    time.sleep(1)
    # 填表單

    ### (2021/6/23~2021/7/7)最近14天內出境史
    nothing_but1 = driver.find_element_by_xpath("//*[@id='emp_depart2']")
    driver.execute_script("arguments[0].click();",nothing_but1)
    #nothing_but1.click()

    ### (2021/6/23~2021/7/7)最近14天內是否出現以下症狀(複選)
    nothing_but2 = driver.find_element_by_xpath('//*[@id="emp_past14_10"]')
    driver.execute_script("arguments[0].click();",nothing_but2)

    ### 自6/6之後，您是否曾有「屏東縣枋山鄉」活動史或接觸史？
    nothing_but3 = driver.find_element_by_xpath('//*[@id="emp_warship7_flag2"]')
    driver.execute_script("arguments[0].click();",nothing_but3)

    ### (2021/6/23~2021/7/7)最近14天內是否有到醫院或社區快篩站施行「新冠肺炎快篩或PCR檢驗」？
    nothing_but4 = driver.find_element_by_xpath('//*[@id="emp_warship6_flag2"]')
    driver.execute_script("arguments[0].click();",nothing_but4)

    ### (2021/6/23~2021/7/7)最近14天內您是否收到政府機關開立之通知單(居家隔離通知書、健康聲明暨居家檢疫通知書、自主健康管理單)？
    nothing_but5 = driver.find_element_by_xpath('//*[@id="emp_home_qua2"]')
    driver.execute_script("arguments[0].click();",nothing_but5)

    ### (2021/6/23~2021/7/7)最近14天內您同住家人或親近友人是否收到政府機關開立通知單(居家隔離通知書、健康聲明暨居家檢疫通知書、自主健康管理單)？
    nothing_but6 = driver.find_element_by_xpath('//*[@id="emp_home_qua_ff2"]')
    driver.execute_script("arguments[0].click();",nothing_but6)

    ### (2021/6/23~2021/7/7)最近14天內，您是否曾與新冠肺炎確診病患有接觸？
    nothing_but7 = driver.find_element_by_xpath('//*[@id="emp_2019nCoV2"]')
    driver.execute_script("arguments[0].click();", nothing_but7)

    ### (2021/6/23~2021/7/7)最近14天內，您同住家人或親近友人是否有到醫院或社區快篩站施行「新冠肺炎快篩或PCR檢驗」？
    nothing_but8 = driver.find_element_by_xpath('//*[@id="emp_contact2"]')
    driver.execute_script("arguments[0].click();", nothing_but8)

    ### 中央流行疫情指揮中心公布確診個案之國內活動足跡如下所述，你是否於下列時間點出入下列地點？(確診個案足跡依據2021/07/07指揮中心及各縣市衛生局公布資料更新)
    nothing_but9 = driver.find_element_by_xpath('//*[@id="emp_warship3_flag2"]')
    driver.execute_script("arguments[0].click();", nothing_but9)

    time.sleep(2)
    submit = driver.find_element_by_xpath("//*[@id='submit_btn']")
    #submit.click()

def clear():
    root.destroy()

root = Tk()
w=Canvas(root,width=300,height=50)
w.pack()

enterusername = StringVar()
enterpassword = StringVar()

Aframe=Frame(root)
Aframe.pack(side=TOP)
Alabel=Label(Aframe, text='輸入學號:', font=("微軟正黑體",15))
Alabel.pack(side=TOP)
entry1=Entry(Aframe,textvariable=enterusername,font=(20))
entry1.pack(side=TOP)

Alabe2=Label(Aframe, text='輸入密碼:', font=("微軟正黑體",15))
Alabe2.pack(side=TOP)
entry2=Entry(Aframe,textvariable=enterpassword,font=(20), show='*')
entry2.pack(side=TOP)

searchButton=Button(Aframe,text='送出', command=AUTOFORM,font=(20))
searchButton.pack(side='right', pady=20)
w2=Canvas(root,width=300,height=40)
w2.pack()

searchButton=Button(Aframe,text='關閉', command=clear,font=(20))
searchButton.pack(side='left', pady=20)

root.mainloop()
