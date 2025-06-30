import allure
from selene import browser, by, have
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Задачи и репозитории")
@allure.story("Просмотр раздела 'Задачи'")
@allure.link("https://github.com/")
def test_decorator_steps():
    open_page()
    search_for_repository('eroshenkoam/allure-qaguru')
    go_to_repository('eroshenkoam/allure-qaguru')
    open_issues()
    should_see_issues_with_number('2')

@allure.step("Открываем главную страницу")
def open_page():
    browser.open('https://github.com/')

@allure.step("Ищем репозиторий")
def search_for_repository(repository):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repository)
    s('#query-builder-test').submit()

@allure.step("Переходим по ссылке репозитория")
def go_to_repository(repository):
    s(by.link_text(repository)).click()

@allure.step("Открываем таб Issues")
def open_issues():
    s("#issues-tab").click()

@allure.step("Проверяем наличие Issue с номером 2")
def should_see_issues_with_number(number):
    s('.ListView-module__ul--vMLEZ').should(have.text("#" + number))
