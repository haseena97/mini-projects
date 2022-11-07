# Load the Dataset
library(readxl)
library(readr)
Promotion<-read_csv(file.choose())
attach(Promotion)
Stacked_Data <- stack(Promotion)
?stack
View(Stacked_Data)
colnames(Stacked_Data)<-c("Defective","Country")
View(Stacked_Data)
attach(Stacked_Data)
?write_csv
install.packages("writexl")
library("writexl")
write_xlsx(Stacked_Data,"C:\\Users\\Acer\\Downloads\\Hypothesis_Testing_Assignment\\new.xlsx")
