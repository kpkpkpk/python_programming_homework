from scipy.stats import pearsonr

list1 = [1, 1]
list2 = [1, 1]
list3 = [4, 1, 0, 25, 9, 16]

corr, _ = pearsonr(list1, list2)
# corr, _ = pearsonr(list1, list3)
print(f'Pearsons correlation: {corr}')
