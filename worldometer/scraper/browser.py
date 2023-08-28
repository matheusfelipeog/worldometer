from typing import Dict

from requests_html import HTML, HTMLSession


class Browser:

    def __init__(self) -> None:
        self.session = HTMLSession()

    def get_page_content(self, url: str, timeout: int = 30) -> HTML:
        res = self.session.get(url, timeout=timeout)

        # requests-html does not have the type hint set correctly in
        # some modules (session.get is one of them), so type checkers
        # report a problem. I will probably trade this package in the future.
        html_obj = res.html  # type: ignore
        return html_obj

    def render_page(self, html_obj: HTML) -> None:
        html_obj.render()

    def run_js_script(self, html_obj: HTML, script: str = '') -> Dict[str, dict]:
        script_return = html_obj.render(script=script)
        return script_return  # type: ignore