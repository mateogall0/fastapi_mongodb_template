def clear_nones(data: dict) -> dict:
    return {k: v for k, v in data.items() if v is not None}
