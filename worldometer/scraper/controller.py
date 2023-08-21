from typing import Dict, Optional

from worldometer.scraper.browser import Browser
from worldometer.scraper.parser import get_rts_counters_only_with_last_value_key


browser = Browser()


def get_rts_counters_object() -> Dict[str, Optional[int]]:
    html = browser.get_page_content('https://www.worldometers.info')
    script_return = browser.run_js_script(html, script='() => rts_counters')
    rts_counters = get_rts_counters_only_with_last_value_key(rts_counters=script_return)
    return rts_counters
