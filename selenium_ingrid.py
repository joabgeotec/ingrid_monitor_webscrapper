from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
logger.setLevel(logging.CRITICAL)  # or any variant from ERROR, CRITICAL or NOTSET

options = Options()
options.add_argument('--log-level=3')
options.add_argument('--ignore-certificate-errors')
# options.headless = True
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(executable_path=r"C:\Users\jbnf\driver\chromedriver.exe", chrome_options=options) # cuidado com a versão do chromedriver)

browser.get('https://10.83.101.238:8443/ingrid_bdgd')

delay = 3 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'id_usuario')))
    print("Pagina de Login aberta!")
except TimeoutException:
    print ("Loading took too much time!")

username = browser.find_element(By.ID, "id_usuario")
password = browser.find_element(By.ID, "senha")

username.send_keys("coord")
password.send_keys("indra")

delay = 3 # seconds

browser.find_element(By.XPATH, "/html/body/form/div/div[2]/div[4]/button").submit()

delay = 3 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[22]/div/div[1]/div/span[5]')))
    print("Ingrid aberto!")
except TimeoutException:
    print ("Loading took too much time!")

browser.find_element(By.XPATH, "/html/body/div[22]/div/div[1]/div/span[5]").click()

delay = 3 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[2]')))
    print("Agendamentos abertos!")

    print("#######################################################")
    print("ÚLTIMO AGENDAMENTO:")

    ## TODO, ADICIONAR NUMA TABELA (pandas)
    ## todo, guardar num json
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[2]").text)
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[3]").text)
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[4]").text)
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[5]").text)
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[6]").text)
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[7]").text)
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[8]").text)
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[9]").text)
    # print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[11]").text)
    print(browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td[12]").text)
    print("#######################################################")
except TimeoutException:
    print ("Loading took too much time!")

browser.quit()
