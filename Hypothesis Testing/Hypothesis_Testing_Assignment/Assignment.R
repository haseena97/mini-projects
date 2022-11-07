# Hypothesis Testing

# Load the Dataset
library(readxl)
library(readr)
# 2 sample t Test

######## Promotion.xlsx data ########## 2 continuous data
Promotion<-read_csv(file.choose())
Promotion<-read_excel(file.choose())
attach(Promotion)
colnames(Promotion)<-c("A","B")

# Changing column names
View(Promotion)
attach(Promotion)

# Normality test
shapiro.test(A)
# p-value = 0.2246 >0.05 so p high null fly => It follows normal distribution

shapiro.test(B)
# p-value = 0.1916 >0.05 so p high null fly => It follows normal distribution

# Variance test
var.test(A,B)
# p-value = 0.653 > 0.05 so p high null fly => Equal variances


# 2 sample t Test
t.test(A, B, alternative = "two.sided", conf.level = 0.95) 

# alternative = "two.sided" means we are checking for equal and unequal means
# null Hypothesis -> Equal means
# Alternate Hypothesis -> Unequal Hypothesis
# p-value = 0.02523 < 0.05 accept alternate Hypothesis unequal means
# p-value = 0.4723 > 0.05 accept null Hypothesis equal means
?t.test
t.test(A, B, alternative = "greater", var.equal = T)

# alternative = "greater means true difference is greater than 0
# Null Hypothesis -> (InterestRateWaiver-StandardPromotion) < 0
# Alternative Hypothesis -> (StandardPromotion - InterestRateWaiver) > 0
# p-value = 0.01211 < 0.05 => p low null go => accept alternate hypothesis
# InterestRateWaiver better promotion than StandardPromotion


########## Anova ##########

library(readr)
# Load the data : Contract_Renewal Data
CRD <- read_csv(file.choose())
View(CRD)
attach(CRD)
colnames(CRD)<-c("1","2","3","4")

# Changing column names
View(CRD)
attach(CRD)
# Normality test
shapiro.test(`1`)
shapiro.test(`2`)
shapiro.test(`3`)
shapiro.test(`4`)
# Variance test
var.test(`1`,`2`)
var.test(`2`,`3`)
var.test(`3`,`4`)
var.test(`4`,`1`)
Stacked_Data <- stack(CRD)
?stack
View(Stacked_Data)

attach(Stacked_Data)
colnames(Stacked_Data)

Anova_results <- aov(values~ind, data = Stacked_Data)
summary(Anova_results)

# p-value = 0.104 > 0.05 accept null hypothesis
# 3 suppliers transaction times are equal


########### Proportional T Test ##########
library(readxl)
library(readr)
# Load the data: JohnyTalkers data
Johnytalkers<-read_excel(file.choose()) 
Foot<-read_csv(file.choose()) 
View(Foot)

attach(Foot)

table1 <- table(Female)
table1
table2 <- table(Weekend)
table2
table3 <- table(Weekdays, Weekend)
table3

?prop.test
prop.test(x=c(113,167),n=c(400,400), conf.level = 0.95, alternative = "two.sided")
# two.sided -> means checking for equal proportions of Adults and children under purchased
# p-value = 6.261e-05 < 0.05 accept alternate hypothesis i.e.
# Unequal proportions 

prop.test(x=c(58,152),n=c(480,740), conf.level = 0.95, alternative = "greater")
# Ha -> Proportions of Adults > Proportions of Children
# Ho -> Proportions of Children > Proportions of Adults
# p-value = 0.999 > 0.05 accept null hypothesis 
# so proportion of Children > proportion of children 
# Do not launch the ice cream shop


######### Chi Square Test ##########
library(readxl)
library(readr)
# Load the data: Bahaman.xlsx
Bahaman<-read_excel(file.choose())
Course<-read_csv(file.choose())
View(Course)
Stacked_Data <- stack(Course)
?stack
View(Stacked_Data)
colnames(Stacked_Data)<-c("Defective","Country")
View(Stacked_Data)
attach(Stacked_Data)
table(Country,Defective)

chisq.test(table(Country,Defective))

# p-value = 0.6315 > 0.05  => Accept null hypothesis
# => All countries have equal proportions 

# All Proportions are equal 
