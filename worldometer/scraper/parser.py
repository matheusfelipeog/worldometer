from typing import Dict


def get_rts_counters_only_with_last_value_key(rts_counters: Dict[str, dict]):
    return {key: val.get('last_value') for key, val in rts_counters.items()}
