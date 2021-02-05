from requests_html import HTMLSession 

from .const import URL

class Worldometer(object):
    def __init__(self):
        self._session = HTMLSession()

        # Get html page and render dynamic content
        self._r = self._session.get(URL)
        self._r.html.render()
