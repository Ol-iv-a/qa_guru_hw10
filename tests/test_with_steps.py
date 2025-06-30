import allure
from selene import browser, by, have
from selene.support.shared.jquery_style import s


def test_with_steps():
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com/')

    with allure.step("Ищем репозиторий"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-qaguru')
        s('#query-builder-test').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-qaguru")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 2"):
        s('.ListView-module__ul--vMLEZ').should(have.text("#2"))


