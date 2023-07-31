import flask
import selenium.common.exceptions
from flask import request, jsonify
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium import webdriver
import re
import subprocess
def is_for_windows_sarzamin(link:str) -> bool:
    link = link.split('?')[0]
    return link.endswith('.exe') or link.endswith('.zip') or link.endswith('rar')

def extractEnglish_sarzmain(myStr: str) -> str:
    enStr = ''
    for char in myStr:
        if 0 <= ord(char) < 256:
            enStr += char
    enStr = enStr.split('-')[0]
    enStr = enStr.strip()
    if enStr != '32' and enStr != '64':
        enStr = 'Dont care'
    return enStr

def extractEnglish(myStr: str) -> str:
    enStr = ''
    for char in myStr:
        if 0 <= ord(char) < 256:
            enStr += char
    return enStr


def extractEnglish_soft(myStr: str) -> str:
    enStr = ''
    for char in myStr:
        if 0 <= ord(char) < 256:
            enStr += char
    myList = enStr.split()
    filter(lambda x: True if x.isalnum() else False, myList)
    return list(filter(lambda x: True if x.isalnum() else False, myList))[0]


def initiate_api():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/', methods=['GET'])
    def landing_page():
        return '<h1> landing page</h1><p>Hello From MoTaRa</p> <a href="fromyasdl?query=">From Yasdl.com</a> <a href="fromsoft98?query=">From soft98.ir</a>' \
               '<a href="fromsarzamin?query=">From SarzaminDownload.com</a>'

    @app.route('/fromsarzamin', methods=['GET'])
    def urls_from_sarzamin():
        try:
            if 'query' in request.args and len(request.args['query']) > 0:
                options = ChromeOptions()
                options.add_argument("--headless=new")
                driver = webdriver.Chrome(options=options)
                query = str(request.args['query'])
                driver.get(
                    f'https://www.google.com/search?q={query}+site%3Asarzamindownload.com+pc&hl=fa&sxsrf=APwXEdcDaj7CFFgMkontroDnt0yvMRUR5A%3A1687356138385&ei=6gKTZK-WF4uOxc8Pm-i02AQ&ved=0ahUKEwivs_O5w9T_AhULR_EDHRs0DUsQ4dUDCA8&uact=5&oq=query+site%3Asarzamindownload.com+pc&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAVDxBljbGWCVHWgCcAB4AIAB7QGIAasJkgEFMC4zLjOYAQCgAQHAAQE&sclient=gws-wiz-serp')
                # clicking on the most relevant result
                driver.find_element(By.CLASS_NAME, "VuuXrf").click()
                more_a = driver.find_elements(By.CLASS_NAME, "more-a")
                if len(more_a) > 0:
                    more_a[0].click()
                # download_links_div = driver.find_elements(By.CLASS_NAME, "download-links")
                # if len(download_links_div) == 0:
                #     dl_box = driver.find_element(By.CLASS_NAME, "OpenTable2")
                # else:
                #     dl_box = download_links_div[0]
                anchor_tags = driver.find_elements(By.TAG_NAME, 'a')
                anchor_tags = list(filter(lambda x: x.get_attribute('href') != '', anchor_tags))
                anchor_tags = list(filter(lambda x: x.get_attribute('href') is not None, anchor_tags))
                anchor_tags = list(filter(lambda x:is_for_windows_sarzamin(x.get_attribute('href')), anchor_tags))


                download_link_hrefs = list(map(lambda x: x.get_attribute('href'), anchor_tags))
                download_link_texts = list(map(lambda x: extractEnglish_sarzmain(x.text), anchor_tags))
                download_link_dict = dict(zip(download_link_texts, download_link_hrefs))
                return jsonify(download_link_dict)
            else:
                return 'No query specified'
        except:
            return jsonify(dict())


    @app.route('/fromsoft98', methods=['GET'])
    def urls_from_soft98():
        try:
            if 'query' in request.args and len(request.args['query']) > 0:

                options = ChromeOptions()
                # options.add_argument("--headless=new")

                driver = webdriver.Chrome(options=options)

                # getting some query and searching for it in google
                query = str(request.args['query'])
                driver.get(
                    f'https://www.google.com/search?q=%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF+{query}+%D8%A8%D8%B1%D8%A7%DB%8C+%D9%88%DB%8C%D9%86%D8%AF%D9%88%D8%B2+soft98')
                names = driver.find_elements(By.CLASS_NAME, "VuuXrf")
                # clicking on the most relevant result
                names[0].click()
                # getting soft98 download box
                dl_boxes = driver.find_element(By.ID, 'dtill')
                if dl_boxes is not None:
                    dl_boxes = dl_boxes[0]
                    # getting all soft98 download anchor tags
                    dl_buttons = dl_boxes.find_elements(By.XPATH, '*')
                    # getting download for Windows section
                    # starting_link_index = 0
                    # for i in range(len(dl_buttons)):
                    #     if len(dl_buttons[i].find_elements(By.TAG_NAME, 'span')) > 0:
                    #         if dl_buttons[i].find_elements(By.TAG_NAME, 'span')[0].text == 'نسخه Windows':
                    #             starting_link_index = i
                    #
                    # last_link_index = 0
                    # for i in range(starting_link_index + 1, len(dl_buttons)):
                    #     if dl_buttons[i].tag_name == 'dt':
                    #         last_link_index = i
                    #         break
                    last_link_index = 0
                    for i in range(len(dl_buttons)):
                        if dl_buttons[i].get_attribute('class') == '':
                            last_link_index = i
                            break

                    wanted_dl_buttons = dl_buttons[:last_link_index]

                    wanted_dl_buttons = filter(lambda x: True if x.tag_name == 'dd' else False, wanted_dl_buttons)
                    download_link_hrefs = map(lambda x: x.find_element(By.TAG_NAME, 'a').get_attribute('href'),
                                              wanted_dl_buttons)
                    download_link_texts = map(lambda x: extractEnglish_soft(x.find_element(By.TAG_NAME, 'a').text),
                                              wanted_dl_buttons)
                    download_link_dict = dict(zip(download_link_texts, download_link_hrefs))
                    return jsonify(download_link_dict)
                else:
                    return jsonify(dict())
            else:
                return 'no query specified'
        except selenium.common.exceptions.SeleniumManagerException:
            return '<h1 style="background-color:red;">No Internet Connection</h1>'

    app.run()

initiate_api()




# def contains(string: str, pattern: str) -> bool:
#     pattern = r".zip\.$"
#     return bool(re.search(pattern, string))
# def isForWindows(link:str) -> bool:
#     link = link.split('?')[0]
#     return link.endswith('.rar') or link.endswith('.zip') or link.endswith('.exe')
# print(isForWindows("https://dl2.soft98.ir/mobile/Zapya.2.8.0.3-Full.exe?1687174720"))
#
#
#
#
