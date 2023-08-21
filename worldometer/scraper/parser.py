from typing import Dict, Optional


def get_rts_counters_only_with_last_value_key(rts_counters: Dict[str, dict]) -> Dict[str, Optional[int]]:
    return {key: val.get('last_value') for key, val in rts_counters.items()}
