
# Implementing Apriori algorithm from mlxtend
# apriori() function evaluate support value for each product.
#conda install mlxtend

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
book = pd.read_csv("C:/Users/Acer/Desktop/Data Science/Association Rules/Association Rules Assignment/Data Sets/book.csv")

# kira support values
# Support is an indication of how frequently the itemset appears in the dataset
# one might want to consider only the itemsets which occur
# at least 50 times out of a total of 10,000 transactions i.e. support = 0.005
frequent_itemsets = apriori(book, min_support=0.008, max_len=3, use_colnames = True)
frequent_itemsets = apriori(book, min_support=0.008, use_colnames = True)
# sort to see highest support first
frequent_itemsets.sort_values('support', ascending = False, inplace=True)

# Most Frequent item sets based on support 
# Confidence is an indication of how often the rule has been found to be true.
import matplotlib.pyplot as plt
colors = ["red","green","blue","black","yellow","magenta","cyan", "pink","orange","brown"]
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
rules_no_redudancy.sort_values('lift', ascending=False, inplace = True)

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending=False).head(10)
import seaborn as sns
import matplotlib.pyplot as plt
############################## Visualization ##########################################
rules_no_redudancy['lhs_items'] = rules_no_redudancy['antecedents'].apply(lambda x:len(x) )
rules_no_redudancy[rules_no_redudancy['lhs_items']>1].sort_values('lift', ascending=False).head()
rules_no_redudancy['antecedents_'] = rules_no_redudancy['antecedents'].apply(lambda a: ','.join(list(a)))
rules_no_redudancy['consequents_'] = rules_no_redudancy['consequents'].apply(lambda a: ','.join(list(a)))
pivot = rules_no_redudancy[rules_no_redudancy['lhs_items']>1].pivot(index = 'antecedents_', columns = 'consequents_', values= 'lift')
sns.heatmap(pivot, annot = True)
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()