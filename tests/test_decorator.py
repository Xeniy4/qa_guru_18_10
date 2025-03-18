import allure
from selene import have
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_decorator():
    open_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("95")


@allure.step('Открываем главную страницу')
def open_page():
    browser.config.window_width = 1900
    browser.config.window_height = 1080
    browser.open("https://github.com")


@allure.step('Поиск нужного репозитория {repo}')
def search_for_repository(repo):
    s(".header-search-button.flex-1").click()
    s("#query-builder-test").type(repo)
    s("#query-builder-test").submit()


@allure.step('Открываем нужный репозиторий {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()



@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверка наличия Issue с номером {number}")
def should_see_issue_with_number(number):
    s("[data-testid='list-row-repo-name-and-number']").should(have.text(number))