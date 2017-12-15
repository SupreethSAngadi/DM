library("gridExtra")
library("devtools")
library("mlbench")
library("caTools")
library("FastKNN")
library("fastknn")
library("glmnet")
library(caTools)
library(ggplot2)
library(readr)
library(dplyr)
library(ggvis)
library (class)
library(highcharter)
library(caret)
library(MASS)
library(ElemStatLearn)


#  load data
dep_data<-survey_Autosaved_

#data cleaning 
for (i in 1:27){
  if(sum(is.na(dep_data[,i]))>20)
    print(paste(i," ",sum(is.na(dep_data[,i]))))
  
}
#remove the attributes 
dep_data <- dep_data[,-c(5,9,27)]
sum(is.na(dep_data))
# 1.age
range(dep_data$Age)
#  -1.726e+03  1.000e+11:min and max are incorrect values
dep_data <- dep_data %>% filter((Age >0 & Age <100))
range(dep_data$Age)
sum(is.na(dep_data$Age))
#no missing values -> find outliers
hist(dep_data$Age)
#using tukey'S fivenumber summary
fivenum(dep_data$Age)
# q1=27,q3=36
IQR(dep_data$Age)
#iqr=9
out <- c((27-1.5*9),(36+1.5*9))
out
dep_data <- dep_data %>% filter(Age>out[1]) 

#2.gender

dep_data$Gender<- tolower(dep_data$Gender)
unique(dep_data$Gender)
#39 diff values : group everything into male/female/trans 

male <- c("male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man","msle", "mail", "malr","cis male","cis man")
trans<- c("trans-female", "something kinda male?", "queer/she/they", "non-binary","nah", "all", "enby", "fluid", "genderqueer", "androgyne", "agender", "male leaning androgynous", "guy (-ish) ^_^", "trans woman", "neuter", "female (trans)", "queer", "ostensibly male, unsure what that really means" )
female <- c("cis female", "f", "female", "woman",  "femake", "female ","cis-female/femme", "female (cis)", "femail")

dep_data$Gender <- sapply(dep_data$Gender,function(x) ifelse(x %in% male,"male",x))
dep_data$Gender <- sapply(dep_data$Gender,function(x) ifelse(x %in% trans,"trans",x))    
dep_data$Gender <- sapply(dep_data$Gender,function(x) ifelse(x %in% female,"female",x))

dep_data <- dep_data %>% filter(Gender != "a little about you")
dep_data <- dep_data %>% filter(Gender != "guy (-ish) ^_^")


#3.selfemployed
#fill missing values with mode
Mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}
Mode(dep_data$self_employed)
dep_data$self_employed <- sapply(dep_data$self_employed,function(x) ifelse(is.na(x),"No",x))

#4. no. of employees
unique(dep_data$no_employees)
# 01-may, jun-25 are missclassified; change them to 01-5, 6-25
dep_data$no_employees <- sapply(dep_data$no_employees,function(x) ifelse(x == "01-May","01-05",x))
dep_data$no_employees <- sapply(dep_data$no_employees,function(x) ifelse(x == "Jun-25","06-25",x))
dep_data[,8]<- sapply(dep_data[,8],function(x) ifelse(x == "01-05",1,x))
dep_data[,8]<- sapply(dep_data[,8],function(x) ifelse(x == "06-25",2,x))
dep_data[,8]<- sapply(dep_data[,8],function(x) ifelse(x == "26-100",3,x))
dep_data[,8]<- sapply(dep_data[,8],function(x) ifelse(x == "100-500",4,x))
dep_data[,8]<- sapply(dep_data[,8],function(x) ifelse(x == "500-1000",5,x))
dep_data[,8]<- sapply(dep_data[,8],function(x) ifelse(x == "More than 1000",6,x))

#leave
dep_data$leave <- sapply(dep_data$leave,function(x) ifelse(x == "Don't know",0,x))
dep_data$leave <- sapply(dep_data$leave,function(x) ifelse(x == "Very easy",1,x))
dep_data$leave <- sapply(dep_data$leave,function(x) ifelse(x == "Somewhat easy",2,x))
dep_data$leave <- sapply(dep_data$leave,function(x) ifelse(x == "Somewhat difficult",3,x))
dep_data$leave <- sapply(dep_data$leave,function(x) ifelse(x == "Very difficult",4,x))

