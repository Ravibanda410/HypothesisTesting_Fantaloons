
###################Proportional T Test(Fantaloons)##########

library(readxl)
Fantaloons <- read_excel(file.choose())
View(Fantaloons)
attach(Fantaloons)

#B.P:proportions of male and female walking in to the store is same or not

table1 <- table(Weekdays)
table1
table2 <- table(Weekend)
table2
table3 <- table(Weekdays,Weekend)
table3

#Ho= Proportions of Male and Female are same
#Ha= Proportions of Male and Female are not same
prop.test(x=c(47,167),c(113,287),conf.level = 0.95,alternative = "two.sided")
# two. sided -> means checking for equal proportions of Male and Female walking into stroe or not
# p-value = 0.003919 < 0.05 accept alternate hypothesis i.e. Unequal proportions


#find out whose proportion is higher
#Ho= Proportions of Male is less than Female
#Ha= Proportions of Male is greater than Female
prop.test(x=c(47,167),c(113,287),conf.level = 0.95,alternative = "greater")
# p-value = 0.998 > 0.05 accept null hypothesis 

#Proportions of Male is walking into store less than Female
