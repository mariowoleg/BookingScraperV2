
from playwright.async_api import async_playwright, Browser, BrowserContext,ViewportSize
from typing import Tuple
from src.config.settings import *

class BrowserFactory:

    def __init__(self, headless: bool = HEADLESS, user_agent: str = DEFAULT_USER_AGENT,
                 navigation_timeout_ms: int = NAVIGATION_TIMEOUT_MS):

        self.headless = headless
        self.user_agent = user_agent
        self.navigation_timeout_ms = navigation_timeout_ms
        self._playwright = None
        self._browser: Browser | None = None
        self._context: BrowserContext | None = None

    async def start(self) -> Tuple[Browser, BrowserContext]:
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(
            headless=self.headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        self._context = await self._browser.new_context(
            user_agent=self.user_agent,
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
            locale="es-ES"
        )

        self._context.set_default_navigation_timeout(self.navigation_timeout_ms)
        self._context.set_default_timeout(self.navigation_timeout_ms)

        return self._browser, self._context


    async def new_page(self):
        if not self._context:
            raise RuntimeError("Browser context is not initialized. Call start() first")

        return await self._context.new_page()

    async def close(self):
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        if self._context:
            await self._context.close()




