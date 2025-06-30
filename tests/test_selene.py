from selene import browser, by, have
from selene.support.shared.jquery_style import s


def test_selene():
    browser.open('https://github.com/')
    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-qaguru')
    s('#query-builder-test').submit()
    s(by.link_text("eroshenkoam/allure-qaguru")).click()
    s("#issues-tab").click()
    s('.ListView-module__ul--vMLEZ').should(have.text("#2"))


