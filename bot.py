from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='chromedriver.exe')
from time import sleep
from password import password as p
username = "Enter Your Login ID"
class bot():
  links=[]
  def __init__(self):
    self.login(username)
    self.like_comment()
  
  def login(self,user1):
    self.driver=webdriver.Chrome()
    self.driver.get("https://www.instagram.com/")
    sleep(5)
    username = self.driver.find_element_by_xpath("//input[@name='username']")

    username.send_keys(user1)

    password=self.driver.find_element_by_xpath("//input[@name='password']")

    password.send_keys(p)

    submit = self.driver.find_element_by_xpath("//button[@type='submit']")

    submit.click()
    sleep(5)
    not_now_1=self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
    not_now_1.click()
    sleep(5)
    # <button class=" " tabindex="0">Not Now</button>
    # <button class="aOOlW   HoLwm " tabindex="0">Not Now</button>
    not_now_2=self.driver.find_element_by_xpath("//button[contains(@class, 'aOOlW') and contains(@class, 'HoLwm')]")
    not_now_2.click()
    sleep(5)

  def like_comment(self):
    search = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
    search.send_keys("#technology")
    sleep(5)
    search.send_keys(Keys.RETURN)
    search.send_keys(Keys.RETURN)
    sleep(5)

    links = self.driver.find_elements_by_tag_name('a')

    def condition(links):
      return '.com/p/' in links.get_attribute("href")

    valid_links = list(filter(condition,links))

    for i in range(5):
      link=valid_links[i].get_attribute("href")
      if link not in self.links:
        self.links.append(link)
    for link in self.links:
      self.driver.get(link)
      sleep(5)
      like=self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
      like.click()




def main():
  my_bot=bot()

if __name__=='__main__':
  main()

