from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

browser = webdriver.Chrome()
browser.get('')

User_id = '//*[@id="txtUserName"]'
pwd = '//*[@id="txtPassword"]'
user_id_c = browser.find_element_by_xpath(User_id)
user_id_c.send_keys('')
pwd_c = browser.find_element_by_xpath(pwd)
pwd_c.send_keys('')
#this is to get the captcha
a = input()
print (a)
captcha = browser.find_element_by_xpath('//*[@id="txtPayConfCaptcha"]')
captcha.send_keys(a)

browser.find_element_by_xpath('//*[@id="btnLogin"]').click() #submit 

time.sleep(1)

master = browser.find_element_by_css_selector('#Panel1 > nav > ul > li:nth-child(2) > a')

#sevika = browser.find_element_by_css_selector('#Panel1 > nav > ul > li:nth-child(3) > a')

Hover = ActionChains(browser).move_to_element(master)

Hover.perform()

browser.find_element_by_xpath('//*[@id="Panel1"]/nav/ul/li[2]/ul/li[1]/a').click()


select = Select(browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlBeat"]'))
select.select_by_visible_text('275181201')

#read the excel file

df = df = pd.read_excel('Test.xlsx',header=None)

for i in df.index:

	name_of_sevika = df.ix[i][0]
	Father_name = df.ix[i][1]
	address= df.ix[i][2]
	religion= df.ix[i][3]
	Qualification = df.ix[i][4]
	dob = str(df.ix[i][7])
	payscale = str(df.ix[i][8])
	experience = str(df.ix[i][9])
	phone = int(df.ix[i][6])
	relationship = df.ix[i][5]

	# Search b Sevika Name
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtSevikaName"]').send_keys(name_of_sevika)

	#click Search
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_search"]').click()

	time.sleep(1)
	#click modify 
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_GrdSevikaList"]/tbody/tr[2]/td[1]/a').click()
	time.sleep(1)

	#Father Name
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TxtMidName"]').clear()
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_TxtMidName"]').send_keys(Father_name)

	#Address
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtAddr"]').clear()
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtAddr"]').send_keys(address)
	time.sleep(1)
	#Religion
	#how to select one of the value in the Religion (Dropdown)
	select = Select(browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlReligion"]'))
	select.select_by_visible_text(religion)
	time.sleep(1)
	#Qualification
	select = Select(browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlEduID"]'))
	select.select_by_visible_text(Qualification)
	time.sleep(1)
	#relationship
	select = Select(browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlmaritstat"]'))
	select.select_by_visible_text(relationship)
	time.sleep(1)
	date = browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_DtDob_txtDate"]')

	browser.execute_script("arguments[0].setAttribute('value',arguments[1])",date,dob)
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtphone"]').send_keys(phone)

	#click nxt button
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_BtnNextTab1"]').click()

	time.sleep(1)

	select = Select(browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlPayscaleID"]'))
	select.select_by_visible_text(payscale)	

	#experience scale
	select = Select(browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlExperience"]'))
	select.select_by_visible_text(experience)

	#click next button 
	time.sleep(3)
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_BtnNextTab2"]').click()
	time.sleep(3)
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_BtnSubmit"]').click()
	time.sleep(6)
	browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnClodeMsg"]').click()
	time.sleep(3)
