import page
import pytest


def test_prihlaseni_zakaznika(page):
    """Testování přihlášení do uživatelského menu přes zkušební email"""

    page.goto('https://www.brainmarket.cz')
    # čekání na vyskočení slevového okna
    discount = page.get_by_text("×").click()
    accept_button = page.get_by_test_id("buttonCookiesAccept").click()

    login = page.get_by_role("link", name="").click()

    input_email = page.get_by_test_id("inputEmail")
    input_email.fill("kikec6712@seznam.cz")

    input_password = page.get_by_test_id("inputPassword")
    input_password.fill("123456789")

    button_submit = page.get_by_test_id("buttonSubmit").click()
    page.wait_for_load_state("networkidle")

    button_signout = page.locator('a[data-testid="buttonSignout"]')

    assert button_signout.is_visible(), "Logout button is not visible on the page."


def test_vyhledani_zbozi_vlozeni_do_kosiku(page):
    """Testovaní vyhledávání zboží a potvrzení o vložení do košíku"""

    page.goto('https://www.brainmarket.cz')
    # čekání na vyskočení slevového okna
    discount = page.get_by_text("×").click()
    accept_button = page.get_by_test_id("buttonCookiesAccept").click()

    search_input = page.get_by_test_id("searchInput")
    search_input.fill("BrainMax NeuroHacker")

    search_button = page.get_by_test_id("searchBtn").click()
    page.wait_for_load_state("networkidle")

    link = page.get_by_role("link", name="BrainMax NeuroHacker, Dopamine Upgrade! 60 rostlinných kapslí Tip").click()

    shopping_cart = page.get_by_role("button", name="Přidat do košíku").click()

    added_to_cart = page.locator('div.h1', has_text='Přidáno do košíku')


    expected_text = 'Přidáno do košíku'
    assert added_to_cart.inner_text() == expected_text


def test_pridano_do_oblibenych(page):
    """Testování přidání produktu do oblíbených položek"""

    page.goto('https://www.brainmarket.cz')
    # čekání na vyskočení slevového okna
    discount = page.get_by_text("×").click()
    accept_button = page.get_by_test_id("buttonCookiesAccept").click()

    search_input = page.get_by_test_id("searchInput")
    search_input.fill("káva")

    search_button = page.get_by_test_id("searchBtn").click()

    page.wait_for_load_state("networkidle")

    coffee = page.locator('span[data-micro="name"]',
                          has_text='BrainMax Coffee Peru, zrnková káva, BIO, 1000 g *CZ-BIO-001 certifikát')
    coffee.click()

    page.wait_for_load_state("networkidle")

    fav_detail = page.locator("#dkLabFavDetailSpan")
    fav_detail.click()

    link_favorite = page.get_by_role("link", name="").click()
    page.wait_for_load_state("networkidle")

    element = page.locator('[title*="BrainMax Coffee Peru, zrnkov"]')

    assert element.is_visible(), "Element not found or not visible on the page."




