#!usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import webDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from selenium.common.exceptions import TimeoutException
import time 

import pandas as pd

import smtplib
from email.message import EmailMessage

import schedule

departure_flight_inputs={'Depature': "JFK", 'Arrival': "LAX", 
                         'Date': "May 20, 2023"}


return_flight_inputs={'Depature': "JFK", 'Arrival': "ORD", 
                      'Date': "Jun 21, 2023"}
def find_cheapest_flights(flight_info):
    PATH = 'path to the chrome browser is used here'
    driver =webdriver.chrome(excutable_path= PATH)

    leaving_from = flight_info['Depature']
    going_to = flight_info['Arrival']
    trip_date = flight_info['Date']


    #go to expedia
    driver.get("https://expedia.com")


    #click on Flights 
    flight_xpath = '//a[@aria-controls="wizard-flight-pwa"]'
    flight_element= WebDriverwait(driver, 5). untill(
        EC.presence_of_element_located((By.XPATH, flight_xpath))
    )
    flight_element.click()
    time.sleep(0.2)



    #click on one way. One way flight is prefferable to deal with 
    oneway_xpath = '//a[@aria-controls="wizard-flight-tab-oneway"]' 
    one_way_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.xPATH, oneway_xpath))
    )
    one_way_element.click()
    timw.sleep(0.2)


    #first part : Flying from, Flying to, Depature Date, Return Date

    #------------Complete leaving from portion--------------
    leaving_from_xpath = '//button[@aria-label="Leaving from"]'
    leaving_from_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, leaving_from_xpath))
    )
    leaving_from_element.clear
    leaving_from_element.click()
    time.sleep(1)
    leaving_from_element.send_keys(leaving_from)

    time.sleep(1) # this is required otherwise it will be too fast for the browser
    leaving_from_element.send_keys(keys.DOWN, Keys.RETURN)
    #---------------------complete leaving from portion-------------------


    #-----------------Complete going to portion---------
    

    


