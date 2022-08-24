import tkinter, subprocess
from tkinter import filedialog
import os, sys, pickle, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions

cwd = os.getcwd()

subprocess.Popen(
  [
    "start",
    "chrome",
    "--remote-debugging-port=8989",
    "--user-data-dir=" + cwd + "/chrome_profile",
  ],
  shell=True,
)
