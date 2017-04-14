from selenium import webdriver
import time

import xlwt
from tempfile import TemporaryFile

def login_to_facebook():
	login_with_facebook= b.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button')
	login_with_facebook.click()
	time.sleep(8)
	user_id = b.find_element_by_xpath('//*[@id="email"]')
	user_id.send_keys("")
	pwd = b.find_element_by_xpath('//*[@id="pass"]')
	pwd.send_keys("")
	log_in_button = b.find_element_by_xpath('//*[@id="loginbutton"]')
	log_in_button.click()
	time.sleep(8)


def write_data_to_excell():
	book = xlwt.Workbook()
	sheet1 = book.add_sheet('My Followers')
	sheet2 = book.add_sheet('Me Following')

	for i,e in enumerate(People_that_follow_me):
	    sheet1.write(i,0,e)


	for i,e in enumerate(people_whom_i_follow):
	    sheet2.write(i,0,e)

	name = "Insta.xls"
	book.save(name)
	book.save(TemporaryFile())


def scroll_the_dialog():
	dialog = b.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
	for i in range(30):

		b.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
		
		time.sleep(1)


def close_the_dialog():
	dialog = b.find_element_by_xpath('/html/body/div[2]/div/button')
	dialog.click()


b = webdriver.Firefox()
b.get('https://www.instagram.com/')
time.sleep(8)


def get_list_of_people():
	list_of_people = []
	for row in b.find_elements_by_css_selector('a._4zhc5.notranslate._j7lfh'):
		list_of_people.append(row.get_attribute("title"))
		print(row.get_attribute("title"))
	return list_of_people






login_to_facebook()

get_my_instagram_profile = b.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div/div/div[3]/div/div[3]/a')
get_my_instagram_profile.click()
time.sleep(15)


my_followers= b.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[2]/a')
my_followers.click()
time.sleep(5)



scroll_the_dialog()


People_that_follow_me = get_list_of_people()

#close the dialog
close_the_dialog()

me_following = b.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[3]/a')
me_following.click()
time.sleep(3)



scroll_the_dialog()


people_whom_i_follow = get_list_of_people()

#close the dialog
close_the_dialog()


b.quit()


write_data_to_excell()

