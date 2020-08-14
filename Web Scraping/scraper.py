from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

file = open('output.txt', 'a')
browser = webdriver.Chrome("chromedriver_linux64/chromedriver")


def monitor_info(link):
    browser.get(link)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    tables = soup.find_all("table")
    table = tables[0]
    tab_data = [
        [
            cell.text for cell in row.find_all(["th", "td"])
        ]
        for row in table.find_all("tr")
    ]
    data = []
    title = []
    for x in tab_data:
        data.append(x[1])
        title.append(x[0])

    dic = {}

    for i in range(0, len(title)):
        dic[title[i]] = data[i]
    
    return dic


links = []
data = []

specialPrices = []
regularPrices = []

# browser.save_screenshot('screenshot.png')

df = pd.DataFrame()

try:
    for i in range(1, 3, 1):
        browser.get(
            "https://www.ryanscomputers.com/grid/all-monitor-all-brand?page="+str(i)+"&limit=72")
        titles = browser.find_elements_by_class_name('product-box')
        for title in titles:

            # Grub Links 

            link = title.find_element_by_tag_name('a')
            link = link.get_attribute('href')
            links.append(link)

            # Special Price
            specialPrice = title.find_element_by_class_name("price").text
            specialPrice = specialPrice.replace(',', '')
            specialPrices.append(int(specialPrice))


            # Regular Price 

            regularPrice = title.find_element_by_class_name("old-price").text
            regularPrice = regularPrice.replace(',', '')
            regularPrices.append(int(regularPrice))


    for link in links:
        dic ={}
        dic = monitor_info(link)
        # print(dic)
        # print("--"*20)
        data.append(dic)
        # print(data)

    browser.quit()


    df = pd.DataFrame(data)
    df["Regular Price"] = regularPrices
    df["Special Price"] = specialPrices
    df.to_csv('monitors.csv', encoding='utf-8')
    


except Exception as e:
    print(e)
    browser.quit()
