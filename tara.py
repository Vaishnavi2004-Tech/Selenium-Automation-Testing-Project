import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os
driver=webdriver.Chrome()
driver.maximize_window()
url="http://127.0.0.1:5000/register"
driver.get(url)
print("Page opened Successfully")
time.sleep(2)
username = driver.find_element(By.ID,"username").send_keys("VaishnaviTARA@2026123")
print("usename entered")
password = driver.find_element(By.ID,"password").send_keys("VaishnaviTARA@2026123")
print("password entered")
c_password = driver.find_element(By.ID,"confirm_password").send_keys("VaishnaviTARA@2026123")
print("password confirmed")
register = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div[2]/form/div[4]/button"))
)
register.click()
print("Registered Successfully")
time.sleep(5)
 
#login page  

# have to change the username if you are register with new username

lusername = driver.find_element(By.ID,"username").send_keys("VaishnaviTARA@2026123")
print("usename entered")
lpassword = driver.find_element(By.ID,"password").send_keys("VaishnaviTARA@2026123")
print("password entered")
login = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div[2]/form/div[3]/button"))
)
login.click()
print("Logged in Successfully")
time.sleep(2)

data_collection = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div/div/div[2]/div[2]/a[1]"))
)
data_collection.click()
print("Data Collection page opened")
time.sleep(2)

choose_file = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='fileInput']"))
)
choose_file.send_keys("D:\\SOURCE CODE\\CAN_HCRL_OTIDS_B.csv")
print("file choosed")
time.sleep(2)

upload_dataset = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='uploadForm']/button"))
)
upload_dataset.click()
print("dataset uploaded")
time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
print("srolled down")

label_encoding = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='labelEncodingBtn']"))
)
label_encoding.click()
print("label encoding button clicked")
time.sleep(2)

# Scroll down to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
print("srolled down")
# Scroll right by 500 pixels
driver.execute_script("window.scrollBy(500, 0);")
time.sleep(1)
print("srolled Right")
# Scroll left by 500 pixels
driver.execute_script("window.scrollBy(-500, 0);")
time.sleep(1)
print("Scroll left")

# First locate the element properly
data_splitting = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='dataSplittingBtn']"))
)

# Then scroll into view
driver.execute_script("arguments[0].scrollIntoView();", data_splitting)
time.sleep(2)

# Optionally click
data_splitting.click()
print("data splitting done")
time.sleep(2)

data_accuracy =WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='algorithmAccuracyBtn']"))
)
data_accuracy.click()
print("data accuracy calculated")
time.sleep(2)

Threat_visual = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='threatVisualizationBtn']"))
)
Threat_visual.click()
print("threat visualization opened")
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
print("srolled down")

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
print("scroll up")

privacy_assessment= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='navbarNav']/ul/li[4]/a"))
)
privacy_assessment.click()
print("privacy assessment opened")
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
print("srolled down")

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
print("scroll up")

attack_simulation = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='navbarNav']/ul/li[5]/a"))
)
attack_simulation.click()
print("Attack simulation done")
time.sleep(2)

spoofing = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div/div[2]/div[1]/div/button[1]"))
)
spoofing.click()
print("spoofing clicked")
time.sleep(2)

dos = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div/div[2]/div[1]/div/button[2]"))
)
dos.click()
print("dos clicked")
time.sleep(2)

fuzzing = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div/div[2]/div[1]/div/button[3]"))
)
fuzzing.click()
print("fuzzing clicked")
time.sleep(2)

replay = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div/div[2]/div[1]/div/button[4]"))
)
replay.click()
print("replay clicked")
time.sleep(2)

real_time = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='navbarNav']/ul/li[6]/a"))
)
real_time.click()
print("real time monitor started")
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
print("srolled down")

start_monitor = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='startMonitoringBtn']"))
)
start_monitor.click()
print("monitor started")

time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
print("srolled down")

stop_monitor = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='startMonitoringBtn']"))
)
stop_monitor.click()
print("monitor stopped")
time.sleep(2)

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
print("scroll up")

prediction = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='navbarNav']/ul/li[7]/a"))
)
print("prediction page opened")
prediction.click()

normal = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div/div[2]/div/div[1]/div/span[1]"))
)
normal.click()
print("Initially clicked the normal data")
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
print("srolled down")

detect = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='predictBtn']"))
)
detect.click()
print(" detection button clicked")
time.sleep(2)

new_prediction = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='newPredictionBtn']"))
)
new_prediction.click()
print(" new prediction button clicked")
time.sleep(2)

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
print("scroll up")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
print("srolled down")

extreme = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div/div[2]/div/div[1]/div/span[7]"))
)
extreme.click()
print("data changed to extrerme values")
time.sleep(2)

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
print("scroll up")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
print("srolled down")


back = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='actionButtons']/a"))
)
print("Back to exploration page")
back.click()
time.sleep(2)

logout = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='navbarNav']/ul/li/a"))
)
logout.click()
print("logged out successfully")
time.sleep(2)
