from typing import Dict, Union

from requests_html import HTML, HTMLSession


class HTTPRequester:

    def __init__(self, timeout: int = 30) -> None:
        self.base_url = 'https://www.worldometers.info'
        self.session = HTMLSession()
        self.timeout = timeout

    def get_page_content(self, url_path: str = '') -> HTML:
        url = f'{self.base_url}/{url_path}'
        res = self.session.get(url, timeout=self.timeout)

        # requests-html does not have the type hint set correctly in
        # some modules (session.get is one of them), so type checkers
        # report a problem. I will probably trade this package in the future.
        html_obj = res.html  # type: ignore
        return html_obj

    def render_page(self, html_obj: HTML, script: str = '') -> Union[HTML, Dict[str, dict]]:

        script_return = html_obj.render(script=script)

        if script and script_return:
            return script_return

        return HTML(html=html_obj.html)
