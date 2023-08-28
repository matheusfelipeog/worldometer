from typing import Dict, List, Optional, Tuple, Union

import pandas as pd


def get_rts_counters_only_with_last_value_key(
    rts_counters: Dict[str, dict]
) -> Dict[str, Union[int, float, None]]:
    return {
        key: subdict.get('last_value') or None
        for key, subdict in rts_counters.items()
    }


def get_html_tables_data(
    html: str,
    attrs: Optional[Dict[str, str]],
    new_column_names: List[Tuple[str, ...]]
) -> List[List[dict]]:
    data = []
    dfs = pd.read_html(html, attrs=attrs, flavor='bs4')
    for idx, df in enumerate(dfs):
        df.columns = new_column_names[idx]
        data.append(df.to_dict(orient='records'))
    return data
