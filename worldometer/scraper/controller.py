from typing import Dict, Optional

from worldometer.scraper.browser import Browser
from worldometer.scraper.parser import get_rts_counters_only_with_last_value_key

from worldometer.scraper.utils import make_url

BASE_URL = 'https://www.worldometers.info'

browser = Browser()


def get_rts_counters_object() -> Dict[str, Optional[int]]:
    url = make_url(BASE_URL)
    html = browser.get_page_content(url)
    script_return = browser.run_js_script(html, script='() => rts_counters')
    rts_counters = get_rts_counters_only_with_last_value_key(rts_counters=script_return)
    return rts_counters
