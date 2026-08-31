from playwright.sync_api import Page, expect, Route
import re
import json


def test_iphone_rename(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()

        def rename_product(obj):
            if isinstance(obj, dict):
                for key, value in list(obj.items()):
                    if isinstance(value, str):
                        new_value = re.sub(r'iPhone\s+17\s+Pro', 'яблокофон 17 про', value)
                        if new_value != value:
                            obj[key] = new_value
                        else:
                            rename_product(value)
                    else:
                        rename_product(value)
            elif isinstance(obj, list):
                for item in obj:
                    rename_product(item)

        rename_product(body)

        route.fulfill(
            response=response,
            body=json.dumps(body)
        )

    page.route("https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat&fae=true", handle_route)

    page.goto('https://www.apple.com/shop/buy-iphone')

    page.locator('h3.rf-hcard-content-title:has-text("iPhone 17 Pro")').first.click()

    popup_title = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')

    expect(popup_title).to_have_text(re.compile(r'\s*яблокофон\s+17\s+про\s*'))
