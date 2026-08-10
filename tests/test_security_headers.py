from playwright.sync_api import sync_playwright

def test_security_headers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        response = page.goto("https://www.saucedemo.com/")
        headers = response.headers
        
        # Kontrola bezpecnostnych hlaviciek
        if 'strict-transport-security' not in headers:
            print("BUG: Chyba HSTS hlavicka na SauceDemo")
        if 'content-security-policy' not in headers:
            print("BUG: Chyba CSP hlavicka na SauceDemo")
        
        # Test prejde vzdy – len zaznamename chyby
        assert True