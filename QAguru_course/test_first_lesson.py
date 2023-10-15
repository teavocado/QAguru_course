from selene import browser, have, be
import yaml

# Открываем файл конфигурации
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

username = config["username"]
password = config["password"]


def test_successful_login():
    # GIVEN
    browser.open('https://demowebshop.tricentis.com/')
    browser.should(have.url("https://demowebshop.tricentis.com/"))

    # WHEN
    browser.element('.ico-login').click()

    # AND
    browser.element('#Email').type(username)
    browser.element('#Password').type(password)
    browser.element('.login-button').click()

    # THEN
    browser.element('.header .account').should(have.text(username))
    browser.element('.ico-logout').should(be.visible)
