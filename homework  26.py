
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
sym_diff_list = [x for x in set1 if x not in set2] + [x for x in set2 if x not in set1]
sym_diff_set = set(sym_diff_list)
print("Symmetric difference (list):", sym_diff_list)
print("Symmetric difference (set):", sym_diff_set)