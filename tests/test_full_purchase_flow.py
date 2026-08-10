from playwright.sync_api import sync_playwright, expect

def test_full_purchase_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 1. Prihlasenie
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
        # 2. Pridanie produktov
        page.click("#add-to-cart-sauce-labs-backpack")
        page.click("#add-to-cart-sauce-labs-bike-light")
        cart_badge = page.locator(".shopping_cart_badge")
        expect(cart_badge).to_have_text("2")
        
        # 3. Prechod do kosika
        page.click(".shopping_cart_link")
        expect(page).to_have_url("https://www.saucedemo.com/cart.html")
        page.click("#checkout")
        
        # 4. Vyplnenie udajov
        page.fill("#first-name", "Frantisek")
        page.fill("#last-name", "Rados")
        page.fill("#postal-code", "04001")
        page.click("#continue")
        expect(page.locator(".summary_info")).to_be_visible()
        
        # 5. Dokoncenie
        page.click("#finish")
        success_message = page.locator(".complete-header")
        expect(success_message).to_have_text("Thank you for your order!")
        
        # 6. Odhlasenie
        page.click("#react-burger-menu-btn")
        page.click("#logout_sidebar_link")
        expect(page).to_have_url("https://www.saucedemo.com/")
        
        browser.close()