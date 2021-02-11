def scrapper(person):
    import main
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    import time
    driver = webdriver.Chrome('D:\Bobi\Bobi\librarys\chromedriver.exe')

    #open the webpage
    driver.get("http://www.instagram.com")
    #target username

    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept")]'))).click()
    #enter username and password
    username.clear()
    username.send_keys("bobyif.if@gmail.com")
    password.clear()
    password.send_keys("guccibagador222")

    #target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    #We are logged in!
    #nadle NOT NOW
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()


    #target the search input field
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))

    #search for the hashtag cat
    keyword = person
    searchbox.send_keys(keyword)

    # Wait for 5 seconds
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(2)
    #scroll down to scrape more images
    driver.execute_script("window.scrollTo(0, 16000);")
    time.sleep(3)

    images1 = driver.find_elements_by_tag_name('img')
    images1 = [image.get_attribute('src') for image in images1]
    print('Number of scraped images: ', len(images1))

    import os
    import wget

    path = os.getcwd()

    path
    counter = 0
    for image in images1:
        save_as = os.path.join(path, keyword + str(counter) + '.jpg')
        wget.download(image, save_as)
        counter += 1

    driver.quit()
