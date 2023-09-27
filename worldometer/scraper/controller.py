from typing import Dict, List, Optional, Tuple, Union

from worldometer.scraper.browser import Browser

from worldometer.scraper.parser import (
    get_rts_counters_only_with_last_value_key,
    get_html_tables_data
)

from worldometer.scraper.utils import make_url

from worldometer.scraper.consts import BASE_URL


browser = Browser()


def get_rts_counters_object(
        path_url: Optional[str] = None
) -> Dict[str, Union[int, float, None]]:
    url = make_url(BASE_URL, path_url)
    html = browser.get_page_content(url)
    script_return = browser.run_js_script(html, script='() => rts_counters')
    rts_counters = get_rts_counters_only_with_last_value_key(rts_counters=script_return)
    return rts_counters


def get_data_tables(
    path_url: str,
    new_column_names: List[Tuple[str, ...]],
    render: bool = False,
    attrs: Optional[Dict[str, str]] = {'class': 'table'}
) -> List[List[dict]]:
    url = make_url(BASE_URL, path_url)
    html = browser.get_page_content(url)

    if render:
        browser.render_page(html)

    data = get_html_tables_data(
        html=html.html,
        new_column_names=new_column_names,
        attrs=attrs
    )
    return data
