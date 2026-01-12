def nested_loop_join(left_rows, right_rows, left_key, right_key):
    result = []
    for l in left_rows:
        for r in right_rows:
            if l[left_key] == r[right_key]:
                result.append({**l, **r})
    return result