#1 yes 0 no 2 don't know
for(i in 2:24){
  dep_data[,i] <- sapply(dep_data[,i],function(x) ifelse(x == "Yes",1,x))
  dep_data[,i]<- sapply(dep_data[,i],function(x) ifelse(x == "No",0,x))
  dep_data[,i]<- sapply(dep_data[,i],function(x) ifelse(x == "Don't know",2,x))
  dep_data[,i]<- sapply(dep_data[,i],function(x) ifelse(x == "Not sure",2,x))
  dep_data[,i]<- sapply(dep_data[,i],function(x) ifelse(x ==  "Some of them",2,x))
  dep_data[,i]<- sapply(dep_data[,i],function(x) ifelse(x ==  "Maybe",2,x))
}




#gender
dep_data[,3]<- sapply(dep_data[,3],function(x) ifelse(x ==   "male",1,x))
dep_data[,3]<- sapply(dep_data[,3],function(x) ifelse(x ==  "female",0,x))
dep_data[,3]<- sapply(dep_data[,3],function(x) ifelse(x ==  "trans",2,x))

#PLOTS  
g1<-ggplot(dep_data,aes(dep_data$remote_work, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("remote work",position = "bottom")+scale_y_continuous(position = "left")
g1

g2<-ggplot(dep_data,aes(dep_data$tech_company, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("Tech company",position = "bottom")+scale_y_continuous(position = "left")
g2

g3<-ggplot(dep_data,aes(dep_data$self_employed, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("Self employed",position = "bottom")+scale_y_continuous(position = "left")
g3

g4<-ggplot(dep_data,aes(dep_data$Gender, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("Gender",position = "bottom")+scale_y_continuous(position = "left")
g4

g5<-ggplot(dep_data,aes(dep_data$benefits, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("benefits",position = "bottom")+scale_y_continuous(position = "left")
g5

g6<-ggplot(dep_data,aes(dep_data$care_options, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("care options",position = "bottom")+scale_y_continuous(position = "left")
g6
g7<-ggplot(dep_data,aes(dep_data$wellness_program, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("wellness_program",position = "bottom")+scale_y_continuous(position = "left")
g7

g8<-ggplot(dep_data,aes(dep_data$seek_help, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("seek_help",position = "bottom")+scale_y_continuous(position = "left")
g8


g9<-ggplot(dep_data,aes(dep_data$anonymity, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("anonymity",position = "bottom")+scale_y_continuous(position = "left")
g9

g10<-ggplot(dep_data,aes(dep_data$mental_health_consequence, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("mental_health_consequence",position = "bottom")+scale_y_continuous(position = "left")
g10

g10<-ggplot(dep_data,aes(dep_data$leave, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("Leave",position = "bottom")+scale_y_continuous(position = "left")
g10


g11<-ggplot(dep_data,aes(dep_data$phys_health_consequence, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("physical health consequence",position = "bottom")+scale_y_continuous(position = "left")
g11

g12<-ggplot(dep_data,aes(dep_data$coworkers, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("coworkers",position = "bottom")+scale_y_continuous(position = "left")
g12

g13<-ggplot(dep_data,aes(dep_data$supervisor, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("supervisor",position = "bottom")+scale_y_continuous(position = "left")
g13


g14<-ggplot(dep_data,aes(dep_data$mental_health_interview, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("mental_health_interview",position = "bottom")+scale_y_continuous(position = "left")
g14

g15<-ggplot(dep_data,aes(dep_data$phys_health_interview, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("phys_health_interview",position = "bottom")+scale_y_continuous(position = "left")
g15

g16<-ggplot(dep_data,aes(dep_data$mental_vs_physical, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("mental_vs_physical",position = "bottom")+scale_y_continuous(position = "left")
g16

g17<-ggplot(dep_data,aes(dep_data$obs_consequence, fill = dep_data$treatment))+geom_bar(stat = "count")+scale_x_discrete("obs_consequencel",position = "bottom")+scale_y_continuous(position = "left")
g17



#knn for binary variables


mental_knn <- dep_data %>% dplyr::select(c(family_history,self_employed,remote_work,tech_company,treatment))

set.seed(412)

mental<-sample.split(mental_knn$treatment,SplitRatio = 0.7)
train_m<-mental_knn[mental,-5]
train_t<-mental_knn[mental,]
train_m1<-sample.split(train_t$treatment,SplitRatio = 0.7)
train_1<-train_t[train_m1,-5]
train_1t<-train_t[train_m1,]
valid_1t<-subset(train_t,train_m1==F)
valid_1<-valid_1t[,-5]
train_class<-train_t[train_m1,5]
train_class<-as.factor(train_class$treatment)
test_class<-valid_1t [,5]
test<- subset(mental_knn,mental==F)
test_m<-test[,-5]

trctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 3)
set.seed(123)
knn_fit <- train(treatment ~., data = train_1t, method = "knn",
                 trControl=trctrl,
                 preProcess = c("center", "scale"),
                 tuneLength = 10, prob = TRUE)
knn_fit
plot(knn_fit)



test_pred <- predict(knn_fit, newdata = test_m)
test_pred 
confusionMatrix(test_pred,test$treatment)
test_pred1 <- test_pred[1:376]
test_pred1


#using knn decision



mental_knn <- cbind(lapply(mental_knn[1:4], as.integer),mental_knn[5])
set.seed(412)
colnames(mental_knn)[5] <- "Target"
mental_knn <- cbind(mental_knn[1:4],lapply(mental_knn[5], as.factor))

set.seed(412)
sample.idx <- sample.split(mental_knn$Target, SplitRatio = 0.7)
x <- as.matrix(mental_knn[sample.idx, -5])
y <- mental_knn$Target[sample.idx]
set.seed(123)
tr.idx <- sample.split(y, SplitRatio = 0.7)
x.tr   <- x[tr.idx, ]
x.te   <- x[-tr.idx, ]
y.tr   <- y[tr.idx]
y.te   <- y[-tr.idx]
new.mental_knn <- knnExtract(x.tr, y.tr, x.te, k = 5, folds = 5)
glm <- glmnet(x = new.mental_knn$new.tr, y = y.tr, family = "binomial", lambda = 0)
yhat <- drop(predict(glm, new.mental_knn$new.te, type = "class"))
yhat <- factor(yhat, levels = levels(y.tr))
classLoss(actual = y.te, predicted = yhat)
knnDecision(x.tr, y.tr, x.te, y.te, k = 7)


#knn for other attributes
mental_knn1 <-  dep_data %>% dplyr::select(c(Age,no_employees,benefits,care_options,wellness_program,seek_help,leave,mental_health_consequence,phys_health_consequence,coworkers,supervisor,mental_health_interview,phys_health_interview, mental_vs_physical,obs_consequence,treatment))
set.seed(412)

mental1<-sample.split(mental_knn1$treatment,SplitRatio = 0.7)
train_m1<-mental_knn1[mental1,-16]
train_t1<-mental_knn1[mental1,]
train_m11<-sample.split(train_t1$treatment,SplitRatio = 0.7)
train_11<-train_t1[train_m11,-16]
train_1t1<-train_t1[train_m11,]
valid_1t1<-subset(train_t1,train_m11==F)
valid_11<-valid_1t1[,-16]
train_class1<-train_t1[train_m11,16]
train_class1<-as.factor(train_class1$treatment)
test_class1<-valid_1t1 [,16]
test1<- subset(mental_knn1,mental1==F)
test_m1<-test1[,-16]

trctrl <- trainControl(method = "repeatedcv", number = 10, repeats = 3)
set.seed(123)
knn_fit1 <- train(treatment ~., data = train_1t1, method = "knn",
                 trControl=trctrl,
                 preProcess = c("center", "scale"),
                 tuneLength = 10, prob = TRUE)
knn_fit1
plot(knn_fit1)

test_pred1 <- predict(knn_fit1, newdata = test_m1)
test_pred1
confusionMatrix(test_pred1,test1$treatment)
test_pred11 <- test_pred1[1:376]
test_pred1

