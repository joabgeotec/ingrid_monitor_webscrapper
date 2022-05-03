from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
import time
start_time = time.time()
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
    browser.get(ingrid[8:len(ingrid)])
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
        print("EMPRESA: ", ingrid[0:7])
        print("SITE: ", ingrid[8:len(ingrid)])
        print("ÚLTIMO AGENDAMENTO: ")

        table = browser.find_element(By.CSS_SELECTOR, "#AgendarExtratorTableContainer > div > table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        for data in rows[1].find_elements(By.TAG_NAME, "td"):
            print(data.text)

        cel_button = len(rows[1].find_elements(By.TAG_NAME, "td")) - 1

        if rows[1].find_elements(By.TAG_NAME, "td")[cel_button].get_attribute('innerText') == "Ver erro":
            button = '/html/body/div[2]/div/div/div[2]/form/div[2]/div/div/div/table/tbody/tr[1]/td['+str(cel_button)+']/button'
            browser.find_elements(By.XPATH, button)[0].click()
            alerta = browser.find_element(By.CLASS_NAME, 'toast-message').text.replace('\n','').replace('Ocorreu um erro durante a extração.','')
            print(alerta)
        
        browser.find_element(By.XPATH, '//*[@id="editor-agendar-extrator"]/div[1]/a').click()

        browser.find_element(By.XPATH, '//*[@id="menu"]/span[6]/a').click()
        print("Monitor de Processo:")

        try:
            myElem4 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="LogProcessamentoTableContainer"]/div/table/tbody/tr[1]/td[1]')))
            
            monitor_cell = browser.find_element(By.XPATH, '//*[@id="LogProcessamentoTableContainer"]/div/table/tbody/tr[1]/td[1]')
            print(monitor_cell.text)
        except TimeoutException:
            print ("Loading took too much time!")



        ## TODO, ADICIONAR NUMA TABELA (pandas)
        ## todo, guardar num json/csv

        print("#######################################################")
    except TimeoutException:
        print ("Loading took too much time!")

print("--- %s seconds ---" % (time.time() - start_time))
browser.quit()