from typing import Dict, List, Optional, Tuple, Union

from io import StringIO

import pandas as pd

from worldometer.scraper.exceptions import (
    ColumnNamesLengthError,
    HTMLTablesNotFoundError
)


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

    try:
        dfs = pd.read_html(io=StringIO(html), attrs=attrs, flavor='bs4')

        dfs_len = len(dfs)
        col_names_len = len(new_column_names)

        if dfs_len != col_names_len:
            raise ColumnNamesLengthError(
                f'{col_names_len} tuples of column names for {dfs_len} table'
            )

        for idx, df in enumerate(dfs):

            col_len = len(df.columns)
            new_col_len = len(new_column_names[idx])

            if col_len != new_col_len:
                raise ColumnNamesLengthError(
                    f'Table in position {idx} expected {col_len} column names but received {new_col_len}'
                )

            df.columns = new_column_names[idx]

            data.append(df.to_dict(orient='records'))

    except ValueError as err:
        expected_error_message = 'No tables found'

        if expected_error_message in err.args:
            raise HTMLTablesNotFoundError('No HTML tables found') from err

        raise

    return data
