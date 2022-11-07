# Implementing Apriori algorithm from mlxtend
# apriori() function evaluate support value for each product.
#conda install mlxtend

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

groceries = []

# As the file is in transaction data we will be reading data directly 
with open("C:/Users/Acer/Desktop/Data Science/Association Rules/groceries/groceries.csv") as f:
    groceries = f.read()

# Splitting the data into separate transactions using separator as "\n"
# satu line akan jadi satu string
groceries = groceries.split("\n")

groceries_list = [] # list kosong
for i in groceries:
    groceries_list.append(i.split(","))
    # split ayat jadi collection of keywords
    
all_groceries_list = [i for item in groceries_list for i in item]
# listkan setiap keyword

from collections import Counter
item_frequencies = Counter(all_groceries_list)
# brapa kali setiap barang kluar dlm transaction

# After sorting
item_frequencies = sorted(item_frequencies.items(), key = lambda x:x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in item_frequencies])) # frequency in descending order
items = list(reversed([i[0] for i in item_frequencies]))

# Barplot of top 10 
import matplotlib.pyplot as plt
colors = ["red","green","blue","black","yellow","magenta","cyan", "pink","orange","brown"]
plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color=colors); plt.xticks(list(range(0,11),), items[0:11]); plt.xlabel("items"); plt.ylabel("Count")

# Creating Data Frame for the transactions data 

# Purpose of converting all list into Series object Coz to treat each list element as entire element not to separate 
groceries_series  = pd.DataFrame(pd.Series(groceries_list))
groceries_series = groceries_series.iloc[:9835,:] # removing the last empty transaction

groceries_series.columns = ["transactions"]

# Creating a dummy columns for the each item in each transactions ... Using column names as item name
X = groceries_series['transactions'].str.join(sep='*').str.get_dummies(sep='*')
# kira support values
# Support is an indication of how frequently the itemset appears in the dataset
# one might want to consider only the itemsets which occur
# at least 50 times out of a total of 10,000 transactions i.e. support = 0.005
frequent_itemsets = apriori(X, min_support=0.008, max_len=3, use_colnames = True)

# Most Frequent item sets based on support 
# Confidence is an indication of how often the rule has been found to be true.
colors = ["red","green","blue","black","yellow","magenta","cyan", "pink","orange","brown"]
frequent_itemsets.sort_values('support', ascending = False, inplace=True)
plt.bar(x = list(range(1,11)), height = frequent_itemsets.support[1:11], color=colors)
plt.xticks(list(range(1,11)),frequent_itemsets.itemsets[1:11])
plt.xlabel('item-sets');plt.ylabel('support')
# lift ratio
rules = association_rules(frequent_itemsets, metric="lift", min_threshold = 1)
rules.head(10)
rules.sort_values('lift', ascending = False, inplace=True)

help(rules.sort_values)

########################## To eliminate Redudancy in Rules #################################### 
def to_list(i):
    return (sorted(list(i)))

ma_X = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]
index_rules = []
for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

# Getting rules without any redudancy 
rules_no_redudancy  = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending=False).head(10)

