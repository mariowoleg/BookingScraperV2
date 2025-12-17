from typing import Dict


DEFAULT_USER_AGENT: str = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

VIEWPORT_WIDTH: int = 1366
VIEWPORT_HEIGHT: int = 768

LOCALE: str = "es-ES"

NAVIGATION_TIMEOUT_MS: int = 60_000
ACTION_TIMEOUT_MS: int = 30_000

HEADLESS: bool = True

SCROLL_PAUSE_MS: int = 800
MAX_SCROLLS: int = 50

MAX_HOTELS: int | None = None  # None = todos

BOOKING_BASE_URL: str = "https://www.booking.com"

DEFAULT_SEARCH_PARAMS: Dict[str, str] = {
    "ss": "Barcelona",
    "checkin_year": "2025",
    "checkin_month": "12",
    "checkin_monthday": "25",
    "checkout_year": "2025",
    "checkout_month": "12",
    "checkout_monthday": "28",
    "group_adults": "2",
    "group_children": "0",
    "no_rooms": "1",
}

DEBUG: bool = True
SCREENSHOT_ON_ERROR: bool = True
