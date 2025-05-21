from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# --- Configuration du driver ---
options = Options()
# options.add_argument("--headless")  # Optionnel, pour exécuter sans fenêtre
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36")
service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# --- Charger le site cible ---
driver.get("https://icp.administracionelectronica.gob.es/icpplustieb/index")

# --- Supprimer cookies + localStorage + sessionStorage ---
driver.delete_all_cookies()
driver.execute_script("window.localStorage.clear();")
driver.execute_script("window.sessionStorage.clear();")

# --- Lancer le site ---
# driver.get("https://icp.administracionelectronica.gob.es/icpplustieb/index")
wait = WebDriverWait(driver, 1000000000)

select_element = wait.until(EC.presence_of_element_located((
    By.XPATH, '/html/body/div[1]/div/main/div/div/section/div[2]/form/div[1]/select'
)))
select_element.click()
select = Select(select_element)
select.select_by_visible_text("Barcelona")

button = wait.until(EC.element_to_be_clickable((
    By.XPATH, '/html/body/div[1]/div/main/div/div/section/div[2]/form/div[3]/input[1]'
)))
button.click()


select_element = wait.until(EC.presence_of_element_located((
    By.XPATH, '/html/body/div[1]/div[2]/main/div/div/section/div[2]/form[1]/div[3]/div[1]/div[2]/div/fieldset/div[1]/select'
)))
select_element.click()

# select_element = wait.until(EC.presence_of_element_located((
#     By.ID, 'tramiteGrupo[0]"]/option[1]'
# )))
# select = Select(select_element)
# select.select_by_visible_text("POLICIA-CERTIFICADO DE REGISTRO DE CIUDADANO DE LA U.E.")

# driver.find_element(By.ID, "btnAceptar").click()


# <option value="-1" selected="selected">Despliega para ver trámites disponibles en esta provincia</option>
# //*[@id="tramiteGrupo[0]"]/option[1]