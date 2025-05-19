from django.core.exceptions import ValidationError

def title_validator(value: str):
    restricted_symbols = "@#~/<>"
    for sym in restricted_symbols:
        if sym in value: raise ValidationError(f'{sym} is restricted.')
    return value

def tag_validator(value: str):
    restricted_symbols = "!@#$%^&*()_+-={}~`:|<>?;'\,./'"+'"'
    for sym in restricted_symbols:
        if sym in value: raise ValidationError(f'{sym} is restricted.')
    return value