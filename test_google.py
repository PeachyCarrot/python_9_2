from selene.support.shared import browser
from selene import be, have


def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search1():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ведьмак 3').press_enter()
    browser.element('[id="search"]').should(have.text('Ведьмак 3: Дикая Охота'))


def test_google_not_found():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('gПpfdsgdfsgапFGFHteqw').press_enter()
    browser.element('.card-section').should(have.text('По запросу gПpfdsgdfsgапFGFHteqw ничего не найдено.'))




