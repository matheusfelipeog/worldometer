
from requests_html import HTMLSession 

from .const import worldometer_url

class Worldometer(object):
    def __init__(self):
        self._session = HTMLSession()

        # Get html page and render dynamic content
        self._r = self._session.get(worldometer_url)
        self._r.html.render()
