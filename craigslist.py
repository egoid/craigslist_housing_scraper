import csv
import time
import os
import sys
import re
import json
from selenium import webdriver


def automate():

  bedroom_pattern = re.compile('(\d)br -')
  price_pattern = re.compile('[$](\d+)')

  chromedriver = "/Users/ta/desktop/yobs/scraper_backup/chromedriver"
  os.environ["webdriver.chrome.driver"] = chromedriver
  driver = webdriver.Chrome(chromedriver)
  driver.get("https://sfbay.craigslist.org/search/apa?search_distance=0&postal=94117&availabilityMode=0&housing_type=6")
  driver.set_window_size(1600, 1400)

  # driver.find_element_by_css_selector('a[class=\"apa\"]').click()

  results = {}

  with open('bayarea.csv' , 'rb') as f:
    reader = csv.reader(f)
    next(reader , None )
    for row in reader:
      results[row[0]] = {}
      results[row[0]]['data'] = []
      results[row[0]]['total_count'] = 0

  with open('bayarea.csv' , 'rb') as f:
    reader = csv.reader(f)
    next(reader , None )

    for row in reader:
      try:
        driver.find_element_by_css_selector('input[class=\"flatinput searchInput postal\"]').clear()
      except:
        time.sleep(1)
        driver.find_element_by_css_selector('input[class=\"flatinput searchInput postal\"]').clear()
      try:
        driver.find_element_by_css_selector('input[class=\"flatinput searchInput postal\"]').send_keys(row[1])
      except:
        driver.find_element_by_css_selector('input[class=\"flatinput searchInput postal changed_input\"]').send_keys(row[1])

      try:
        driver.find_element_by_css_selector('button[class=\"searchlink linklike changed_input clickme\"]').click()
      except:
        time.sleep(1)
        driver.find_element_by_css_selector('button[class=\"searchlink linklike changed_input clickme\"]').click()

      try:
        total_count = driver.find_element_by_xpath('//*[@class="totalcount"]').text

        print(row[0] + " : " + total_count + " results found")
        results[row[0]]['zipcode'] = row[1]
        results[row[0]]['total_count'] = results[row[0]]['total_count'] + int(total_count)


        page_results=[];  
        page_results = driver.find_elements_by_class_name("result-info");
        for entry in page_results:
          for bed_match in re.findall(bedroom_pattern, entry.text):
            if (bed_match):
              for price_match in re.findall(price_pattern, entry.text):
                if (price_match):
                  result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                  results[row[0]]['data'].append(result)
        if int(total_count) > 120:
          print("Over 120 Results - Paginating")
          driver.find_element_by_css_selector('a[class=\"button next\"]').click()
          page_results = driver.find_elements_by_class_name("result-info");
          for entry in page_results:
            for bed_match in re.findall(bedroom_pattern, entry.text):
              if (bed_match):
                for price_match in re.findall(price_pattern, entry.text):
                  if (price_match):
                    result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                    results[row[0]]['data'].append(result)
        if int(total_count) > 240:
          print("Over 240 Results - Paginating #2")
          driver.find_element_by_css_selector('a[class=\"button next\"]').click()
          page_results = driver.find_elements_by_class_name("result-info");
          for entry in page_results:
            for bed_match in re.findall(bedroom_pattern, entry.text):
              if (bed_match):
                for price_match in re.findall(price_pattern, entry.text):
                  if (price_match):
                    result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                    results[row[0]]['data'].append(result)
        if int(total_count) > 360:
          print("Over 360 Results - Paginating #3")
          driver.find_element_by_css_selector('a[class=\"button next\"]').click()
          page_results = driver.find_elements_by_class_name("result-info");
          for entry in page_results:
            for bed_match in re.findall(bedroom_pattern, entry.text):
              if (bed_match):
                for price_match in re.findall(price_pattern, entry.text):
                  if (price_match):
                    result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                    results[row[0]]['data'].append(result)
        if int(total_count) > 480:
          print("Over 480 Results - Paginating #4")
          driver.find_element_by_css_selector('a[class=\"button next\"]').click()
          page_results = driver.find_elements_by_class_name("result-info");
          for entry in page_results:
            for bed_match in re.findall(bedroom_pattern, entry.text):
              if (bed_match):
                for price_match in re.findall(price_pattern, entry.text):
                  if (price_match):
                    result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                    results[row[0]]['data'].append(result)
        if int(total_count) > 600:
          print("Over 600 Results - Paginating #5")
          driver.find_element_by_css_selector('a[class=\"button next\"]').click()
          page_results = driver.find_elements_by_class_name("result-info");
          for entry in page_results:
            for bed_match in re.findall(bedroom_pattern, entry.text):
              if (bed_match):
                for price_match in re.findall(price_pattern, entry.text):
                  if (price_match):
                    result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                    results[row[0]]['data'].append(result)
        if int(total_count) > 720:
          print("Over 720 Results - Paginating #6")
          driver.find_element_by_css_selector('a[class=\"button next\"]').click()
          page_results = driver.find_elements_by_class_name("result-info");
          for entry in page_results:
            for bed_match in re.findall(bedroom_pattern, entry.text):
              if (bed_match):
                for price_match in re.findall(price_pattern, entry.text):
                  if (price_match):
                    result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                    results[row[0]]['data'].append(result)
        if int(total_count) > 840:
          print("Over 840 Results - Paginating #7")
          driver.find_element_by_css_selector('a[class=\"button next\"]').click()
          page_results = driver.find_elements_by_class_name("result-info");
          for entry in page_results:
            for bed_match in re.findall(bedroom_pattern, entry.text):
              if (bed_match):
                for price_match in re.findall(price_pattern, entry.text):
                  if (price_match):
                    result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                    results[row[0]]['data'].append(result)
        if int(total_count) > 960:
          print("Over 960 Results - Paginating #8")
          driver.find_element_by_css_selector('a[class=\"button next\"]').click()
          page_results = driver.find_elements_by_class_name("result-info");
          for entry in page_results:
            for bed_match in re.findall(bedroom_pattern, entry.text):
              if (bed_match):
                for price_match in re.findall(price_pattern, entry.text):
                  if (price_match):
                    result = "$" + price_match + " , " + bed_match + "br , " + row[1]
                    results[row[0]]['data'].append(result)
        with open('house.txt' , 'w') as outfile:
          json.dump(results , outfile)
      except:
        print("No results for " + row[1])


  driver.close()

  return "Complete"

if __name__ == "__main__":
  automate()

