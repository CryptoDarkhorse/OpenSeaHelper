from ast import main
import tkinter, subprocess
from tkinter import filedialog
import os, sys, pickle, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions

cwd = os.getcwd()

###wait for methods
def wait_for(code):
  wait.until(
    ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, code))
  )

def wait_xpath(code):
  wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))

##chromeoptions
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(
  executable_path = cwd + "/chromedriver.exe",
  options = opt,
)
wait = WebDriverWait(driver, 60)

# login to opensea

main_page = driver.current_window_handle

for handle in driver.window_handles:
  driver.switch_to.window(handle)
  if handle != main_page:
    driver.close()

for token_id in range(124, 128):
  print("Listing", token_id)

  if token_id <= 125: price = "500" # pirates
  else: price = "100" # treasures

  driver.get("https://opensea.io/assets/matic/0x1af1fd1ffe6c551f2534fb2d897861863ae145c2/" + str(token_id) + "/sell")

  # select ducation
  wait_for("button[class='sc-1xf18x6-0 sc-glfma3-0 jAcrJS gGmNLC']")
  duration_button = driver.find_element_by_css_selector("button[class='sc-1xf18x6-0 sc-glfma3-0 jAcrJS gGmNLC']")
  duration_button.click()

  wait_for("input[placeholder='Select a date range']")
  duration_list = driver.find_element_by_css_selector("input[placeholder='Select a date range']")
  duration_list.click()

  wait_for("span[class='sc-1xf18x6-0 sc-1aqfqq9-0 sc-1idymv7-2 hyzwIu cSiicL']")
  all_items = driver.find_elements_by_css_selector("span[class='sc-1xf18x6-0 sc-1aqfqq9-0 sc-1idymv7-2 hyzwIu cSiicL']")

  duration_item = None
  for item in all_items:
    if item.text == "6 months":
      duration_item = item
  duration_item.click()

  # set price
  wait_for("input[placeholder='Amount']")
  amount = driver.find_element_by_css_selector("input[placeholder='Amount']")
  amount.send_keys(price)

  # select token
  wait_for("div[class='sc-3dr67n-0 kvNabs sc-1shssly-0 bBQLVJ']")
  token_selection = driver.find_element_by_css_selector("div[class='sc-3dr67n-0 kvNabs sc-1shssly-0 bBQLVJ']")
  token_selection.click()

  wait_for("span[class='sc-1xf18x6-0 sc-1aqfqq9-0 sc-1idymv7-2 hyzwIu cSiicL']")
  all_items = driver.find_elements_by_css_selector("span[class='sc-1xf18x6-0 sc-1aqfqq9-0 sc-1idymv7-2 hyzwIu cSiicL']")

  usdc_item = None
  for item in all_items:
    if item.text == "USDC":
      usdc_item = item

  # usdc_button = usdc_item.find_element_by_xpath("./../..")
  usdc_item.click()

  wait_for("button[class='sc-1xf18x6-0 sc-glfma3-0 hiIVBZ eqgvEc']")
  listing_button = driver.find_element_by_css_selector("button[class='sc-1xf18x6-0 sc-glfma3-0 hiIVBZ eqgvEc']")
  listing_button.click()

  # while len(driver.window_handles) == 1:
  #   time.sleep(0.1)

  # for handle in driver.window_handles:
  #   if handle != main_page:
  #     driver.switch_to.window(handle)

  # wait_for("button[data-testid='request-confirm-button']")
  # confirm_button = driver.find_element_by_css_selector("button[data-testid='request-confirm-button']")
  # confirm_button.click()

  # try :
  #   wait_for("input[name='password']")
  #   pwd_input = driver.find_element_by_css_selector("input[name='password']")
  #   pwd_input.send_keys("123qwe!@#QWE")


  #   wait_for("button[data-testid='unlock-wallet-button']")
  #   unlock_button = driver.find_element_by_css_selector("button[data-testid='unlock-wallet-button']")
  #   unlock_button.click()
  # except : 
  #   # already authorize
  #   pass

  # while len(driver.window_handles) > 1:
  #   time.sleep(0.1)

  # print("Wallet closed")

  while len(driver.window_handles) == 1:
    time.sleep(0.1)

  # print("Wallet reopened for sign opened")

  time.sleep(2)

  for handle in driver.window_handles:
    if handle != main_page:
      driver.switch_to.window(handle)

  wait_for("button[data-testid='sign-message']")
  sign_button = driver.find_element_by_css_selector("button[data-testid='sign-message']")
  sign_button.click()

  while len(driver.window_handles) > 1:
    time.sleep(0.1)

  # print("Wallet closed")
  driver.switch_to.window(main_page)
  print("done")

  # wait_for("a[class='sc-1pie21o-0 elyzfO sc-1xf18x6-0 sc-glfma3-0 jPlHEK eqgvEc']")
  # view_button = driver.find_element_by_css_selector("a[class='sc-1pie21o-0 elyzfO sc-1xf18x6-0 sc-glfma3-0 jPlHEK eqgvEc']")
  # view_button.click()

  # wait_for("button[class='sc-1xf18x6-0 sc-glfma3-0 ddExNg eqgvEc OrderManager--second-button']")
