from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# --- Configuration du driver ---
options = Options()
# options.add_argument("--headless")  # Décommente si tu veux l'exécuter sans affichage
service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# --- Lancer le site ---
driver.get("https://icp.administracionelectronica.gob.es/icpplustieb/index")