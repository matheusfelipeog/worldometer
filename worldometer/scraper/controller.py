from typing import Dict, List, Optional, Union

from worldometer.scraper.browser import Browser
from worldometer.scraper.parser import get_rts_counters_only_with_last_value_key
from worldometer.scraper.parser import get_html_tables_data

from worldometer.scraper.utils import make_url

BASE_URL = 'https://www.worldometers.info'

browser = Browser()


def get_rts_counters_object() -> Dict[str, Union[int, float, None]]:
    url = make_url(BASE_URL)
    html = browser.get_page_content(url)
    script_return = browser.run_js_script(html, script='() => rts_counters')
    rts_counters = get_rts_counters_only_with_last_value_key(rts_counters=script_return)
    return rts_counters


def get_data_tables(
    path_url: str,
    new_headers: List[List[str]],
    render: bool = False,
    use_attrs: Optional[bool] = True
) -> List[List[dict]]:
    attrs = {'class': 'table'} if use_attrs else None
    url = make_url(BASE_URL, path_url)
    html = browser.get_page_content(url)
    if render:
        browser.render_page(html)
    data = get_html_tables_data(html.html, new_headers, attrs)
    return data
