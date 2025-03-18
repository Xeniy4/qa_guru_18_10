from selene import have
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.config.window_width = 1900
    browser.config.window_height = 1080
    browser.open("https://github.com")


    s(".header-search-button.flex-1").click()
    s("#query-builder-test").type("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s("[data-testid='list-row-repo-name-and-number']").should(have.text('95'))