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
options.add_argument('--window-size=2560,1440')
options.add_argument('--log-level=3')
options.add_argument('--ignore-certificate-errors')
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(executable_path=r"C:\Users\jbnf\driver\chromedriver.exe", chrome_options=options) # cuidado com a versão do chromedriver)

ingrids = [
'EPB PRD|https://10.83.101.58:8443/ingrid_bdgd',
'EBO PRD|https://10.83.101.59:8443/ingrid_bdgd',
'EMG PRD|https://10.83.101.60:8443/ingrid_bdgd_emg',
'ENF PRD|https://10.83.101.60:8443/ingrid_bdgd_enf',
'ESE PRD|https://10.83.101.61:8443/ingrid_bdgd',
'EMT PRD|https://10.83.101.62:8443/ingrid_bdgd',
'ETO PRD|http://10.83.102.99:8080/ingrid_bdgd',
'ESS PRD|https://10.83.101.64:8443/ingrid_bdgd',
'EMS PRD|http://10.83.103.105:8080/ingrid_bdgd',
'ERO PRD|https://10.83.101.234:8443/ingrid_bdgd',
'EAC PRD|https://10.83.101.238:8443/ingrid_bdgd',
'EMS HML|http://10.83.106.183:8080/ingrid_bdgd',
'EBO HML|http://10.83.106.18:8080/ingrid_bdgd'
]

for ingrid in ingrids:
    print("Acessando: ", ingrid)
    browser.get(string[8:len(string)])
    delay = 3 # seconds / tempo de espera dos elementos
    try:
        myElem1 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'id_usuario')))
        print("Pagina de Login aberta!")
    except TimeoutException:
        print ("Loading took too much time!")

    username = browser.find_element(By.ID, "id_usuario")
    password = browser.find_element(By.ID, "senha")

    username.send_keys("coord")
    password.send_keys("indra")

    try:
        myElem2 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "/html")))
        print("Pagina de Agendamentos aberta!")
    except TimeoutException:
        continue
        print ("Loading took too much time!")

    browser.find_element(By.XPATH, "/html/body/form/div/div[2]/div[4]/button").submit()

    try:
        myElem3 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[22]/div/div[1]/div/span[5]')))
        print("Ingrid aberto!")
    except TimeoutException:
        print ("Loading took too much time!")

    browser.find_element(By.XPATH, "/html/body/div[22]/div/div[1]/div/span[5]").click()

    try:
        myElem4 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#AgendarExtratorTableContainer > div > table")))
        print("Agendamentos abertos!")

        print("#######################################################")
        print("EMPRESA: ", string[0:7])
        print("SITE: ", string[8:len(string)])
        print("ÚLTIMO AGENDAMENTO: ")

        ## TODO, ADICIONAR NUMA TABELA (pandas)
        ## todo, guardar num json

        table = browser.find_element(By.CSS_SELECTOR, "#AgendarExtratorTableContainer > div > table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        for data in rows[1].find_elements(By.TAG_NAME, "td"):
            print(data.text)

        print("#######################################################")
    except TimeoutException:
        print ("Loading took too much time!")

browser.quit()
