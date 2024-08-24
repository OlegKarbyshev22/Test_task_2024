import os
import time
from demoqa_page import SearchHelper


def test_demoqa_search(browser):
    demoqa_page = SearchHelper(browser)
    demoqa_page.go_to_site()
    demoqa_page.enter_first_name("Oleg")
    demoqa_page.enter_last_name("Karbyshev")
    demoqa_page.enter_email("legys22@gmail.com")
    demoqa_page.choose_gender('Male')
    demoqa_page.enter_mobile("8888888888")
    demoqa_page.choose_birthdate(month="April", year="2004", day="22")
    demoqa_page.enter_subjects("Maths")
    demoqa_page.choose_hobbies("Music")
    demoqa_page.add_image(os.getcwd() + "/image/cat.jpeg")
    demoqa_page.enter_address("Улица Пушкина, дом Колотушкина")
    demoqa_page.choose_state("Haryana")
    demoqa_page.choose_city("Karnal")
    demoqa_page.click_submit()
    time.sleep(5)