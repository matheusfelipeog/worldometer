from typing import Dict, List, Optional

import pandas as pd


def get_rts_counters_only_with_last_value_key(rts_counters: Dict[str, dict]) -> Dict[str, Optional[int]]:
    return {key: val.get('last_value') for key, val in rts_counters.items()}


def get_html_table_data(
    html: str,
    new_headers: List[str],
    table_position: int = 0
) -> List[dict]:
    dfs = pd.read_html(html)
    df = dfs[table_position]
    df.columns = new_headers
    data = df.to_dict(orient='records')
    return data
