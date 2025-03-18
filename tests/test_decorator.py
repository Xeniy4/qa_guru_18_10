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
    search_for_text("eroshenkoam")


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


@allure.step('Открываем нужный репозиторий')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Ищем нужный текст {text}')
def search_for_text(text):
    s(".Box-sc-g0xbh4-0.kJvqaq.prc-Link-Link-85e08").should(have.text(text))