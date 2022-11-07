import pandas as pd
import matplotlib.pylab as plt

#data = pd.read_excel("C:\\Users\\Acer\\Downloads\\Hierarchical clustering Assignment\\crime_data (2)\\EastWestAirlines.xlsx")
# multiple sheet
Univ1 = pd.read_csv("C:\\Users\Acer\Downloads\Dimension Reduction Assignment\wine\wine.csv")
Univ1 = pd.read_excel('C:\\Users\\Acer\\Downloads\\Hierarchical clustering Assignment\\crime_data (2)\\EastWestAirlines.xlsx', sheet_name="data")
Univ1.describe().cc1_miles
Univ1.columns
Univ = Univ1.drop(['Type','Alcalinity', 'Magnesium', 'Phenols',
       'Flavanoids', 'Nonflavanoids', 'Proanthocyanins', 'Color', 'Hue',
       'Dilution', 'Proline'], axis=1)
Univ1.columns = ['ID', 'Balance', 'Qual_miles', 'cc1_miles', 'cc2_miles', 'cc3_miles',
       'Bonus_miles', 'Bonus_trans', 'Flight_miles_12mo', 'Flight_trans_12',
       'enroll', 'Award']

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)
# choose by column
 #train_features = train_df.iloc[:, [0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]
# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(Univ.iloc[:, [1,6,10]])
df_norm = norm_func(Univ.iloc[:, :])
df_norm.describe()

# for creating dendrogram
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z = linkage(df_norm, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()


# Now applying AgglomerativeClustering choosing 5 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

h_complete = AgglomerativeClustering(n_clusters=3, linkage = 'complete', affinity = "euclidean").fit(df_norm) 
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

Univ['clust'] = cluster_labels # creating a new column and assigning it to new column 

final = Univ.iloc[:, [3,0,1,2]]
final.head()

# Aggregate mean of each cluster
final.iloc[:, 1:].groupby(final.clust).mean()

z = linkage(final, method = "complete", metric = "euclidean")
# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 # font size for the x axis labels
)
plt.show()
# creating a csv file 
final.to_csv("University.csv", encoding = "utf-8")

import os
os.getcwd()
# barplot
import seaborn as sns
sns.countplot(x="clust", data=Univ)
plt.show()
# KIRA SETIAP CLUSTER ADA BRAPA NEGARA
Univ.clust.value_counts()
# Joint Plot ikut cluster
plt.figure(figsize=(30,25))
grouped_Univ = Univ[['enroll','Qual_miles', 'cc1_miles',
       'Bonus_miles', 'Bonus_trans', 'Flight_miles_12mo', 'Flight_trans_12', 'Balance','clust']].groupby('clust').mean()
axes = grouped_Univ.plot.bar(subplots=True)
plt.show()

# Profiling all features together
grouped_Univ.plot(kind='bar', colormap='Accent')    
grouped_Univ.plot(kind='bar',logy=True, colormap='Accent')    
plt.show()

# identify country belong to a cluster
Univ[Univ['clust']==1]


# Filter the data for that cluster, change label of cluster

Univ1.loc[Univ1['clust'] == 0,'clust'] ='Developing Countries'
Univ1[Univ1['clust'] == 'Developing Countries']
