
from playwright.async_api import Page, TimeoutError as PlayWrightTimeoutError
import re

class PageManager:
    def __init__(self, page: Page):
        self.page = page


    async def goto(self, url: str):
        """Navigate to the given URL"""
        try:
            await self.page.goto(url)
            print("Navigated to", url)

        except PlayWrightTimeoutError:
            raise RuntimeError(f"TimeoutError: Could not navigate to {url}")


    async def accept_cookies(self):
        """Accept cookies"""
        try:
            await self.page.click("#onetrust-accept-btn-handler", timeout=3000)
            print("Accepted cookies")

        except PlayWrightTimeoutError:
            raise RuntimeError("TimeoutError: Could not accept cookies")


    async def close_genius_popup(self):
        """Close Genius popup if displayed, using regex to match button name"""
        try:
            await self.page.get_by_role("button", name=re.compile("ignorar|ignore|skip", re.I)).click(timeout=3000)
            print("Closed Genius popup")
        except:
            pass

