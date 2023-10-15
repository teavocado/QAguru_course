from selene import browser, have
import pytest
import conftest

def test_negative_search(test_open_browser):
    browser.element('[name=q]').type('hdfbkdbvkqjsdbv').press_enter()
    browser.element('#botstuff p').should(have.text('По запросу hdfbkdbvkqjsdbv ничего не найдено.'))