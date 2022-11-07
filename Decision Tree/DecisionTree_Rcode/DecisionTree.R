# Load the Data to see if the customer will default or not
# credit.csv

library(readr)
credit <- read.csv(file.choose(),stringsAsFactors = TRUE)

##Exploring and preparing the data ----
str(credit)
View(credit)
credit <- credit[-16]

# look at the class variable
table(credit$default)

# Shuffle the data
credit_rand <- credit[order(runif(1000)), ]
str(credit_rand)

#credit_rand$default <- as.factor(credit_rand$default)
#credit_train$checking_balance <- as.factor(credit_train$checking_balance)

# split the data frames
credit_train <- credit_rand[1:900, ]
credit_test  <- credit_rand[901:1000, ]

# check the proportion of class variable
prop.table(table(credit_rand$default))
prop.table(table(credit_train$default))
prop.table(table(credit_test$default))


# Step 3: Training a model on the data
#install.packages("C50")
library(C50)

credit_model <- C5.0(credit_train[,-16], credit_train$default)
windows()
plot(credit_model)

# Display detailed information about the tree
summary(credit_model)

# Step 4: Evaluating model performance
# Test data accuracy
test_res <- predict(credit_model, credit_test)
test_acc <- mean(credit_test$default == test_res)
test_acc

# cross tabulation of predicted versus actual classes
library(gmodels)
CrossTable(credit_test$default, test_res, prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn = c('actual default', 'predicted default'))

# On Training Dataset
train_res <- predict(credit_model, credit_train)
train_acc <- mean(credit_train$default == train_res)
train_acc


# cross tabulation of predicted versus actual classes
library(gmodels)
CrossTable(credit_train$default, train_res, prop.chisq = FALSE, prop.c = FALSE, prop.r = FALSE,
           dnn = c('actual default', 'predicted default'))


