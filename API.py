import flask
import selenium.common.exceptions
from flask import request, jsonify
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from Assets import *


def initiate_api():
    app = flask.Flask(__name__)
    @app.route('/', methods=['GET'])
    def landing_page():
        return '<h1> landing page</h1><p>Hello From MoTaRa</p>' \
               ' <a href="fromyasdl?query=">From Yasdl.com</a>' \
               '</br> <a href="/">From soft98.ir</a>' \
               '</br><a href="fromsarzamin?query=">From SarzaminDownload.com</a>'

    @app.route('/fromsarzamin', methods=['GET'])
    def urls_from_sarzamin():
        try:
            if 'query' in request.args and len(request.args['query']) > 0:
                try:
                    records = pickle.load(open(r'sarzamin.bin', 'br'))
                    if records is None:
                        records = dict()
                except:
                    records = {}
                query = str(request.args['query'])
                if not record_search(records, query):
                    options = ChromeOptions()
                    options.add_argument("--headless=new")
                    driver = webdriver.Chrome(options=options)

                    driver.get(
                        f'https://www.google.com/search?q={query}+site%3Asarzamindownload.com+pc&hl=fa&sxsrf=APwXEdcDaj7CFFgMkontroDnt0yvMRUR5A%3A1687356138385&ei=6gKTZK-WF4uOxc8Pm-i02AQ&ved=0ahUKEwivs_O5w9T_AhULR_EDHRs0DUsQ4dUDCA8&uact=5&oq=query+site%3Asarzamindownload.com+pc&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAVDxBljbGWCVHWgCcAB4AIAB7QGIAasJkgEFMC4zLjOYAQCgAQHAAQE&sclient=gws-wiz-serp')
                    # clicking on the most relevant result
                    driver.find_element(By.CLASS_NAME, "VuuXrf").click()
                    more_a = driver.find_elements(By.CLASS_NAME, "more-a")
                    if len(more_a) > 0:
                        more_a[0].click()
                    download_link_dict = common_procedure('sarzamin', query, driver.find_elements(By.TAG_NAME, 'a'))
                    for item in download_link_dict:
                        download_link_dict[item].append('0')
                    return download_link_dict
                else:
                    my_dict = record_search(records, query)
                    for item in my_dict:
                        my_dict[item].append('1')
                    return jsonify(my_dict)
            else:
                return 'No query specified'
        except:
            jsonify(dict())

    @app.route('/tosarzamin', methods=['PUT'])
    def to_sarzamin():
        if 'query' in request.form :
            try:
                records = pickle.load(open(r'sarzamin.bin', 'br'))
                if records is None:
                    records = dict()
            except:
                records = {}
            query = str(request.form['query'])

            options = ChromeOptions()
            options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
            driver.get(
                f'https://www.google.com/search?q={query}+site%3Asarzamindownload.com+pc&hl=fa&sxsrf=APwXEdcDaj7CFFgMkontroDnt0yvMRUR5A%3A1687356138385&ei=6gKTZK-WF4uOxc8Pm-i02AQ&ved=0ahUKEwivs_O5w9T_AhULR_EDHRs0DUsQ4dUDCA8&uact=5&oq=query+site%3Asarzamindownload.com+pc&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAVDxBljbGWCVHWgCcAB4AIAB7QGIAasJkgEFMC4zLjOYAQCgAQHAAQE&sclient=gws-wiz-serp')
            # clicking on the most relevant result
            driver.find_element(By.CLASS_NAME, "VuuXrf").click()
            more_a = driver.find_elements(By.CLASS_NAME, "more-a")
            if len(more_a) > 0:
                more_a[0].click()
            download_link_dict = common_procedure('sarzamin', query, driver.find_elements(By.TAG_NAME, 'a'))
        return 'All Good'


    @app.route('/fromyasdl', methods=['GET'])
    def urls_from_yasdl():
        try:
            if 'query' in request.args and len(request.args['query']) > 0:
                try:
                    records = pickle.load(open(r'yasdl.bin', 'br'))
                    if records is None:
                        records = dict()
                except :
                    records = {}

                query = str(request.args['query'])
                if not record_search(records, query):
                    options = ChromeOptions()
                    options.add_argument("--headless=new")
                    driver = webdriver.Chrome(options=options)

                    # getting some query and searching for it in yasdl
                    driver.get(f"https://www.yasdl.com/?s={query}")
                    more_a = driver.find_elements(By.CLASS_NAME, "read-more-link")
                    if len(more_a) > 0:
                        more_a[0].click()
                    download_link_dict = common_procedure('yasdl', query, driver.find_elements(By.TAG_NAME, 'a'))
                    for item in download_link_dict:
                        download_link_dict[item].append('0')
                    return jsonify(download_link_dict)
                else:
                    my_dict = record_search(records, query)
                    for item in my_dict:
                        my_dict[item].append('1')
                    return jsonify(my_dict)
            else:
                return 'No query specified'
        except:
            return jsonify(dict())




    @app.route('/toyasdl', methods=['PUT'])
    def to_yasdl():
        if 'query' in request.form :
            try:
                records = pickle.load(open(r'yasdl.bin', 'br'))
                if records is None:
                    records = dict()
            except:
                records = {}
            query = str(request.form['query'])

            options = ChromeOptions()
            options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
            # getting some query and searching for it in yasdl
            driver.get(f"https://www.yasdl.com/?s={query}")
            more_a = driver.find_elements(By.CLASS_NAME, "read-more-link")
            if len(more_a) > 0:
                more_a[0].click()
            download_link_dict = common_procedure('yasdl', query, driver.find_elements(By.TAG_NAME, 'a'))
        return 'All Good'





    app.run()


initiate_api()
