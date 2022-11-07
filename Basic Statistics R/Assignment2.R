
# R Packages
install.packages("readr")
library(readr)

# Read data into R
book <- read_csv("C:\\Users\\Acer\\Downloads\\module\\book.csv")
module <- read.csv(file.choose()) # load csv file into R

# C:\Users\Desktop\education.csv - this is windows default file path with a '\'
# C:\\Users\\Desktop\\education.csv - change it to '\\' to make it work in R

View(book)

#Exploratory Data Analysis
#Measures of Central Tendency / First moment business decision

mean(module$Measure) # '$' is used to refer to the variables within object

attach(book) # When used we can directly refer to the variable name
mean(Points)

rm(education) # Remove specific object to free RAM (memory)
rm(list=ls()) # Remove all to free RAM (memory)

median(Points)# Median

# Mode
x <- c(Score)
Mode <- function(x){
  a = table(x)        # x is a vector
  return(a[which.max(a)])
}
Mode(x)

# Measures of Dispersion / Second moment business decision
var(workex) # variance
sd(workex)  # standard deviation
range <- max(workex) - min(workex) # range

# Third moment business decision
install.packages("moments")
library(moments)
skewness(Points)

# Fourth moment business decision
kurtosis(Points)

# Graphical Representation
barplot(Measure)

dotchart(Weigh)

hist(Measure) # histogram

boxplot(Measure) # boxplot
y <- boxplot(Measure)

y$out # to see outliers

# Probability Distribution
install.packages("UsingR")
library("UsingR")
densityplot(Measure)

# Normal Quantile-Quantile Plot
qqnorm(Score)
qqline(Score)

qqnorm(workex)
qqline(workex)

# Transformation to make workex variable normal
qqnorm(log(Score))
qqline(log(Score))

# z-distribution
pnorm(680,711,29) # given a value, find the probability
qnorm(0.975)      # given probability, find the Z value

# t-distribution
pt(1.98, 139)  # given a value, find the probability
qt(0.975, 139) # given probability, find the t value


