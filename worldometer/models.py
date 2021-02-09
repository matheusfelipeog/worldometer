import re

from requests_html import HTML, HTMLSession

from .const import URL
from .const import CSS_SELECTOR_OF_COUNTER_NUMBERS


class Worldometer(object):
    def __init__(self):
        self.metrics = self.collect_metrics()
        
    @staticmethod
    def _get_html(url: str) -> str:

        session = HTMLSession()
        timeout = 15  # in seconds

        try:
            # Get html page and render dynamic content
            r = session.get(url, timeout=timeout)
            r.html.render(timeout=timeout)

            return r.html.raw_html

        except Exception as err:
            raise Exception(err)

    @staticmethod
    def find_metrics_in_html(html_code: str) -> list:
        """Find worldometer metrics in html code."""

        html = HTML(html=html_code)

        # Get only text of all requests_html.Element object
        metrics = [metric.text for metric in html.find(CSS_SELECTOR_OF_COUNTER_NUMBERS)]

        return metrics

    @staticmethod
    def sanitize_metrics(metric_list: list) -> list:
        """Sanitize all metrics in list."""

        sanitized_metrics = []

        for metric in metric_list:
            
            # Get only the number and convert to int
            found = re.search(r'[0-9,]+', metric).group()
            number = int(found.replace(',', ''))

            sanitized_metrics.append(number)
        
        return sanitized_metrics

    def collect_metrics(self) -> list:
        """Collects all metrics from the worldometer site."""

        html = self._get_html(url=URL)
        metrics = self.find_metrics_in_html(html_code=html)
        sanitized_metrics = self.sanitize_metrics(metric_list=metrics)

        return sanitized_metrics
