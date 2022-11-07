# Load the dataset
library(readr)
input <- read_csv(file.choose())
mydata <- input[, c(1,3:8)]
View(normalized_data)
# standardize/Normalize the data
normalized_data <- scale(mydata[, 2:7]) # Excluding the university name

d <- dist(input, method = "euclidean") # Distance matrix

fit <- hclust(d, method = "complete")

plot(fit) # Display dendrogram
plot(fit, hang = -1)

groups <- cutree(fit, k = 3) # Cut tree into 3 clusters

rect.hclust(fit, k = 3, border = "red")

membership <- as.matrix(groups)

final <- data.frame(membership, input)

aggregate(input[,1:3], by=list(final$membership), FUN = mean)

library(readr)
write_csv(final, "hclustoutput.csv")

getwd()
