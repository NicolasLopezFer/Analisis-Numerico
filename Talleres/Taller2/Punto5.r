library(pracma)
library(Matrix)

beta = 0
alpha = 2

a = matrix(c(2, 0, 1,
             beta,2 , -1,
             -1, 1, alpha), nrow=3, byrow=TRUE)
b = matrix (c(1,2,1),nrow=3, byrow=TRUE)


resultado = cbind(a,b)

print (resultado)