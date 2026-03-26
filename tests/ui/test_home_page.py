from pages.home_page import HomePage


def test_home_page_loads_successfully(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home
    _page_to_load()

    assert home_page.is_main_heading_displayed(), "Main heading is not displayed on the Home page."


def test_click_home_stays_on_home_page(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home_page_to_load()

    home_page.click_home()

    assert "atid.store" in home_page.get_current_url(), "Clicking HOME did not keep user on home page."


def test_click_store_navigates_to_store_page(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home_page_to_load()

    home_page.click_store()

    assert "store" in home_page.get_current_url().lower(), "User was not redirected to Store page."


def test_click_men_navigates_to_men_category(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home_page_to_load()

    home_page.click_men()

    assert "men" in home_page.get_current_url().lower(), "User was not redirected to Men category."


def test_click_women_navigates_to_women_category(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home_page_to_load()

    home_page.click_women()

    assert "women" in home_page.get_current_url().lower(), "User was not redirected to Women category."


def test_click_accessories_navigates_to_accessories_category(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home_page_to_load()

    home_page.click_accessories()

    assert "accessories" in home_page.get_current_url().lower(), "User was not redirected to Accessories category."


def test_click_about_navigates_to_about_page(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home_page_to_load()

    home_page.click_about()

    assert "about" in home_page.get_current_url().lower(), "User was not redirected to About page."


def test_click_contact_us_navigates_to_contact_page(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home_page_to_load()

    home_page.click_contact_us()

    current_url = home_page.get_current_url().lower()
    assert "contact" in current_url or "contact-us" in current_url, "User was not redirected to Contact Us page."


def test_shop_now_button_navigates_to_store(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.wait_for_home_page_to_load()

    home_page.click_shop_now()

    assert "store" in home_page.get_current_url().lower(), "SHOP NOW button did not redirect to Store page."


def test_find_more_button_navigates_somewhere1(driver, base_url):
    home_page = HomePage(driver, base_url)

    home_page.open()
    home_page.wait_for_home_page_to_load()

    home_page.click_find_more()

    current_url = home_page.get_current_url().lower()

    assert current_url != base_url.lower()

def test_find_more_button_navigates_somewhere2(driver, base_url):
    home_page = HomePage(driver, base_url)

    home_page.open()
    home_page.wait_for_home_page_to_load()

    home_page.click_find_more()

    current_url = home_page.get_current_url().lower()

    assert "contact" in current_url