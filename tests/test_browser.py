import pytest
from src.core.browser import BrowserFactory


@pytest.mark.asyncio
async def test_browser():
    print("Opening Browser...")
    factory = BrowserFactory(headless=False)

    browser, context = await factory.start()

    print("Creating new page...")
    page = await context.new_page()

    print("Navigating to Booking...")
    await page.goto("https://www.booking.com")

    print("Closing browser...")
    await factory.close()