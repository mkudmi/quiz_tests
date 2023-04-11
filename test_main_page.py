import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "file:///home/maxim/QUIZ%20SITE%20REPO/QUIZ%20v3/index.html"




@pytest.mark.regression
def test_guest_can_click_on_main_button(browser):
    browser.get(link)
    games_link = browser.find_element(By.CLASS_NAME, "btn")
    games_link.click()

@pytest.mark.regression
def test_nav_link_games(browser):
    browser.get(link)
    link_games = browser.find_element(By.CLASS_NAME, "nav__link:first-child")
    link_games.click()

@pytest.mark.xfail(reason="Не сделал поп-ап")
def test_nav_link_rules(browser):
    browser.get(link)
    link_rules = browser.find_element(By.CLASS_NAME, "nav__link:nth-child(2)")
    link_rules.click()

@pytest.mark.regression
def test_nav_link_contacts(browser):
    browser.get(link)

    link_contacts = browser.find_element(By.CLASS_NAME, "nav__link:last-child")
    link_contacts.click()

    section_locator = (By.ID, 'contacts')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(section_locator))

    section_element = browser.find_element(*section_locator)
    assert section_element.is_displayed()

@pytest.mark.regression
def test_show_popup_game_1(browser):
    browser.get(link)

    link_games = browser.find_element(By.CLASS_NAME, 'btn')
    link_games.click()

    section_locator = (By.CLASS_NAME, 'section__games')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(section_locator))

    section_element = browser.find_element(*section_locator)
    assert section_element.is_displayed

    popup_link = browser.find_element(By.ID, 'open__pop__up-reg')
    browser.execute_script("arguments[0].click();", popup_link)
    time.sleep(5)

    popup_locator = (By.CLASS_NAME, 'pop__up__body-reg')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(popup_locator))

    popup_element = browser.find_element(*popup_locator)
    assert popup_element.is_displayed

@pytest.mark.regression
def test_fill_first_form(browser):
    browser.get(link)

    popup_link = browser.find_element(By.ID, 'open__pop__up-reg')
    browser.execute_script("arguments[0].click();", popup_link)

    browser.find_element(By.NAME, 'team_name').send_keys('example')
    browser.find_element(By.NAME, 'cap_name').send_keys('example')
    browser.find_element(By.NAME, 'tel').send_keys('123123123')
    browser.find_element(By.NAME, 'quantity').send_keys('2')
    browser.find_element(By.NAME, 'promo').send_keys('example123')

    browser.find_element(By.ID, 'submit_first').click()

    wait = WebDriverWait(browser, 10)
    success_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(string(), 'Поздравлямба, вы в игре!')]")))
    assert success_element.is_displayed(), "Форма не была успешно отправлена"

@pytest.mark.regression
def test_back_to_top_button(browser):
    browser.get(link)
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    backtotop_btn = browser.find_element(By.ID, 'back_to_top')
    browser.execute_script("arguments[0].click();", backtotop_btn)
    
