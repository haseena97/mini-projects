install.packages("arules")
install.packages("arulesViz")

library("arules")
library(arulesViz)

### On inbuilt Data set #####
data()
data("Groceries")
?Groceries

summary(Groceries)
inspect(Groceries[1:5])

rules <- apriori(Groceries, parameter = list(support = 0.003, confidence = 0.7, minlen = 2))
inspect(rules[1:5])


windows()
plot(rules, method = "scatterplot")
plot(rules, method = "grouped")

rules <- sort(rules,by="lift")

inspect(rules[1:5])
