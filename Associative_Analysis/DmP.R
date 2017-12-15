
#reading the data file
mydata <- read.csv("C:\\Users\\ShivarajRs\\Desktop\\PRoject\\DM.csv", header=T, colClasses="factor")

#finding association rules
library(arules)
rules<-apriori(mydata)
summary(rules)
inspect(rules)

#reduce to small number of rules
rules <- apriori(mydata,parameter = list(minlen=1, maxlen=3 ,supp=.8))
inspect(rules)

View()
#finding interesting rules-1
rules <- apriori(mydata, parameter = list(minlen=1, maxlen=5, conf=.8, supp=0.005),
                 appearance = list(rhs=c("DistrictName=Bagalakot"), default="lhs"))
rules.sorted <- sort(rules, by="lift")
inspect(rules.sorted)

library(arulesViz)
Plot(mydata, method="graph",sup=0.8)

#pruning redundant rules
#find redundant rules
subset.matrix <- is.subset(rules.sorted,rules.sorted)
subset.matrix[lower.tri(subset.matrix, diag = T)] <- NA
redundant <- colSums(subset.matrix, na.rm = T) >= 2
which(redundant)

#remove redundant rules
rules.pruned <- rules.sorted[!redundant]
inspect(rules.pruned)

#visualizing association rules
library(arulesViz)
plot(rules)
plot(rules.sorted)
#plot(rules, method = "grouped")
plot(rules,method = "graph",control = list(type="Commodity"))
plot(rules,method = "graph",control = list(type="Month"))
plot(rules,method = "graph",control = list(type="Unit"))
plot(rules,method="graph",interactive=TRUE,shading=NA)
