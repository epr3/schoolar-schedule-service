def exclude_keys(dict, keys):
  return {x: dict[x] for x in dict if x not in keys}