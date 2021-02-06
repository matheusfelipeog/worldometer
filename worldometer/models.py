from requests_html import HTMLSession

from .const import URL

class Worldometer(object):
    def __init__(self):
        session = HTMLSession()

        try:
            # Get html page and render dynamic content
            self._r = session.get(URL, timeout=15)
            self._r.html.render()

        except Exception as err:
            raise Exception(err)
