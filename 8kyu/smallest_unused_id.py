def next_id(arr):
    return 0 if not arr or 0 not in arr and sum(arr) - sum(range(max(arr)+1)) == 0 else abs(arr and sum(arr) - sum(range(max(arr)+1))) if abs(arr and sum(arr) - sum(range(max(arr)+1))) > 0 else max(arr) + 1
