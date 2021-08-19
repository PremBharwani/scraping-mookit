from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from config import EMAIL,PASS,COURSE_CODE, LATEST_N
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import subprocess
import re
import csv


driver = webdriver.Chrome()
driver.get("https://hello.iitk.ac.in/index.php/user/login")
elem = driver.find_element_by_id("edit-name")
elem.clear()
elem.send_keys(EMAIL)
elem2 = driver.find_element_by_id("edit-pass")
elem2.clear()
elem2.send_keys(PASS)
submit_button_elem = driver.find_element_by_id("edit-submit")
submit_button_elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.implicitly_wait(20)
courses_button = driver.find_element_by_partial_link_text(COURSE_CODE)
courses_button.send_keys(Keys.RETURN)
go_button = driver.find_element_by_id('edit-access-course')
go_button.send_keys(Keys.RETURN)
soup = bs(driver.page_source,'html.parser')

# lecture_details_list = driver.find_elements_by_tag_name('')
# print(len(lecture_details_list))

file1 = open(r"tmp.txt","w+")

lines = (str(driver.page_source)).split('\n')
for line in lines:
    file1.write(line+"\n")

file1.close()

arg1 = 'Week\|unicodeBulletForList'
arg2 = 's/<span _ngcontent-c2="" class="unicodeBulletForList">•<\/span>//g'

data = subprocess.Popen(['grep','-w',arg1,'tmp.txt'], stdout = subprocess.PIPE)
output = str(data.communicate())
final_file = open(r'final_file.txt','w+')
lines=str(output.split("\n"))
# print(lines)
for line in lines:
    final_file.write(line)
final_file.close()


driver.close()



# Merging this here from temp.py

def lmao(str):
    str = re.sub('\s+',' ',str)
    str = re.sub('<span _ngcontent-c2="" class="unicodeBulletForList">•</span>','',str)
    concat_string=''
    lines=[]
    for i in range(len(str)):
        if(i<len(str)-2):
            if(str[i]=='\\'and str[i+1]=='\\' and str[i+2]=='n'):
                lines.append(concat_string)
                concat_string=''
                i+=3
            else:
                concat_string = concat_string + str[i]

    if(len(concat_string)>0):
        lines.append(concat_string)

    return lines

file = open("final_file.txt",'r+')
string_val = str(file.read())
# print(string_val.strip('\n'))

list = lmao(string_val)
print("****************************************************")
span_str = '\n <span _ngcontent-c2="" class="unicodeBulletForList">\\xe2\\x80\\xa2</span>'


lec_details_list = [] # Final list having lec name and week with it 
curr_week = 0



for item in list:
    if 'Week' in item :
        # remove the other stuff
        week_n=''
        for x in item:
            if x.isdigit():
                week_n += x
        curr_week = int(week_n)
    elif  'unicodeBulletForList' in item :
        lec_name = item[77:]
        lec_details_list.append((lec_name,curr_week))



csv_file_header = ['Lecture Name','Week', 'Link']

with open('lecture_results.csv','w',encoding="UTF8") as f:
    helper = csv.writer(f)
    helper.writerow(csv_file_header)
    
    ctr=0
    for i in reversed(lec_details_list):
        if ctr>=LATEST_N:
            break
        row_add = [i[0],i[1],'null']
        helper.writerow(row_add)
        ctr+=1

                
    
print("Done scraping, Stored the results at \'./lecture_results.csv\'")



# print(driver.page_source)
# driver.close()