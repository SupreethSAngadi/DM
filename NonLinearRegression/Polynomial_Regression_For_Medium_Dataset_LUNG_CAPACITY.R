summary(LungCapData2)

library(ggplot2)

ggplot()+
  geom_point(aes(x=LungCapData2$Height, y=LungCapData2$LungCap), color='red')+
  ggtitle('Lung Cap Vs. Height')+
  xlab('Height')+
  ylab('LungCap')

linear_regressor = lm(LungCapData2$LungCap ~ LungCapData2$Height)
linear_regressor
summary(linear_regressor)

#plot(linear_regressor)

ggplot()+
  geom_point(aes(x=LungCapData2$Height, y=LungCapData2$LungCap), color='red')+
  geom_line(aes(x=LungCapData2$Height, y=predict(linear_regressor)), color='darkgreen',lwd=1)+
  ggtitle('Lung Cap Vs. Height')+
  xlab('Height')+
  ylab('LungCap')

quad_regressor = lm(LungCapData2$LungCap ~ poly(LungCapData2$Height, degree = 2, raw = T))
quad_regressor
summary(quad_regressor)

#plot(quad_regressor)

ggplot()+
  geom_point(aes(x=LungCapData2$Height, y=LungCapData2$LungCap), color='red')+
  geom_line(aes(x=LungCapData2$Height, y=predict(linear_regressor), color = "Linear"), lwd=1)+
  geom_line(aes(x=LungCapData2$Height, y=predict(quad_regressor), color = "Quad"), lwd=1)+
  scale_color_manual("", breaks = c("Linear", "Quad"),values = c("Linear"="darkgreen", "Quad"="purple"))+
  ggtitle('Lung Cap Vs. Height')+
  xlab('Height')+
  ylab('LungCap')

cube_regressor = lm(LungCapData2$LungCap ~ poly(LungCapData2$Height, degree = 3, raw = T))
cube_regressor
summary(cube_regressor)

ggplot()+
  geom_point(aes(x=LungCapData2$Height, y=LungCapData2$LungCap), color='red')+
  geom_line(aes(x=LungCapData2$Height, y=predict(linear_regressor), color = "Linear"),lwd=1)+
  geom_line(aes(x=LungCapData2$Height, y=predict(quad_regressor), color = "Quad"), lwd=1)+
  geom_line(aes(x=LungCapData2$Height, y=predict(cube_regressor), color = "Cube"), lwd=1)+
  scale_color_manual("", breaks = c("Linear", "Quad", "Cube"),values = c("Linear"="darkgreen", "Quad"="purple", "Cube"="cyan"))+
  ggtitle('Lung Cap Vs. Height')+
  xlab('Height')+
  ylab('LungCap')

anova(quad_regressor,cube_regressor)

#deg4_regressor = lm(LungCapData2$LungCap ~ poly(LungCapData2$Height, degree = 4, raw = T))
#deg4_regressor
#summary(deg4_regressor)

#ggplot()+
#  geom_point(aes(x=LungCapData2$Height, y=LungCapData2$LungCap), color='red')+
#  geom_line(aes(x=LungCapData2$Height, y=predict(linear_regressor), color = "Linear"),lwd=1)+
#  geom_line(aes(x=LungCapData2$Height, y=predict(quad_regressor), color = "Quad"), lwd=1)+
#  geom_line(aes(x=LungCapData2$Height, y=predict(cube_regressor), color = "Cube"), lwd=1)+
#  geom_line(aes(x=LungCapData2$Height, y=predict(deg4_regressor), color = "Degree4"), lwd=1)+
#  scale_color_manual("", breaks = c("Linear", "Quad", "Cube", "Degree4"),values = c("Linear"="darkgreen", "Quad"="purple", "Cube"="cyan", "Degree4"="Magenta"))+
#  ggtitle('Lung Cap Vs. Height')+
#  xlab('Height')+
#  ylab('LungCap')

library(caTools)

 #set.seed(47)
split <- sample.split(LungCapData2$LungCap, SplitRatio = 0.8)
split
training_set <- subset(LungCapData2,split==T)
training_set
testing_set <- subset(LungCapData2,split==F)
testing_set


poly_regressor = lm(formula = LungCap ~ poly(Height, degree = 2, raw = T), data = training_set)
poly_regressor
summary(poly_regressor)


ggplot()+
  geom_point(aes(x=training_set$Height,y=training_set$LungCap),color='red')+
  geom_line(aes(x=training_set$Height,y=predict(poly_regressor,newdata = training_set)),color='blue', lwd=1)+
  ggtitle('LungCap vs Height(trainingset)')+
  xlab('Height')+
  ylab('LungCap')

ggplot()+
  geom_point(aes(x=testing_set$Height,y=testing_set$LungCap),color='green')+
  geom_line(aes(x=training_set$Height,y=predict(poly_regressor,newdata = training_set)),color='blue',lwd=1)+
  ggtitle('LungCap vs Height(testingset)')+
  xlab('Height')+
  ylab('LungCap')

