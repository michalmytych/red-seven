def get_items_count_dict(items: list) -> dict:
  counts = dict()
  for i in items:
    counts[i] = counts.get(i, 0) + 1
  return counts
