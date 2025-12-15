
from playwright.async_api import async_playwright, Browser, BrowserContext,ViewportSize
from typing import Tuple

DEFAULT_USER_AGENT = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64),"
    "AppleWebKit/537.36 (KHTML, like Gecko),"
    "Chrome/122.0.0.0 Safari/537.36"
}

view_port_width = 1366,
view_port_height = 768

view_port_size: ViewportSize | None = ViewportSize(view_port_width, view_port_height)

class BrowserFactory:

    def __init__(self, headless: bool = True, user_agent: str = DEFAULT_USER_AGENT,
                 navigation_timeout_ms: int = 60000):

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
            viewport=ViewportSize,
            locale="es-ES"
        )

        self._context.set_default_navigation_timeout(self.navigation_timeout_ms)
        self._context.set_default_timeout(self.navigation_timeout_ms)

        return self._browser, self._context


    async def new_page(self):
        if self._context:
            raise RuntimeError("Browser context is not initialized. Call start() first")

        return await self._context.new_page()

    async def close(self):
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        if self._context:
            await self._context.close()




