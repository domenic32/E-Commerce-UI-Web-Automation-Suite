import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"

def test_complete_item_purchase_flow(page: Page):
    """Verify end-to-end purchasing workflow from inventory to order confirmation."""
    # 1. Log in
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # 2. Add product to cart
    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    
    # 3. Navigate to Cart
    page.click(".shopping_cart_link")
    expect(page.locator(".cart_item")).to_have_count(1)
    
    # 4. Proceed to Checkout
    page.click("#checkout")
    
    # 5. Fill customer details
    page.fill("#first-name", "Jane")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "63901")
    page.click("#continue")
    
    # 6. Verify Overview and Finish
    expect(page.locator(".title")).to_have_text("Checkout: Overview")
    page.click("#finish")
    
    # 7. Assert Order Completion
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
