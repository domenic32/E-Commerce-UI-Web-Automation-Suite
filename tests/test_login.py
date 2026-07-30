import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"

def test_successful_login(page: Page):
    """Verify standard user can log in successfully."""
    page.goto(BASE_URL)
    
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # Assert URL redirect and inventory page visibility
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

def test_locked_out_user_error(page: Page):
    """Verify appropriate error message appears for a locked out user."""
    page.goto(BASE_URL)
    
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # Assert error banner appears with correct text
    error_container = page.locator("[data-test='error']")
    expect(error_container).to_be_visible()
    expect(error_container).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
