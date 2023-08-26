from typing import Dict, List, Optional

import pandas as pd


def get_rts_counters_only_with_last_value_key(rts_counters: Dict[str, dict]) -> Dict[str, Optional[int]]:
    return {key: val.get('last_value') for key, val in rts_counters.items()}


def get_html_tables_data(
    html: str,
    new_headers: List[List[str]],
    attrs: Optional[Dict[str, str]]
) -> List[List[dict]]:
    data = []
    dfs = pd.read_html(html, attrs=attrs, flavor='bs4')
    for idx, df in enumerate(dfs):
        df.columns = new_headers[idx]
        data.append(df.to_dict(orient='records'))
    return data
