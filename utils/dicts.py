def get_val(collection: dict, key, default='unicorn'):
    if key in collection:
        return collection[key]
    else:
        return default
