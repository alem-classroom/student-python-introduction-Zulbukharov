def clear_dict(dict):
    dict.clear()
    return {}
    # delete everything in dict and return it

def get_dict_items(dict):
    return dict.items()
    # return keys and values of dict

def get_dict_keys(dict):
    return dict.keys()

def get_dict_value_by_key(dict, key):
    return dict.get(key)

def delete_dict_element_by_key(dict, key):
    if key in dict: del dict[key]

