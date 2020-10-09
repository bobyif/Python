           #LIBRARYS
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from letters import letters as ls
from pynput import keyboard
import msvcrt
import random
import time

i = 1

user_input = int(input("Write how much photos do you whant to download :"))
 

        #BROWSER
browser = webdriver.Chrome()

while i <= user_input:
        i+=1        

                #RANDOM FUNC  
        random_1 = random.randint(1,10000000)
        random_num_1 = random.randint(1,9)  
        random_num_2 = random.randint(1,9)  
        random_num_3 = random.randint(1,9)
        random_let_1 = random.choice(ls)        
        random_let_2 = random.choice(ls)
        random_let_3 = random.choice(ls)


                #SEARCH ENGINE
        search = ("https://prnt.sc/" + str(random_num_1) + random_let_1 + str(random_num_2) + random_let_2 + str(random_num_3) + random_let_3)
        browser.get(search)
        time.sleep(1)

                        #IMG SELECTER
        img = browser.find_element_by_xpath("/html/body/div[3]/div/div/img")    
        actions = ActionChains(browser)

                  #SCREEN SHOT
        browser.save_screenshot('light_shot' + str(random_1) + '.png')

                #EXIT()           
        if msvcrt.kbhit():
        	if ord(msvcrt.getch()) == 27:
                       browser.quit()
print(i)        