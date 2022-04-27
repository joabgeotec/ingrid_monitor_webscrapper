import mechanize
from bs4 import BeautifulSoup
import urllib # pip install requests
import http.cookiejar # pip install cookiejar
## para build, instalar pyinstaller, depois rodar pyinstaller <script>.py

print("> Iniciando!")
cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_handle_robots(False) ## ignora robots.txt
br.set_cookiejar(cj)

print("> Abrindo Ingrid!")
br.open("http://10.155.2.18:8080/ingrid_bdgd/") # vai retornar um response_seek_wrapper mas é normal

br.select_form(nr=0)

br.form['id_usuario'] = 'coord'
br.form['senha'] = 'indra'
br.submit()  # vai retornar um response_seek_wrapper mas é normal
print("> Login efetuado com sucesso!")

soup = BeautifulSoup(br.response().read(), 'lxml') # pip install lxml
spans = soup.find_all('a', {'href': 'Monitor.jsp'})
print(spans[0])
