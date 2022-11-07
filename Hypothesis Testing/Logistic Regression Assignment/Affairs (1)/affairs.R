# Load the Dataset
install.packages('AER')
data(Affairs,package="AER")
View(Affairs)
claimants <- read.csv(file.choose()) # Choose the claimants Data set
View (claimants)
Affair2 <- Affair2[, -1]
write.csv(Affairs,"C:\\Users\\Acer\\Downloads\\Affairs (1)\\Affair.csv", row.names = TRUE)
# tukar binary variables
Affairs$gender<-ifelse(Affairs$gender=="male",1,0)
Affairs
# randomly split train test data
#Use 70% of dataset as training set and remaining 30% as testing set
sample <- sample(c(TRUE, FALSE), nrow(Affair2), replace=TRUE, prob=c(0.7,0.3))
Affairs_train  <- Affair2[sample, ]
Affairs_test   <- Affair2[!sample, ]

claimants <- read.csv(file.choose()) # Choose the claimants Data set
View (claimants)
colnames(claimants) # give column names
claimants <- claimants[, -1] # Removing the first column which is is an Index
# split into train and test
Affairs_train <- Affairs[1:421, ]
Affairs_test <- Affairs[422:601, ]
# train data into logistic model (binomial)
model <- glm(affairs2~., data = Affairs_train, family = "binomial")
summary(model)

# Prediction on Test data 
prob_test <- predict(model, Affairs_test, type="response")
prob_test

# Confusion matrix and considering the threshold value as 0.5 
confusion_test <- table(prob_test>0.5, Affairs_test$affairs2)
confusion_test

# Model Accuracy 
Accuracy_test <- sum(diag(confusion_test)) / sum(confusion_test)
Accuracy_test


# Prediction on Train data 
prob_train <- predict(model, Affairs_train, type="response")

# Confusion matrix and considering the threshold value as 0.5 
confusion_train <- table(prob_train > 0.5, Affairs_train$affairs2)
confusion_train

# Model Accuracy 
Accuracy_train <- sum(diag(confusion_train)) / sum(confusion_train)

install.packages('ROCR')
library(ROCR)
rocrpred<-prediction(prob_test,Affair2$affairs2)
rocrperf<-performance(rocrpred,'tpr','fpr')

str(rocrperf)