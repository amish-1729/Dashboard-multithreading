## Using threading to generate random numbers on 6 threads at specific intervals

import threading
import time
import random
import lxml.html
from selenium import webdriver


class HTMLParser:
    def __init__(self, html_file):
        self.html_file = html_file
        self.html = lxml.html.parse(self.html_file)
        self.root = self.html.getroot()

    def get_element_by_id(self, id):
        return self.root.get_element_by_id(id)

    def changeElementText(self, id, text):
        element = self.get_element_by_id(id)
        element.text = text


driver = webdriver.Chrome()
driver.get("file:///home/rk/Documents/6thsem/PA/dashboard.html")
parser = HTMLParser("dashboard.html")

def display(number, displayID):
    parser.changeElementText("change", f"{str.upper(displayID)}  -> {str(number)}")
    parser.changeElementText(displayID, str(number))
    parser.html.write("dashboard.html")
    driver.refresh()

def generateRandomNumber(lb, ub, refreshRate, displayID):
    while True:
        display(random.randint(lb, ub), displayID)
        parser.changeElementText("change", "Sleeping for " + str(refreshRate) + " seconds")
        time.sleep(refreshRate)


if __name__ == "__main__":
    # Create 6 threads
    displayIDs = ["red", "orange", "yellow", "green", "cyan", "blue"]
    refershRates = [20, 15, 25, 10, 5, 30]
    lb, ub = 0, 10
    for i in range(0,len(displayIDs)):
        thread = threading.Thread(
            target=generateRandomNumber, args=(lb, ub, refershRates[i], displayIDs[i])
        )
        thread.start()
        lb += 10
        ub += 10
