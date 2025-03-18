import allure
from selene import have
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_steps_github():
    with allure.step('Открываем главную страницу'):
        browser.config.window_width = 1900
        browser.config.window_height = 1080
        browser.open("https://github.com")

    with allure.step('Клик на поиске'):
        s(".header-search-button.flex-1").click()

    with allure.step('Пишем текст поиска репозитория'):
        s("#query-builder-test").type("eroshenkoam/allure-example")

    with allure.step('Нажимаем Enter'):
        s("#query-builder-test").submit()

    with allure.step('Открываем нужный репозиторий'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Ищем текст на странице репозитория eroshenkoam'):
        s(".Box-sc-g0xbh4-0.kJvqaq.prc-Link-Link-85e08").should(have.text('eroshenkoam'))

    # s("#issues-tab").click()
    #
    # s("[data-testid='list-row-repo-name-and-number']").should(have.text('95'))

    # s(by.partial_text("#76")).should(be.visible)