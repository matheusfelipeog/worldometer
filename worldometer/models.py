from requests_html import HTMLSession

from .const import URL


class Worldometer(object):
    def __init__(self):
        self._r = Worldometer._get(URL)
        
    @staticmethod
    def _get(url):

        session = HTMLSession()

        try:
            # Get html page and render dynamic content
            r = session.get(url, timeout=15)
            r.html.render()

            return r

        except Exception as err:
            raise Exception(err)
