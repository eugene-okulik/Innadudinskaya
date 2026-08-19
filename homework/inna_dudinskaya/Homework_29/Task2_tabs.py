from playwright.sync_api import Page, BrowserContext, expect


def test_new_tab_button(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')

    button = page.get_by_role('link', name='Click')

    with context.expect_page() as new_page_event:
        button.click()

    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()

    expect(button).to_be_enabled()
