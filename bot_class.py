from math import ceil
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random, time

class InstaBot:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        options = Options().add_argument("--headless")
        self.browser = webdriver.Chrome('chromedriver/chromedriver.exe', options=options)


    def login(self) -> None:
        try:
            print('[+] Входжу в акаунт {1}'.format(self.username))
            self.browser.get('https://www.instagram.com/')
            time.sleep(2)

            self.browser.find_element(By.NAME, 'username').send_keys(self.username)
            time.sleep(random.randrange(3))

            passw = self.browser.find_element(By.NAME, 'password').send_keys(self.password, Keys.ENTER)
            time.sleep(random.randrange(3))

            print('[+] Увійшов')

            time.sleep(12)

        except Exception as e:
            self.close_youreself()
            print('Problem in login')
            print(e)


    def make_list(self) -> set:
        try:
            print('[+] Створюю список з підписками аккаунту...')
            self.browser.get('https://www.instagram.com/{0}/'.format(self.username))
            time.sleep(2)

            count_of_scrolling_page = ceil(int(self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a/div/span[1]').text) / 12)

            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a[1]').click()
            time.sleep(2)

            followers_ul = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
            
            for _ in range(count_of_scrolling_page):
                self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_ul)
                time.sleep(2)
            
            tegs_a = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]').find_elements(By.TAG_NAME, 'a')
            
            
            my_sub = set([i.get_attribute('href') for i in tegs_a])
            print('[+] Завершено')
            


            print('[+] Створюю список з підписниками аккаунту...')
            self.browser.get('https://www.instagram.com/{0}/'.format(self.username))
            time.sleep(2)

            count_of_scrolling_page = ceil(int(self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div/span[1]').text) / 12)

            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a[1]').click()
            time.sleep(2)

            followers_ul = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
            
            for _ in range(count_of_scrolling_page):
                self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', followers_ul)
                time.sleep(2)
            
            tegs_a = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]').find_elements(By.TAG_NAME, 'a')
            
            
            my_followers = set([i.get_attribute('href') for i in tegs_a])
            print('[+] Завершено')

            return set(my_sub) - set(my_followers)

        except Exception as e:
            self.close_youreself()
            print('Problem in make_list')
            print(e)


    def unsubscribe(self, lst: list[str]) -> None:
        try:
            for i in lst:
                print('[+] Відписуюся від користувача {0}'.format(i.split('/')[-2]))
                self.browser.get(i)
                time.sleep(3)

                self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button/div[1]').click()
                time.sleep(3)

                self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]').click()
                print('[+] Відписано')
                time.sleep(3)

        except Exception as e:
            self.close_youreself()
            print('Problem in unsubscribe')
            print(e)
            

    def close_youreself(self) -> None:
        self.browser.close()
        self.browser.quit()
