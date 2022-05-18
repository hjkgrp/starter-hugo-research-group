require(kernlab) # dependency of CVST and DDR
require(CVST) # library for KRR, loads kernlab
require(DRR)  # library for fast cross validation
require(Metrics) # some useful tools

## load the file prepared in part 1
data <- read.csv("QM9_descriptor_file.csv",header=TRUE,row.names = 1)

## choose number of training points
training_examples <- 4000

## partition the data
train_ind = sample(nrow(data),training_examples)
df_test = data[-train_ind,]
df_train=data[train_ind,]



## normalize data 
df_train <- scale(df_train,center=TRUE,scale=TRUE)
train_center <- attr(df_train, 'scaled:center')
train_scale <- attr(df_train, 'scaled:scale')
df_train <- as.data.frame(df_train)


# unit conversion
HA_to_kcal_mol = 627.5095;



# note: data science best practice, only use training scales!
df_test <- scale(df_test,center = train_center,scale=train_scale)
df_test <- as.data.frame(df_test)


## Load into CVST
x_train <- df_train[,2:ncol(df_train)]
y_train <-  df_train[,'u0']
x_test <- df_test[,2:ncol(df_test)]
y_test <-  df_test[,'u0']
train_data_CVST <-constructData(x=as.matrix(x_train), y=y_train)
test_data_CVST <-constructData(x=as.matrix(x_test), y=y_test)



## set up learners
krr_learner = constructFastKRRLearner()   ## Build the base learner


## first time around, don't do CV but use a reasonable kernel:
params_krr = list(kernel="rbfdot", sigma=1E-6, lambda=1E-11,nblocks=4)


#krr_learner = constructKRRLearner()   ## Build the base learner                                                                                                                                                                                  

#params_CVST_krr = constructParams(kernel = 'rbfdot',sigma=10^(seq(-8,-3,length=5)),lambda=10^(seq(-12,-8,length=4)))


#params_krr$sigma=1e-6
#params_krr$lambda=1E-11

## train model
krr_trained = krr_learner$learn(train_data_CVST, params_krr)
## use model for prediction
test_krr = krr_learner$predict(krr_trained, test_data_CVST)
train_krr = krr_learner$predict(krr_trained, train_data_CVST)
pred_test_y_krr =  as.vector(test_krr*train_scale["u0"] +  train_center["u0"])
pred_train_y_krr = as.vector(train_krr* train_scale["u0"] +  train_center["u0"])

pred_test_y_krr = as.vector(test_krr*train_scale["u0"] + train_center["u0"])
pred_train_y_krr = as.vector(train_krr*train_scale["u0"] + train_center["u0"])

test_target = as.vector(test_data_CVST$y*train_scale["u0"]  +  train_center["u0"])
train_target = as.vector(train_data_CVST$y*train_scale["u0"]  +  train_center["u0"])

## evaluate
train_mse_krr = mse(pred_train_y_krr,train_target)*(HA_to_kcal_mol^2)
test_mse_krr = mse(pred_test_y_krr,test_target)*(HA_to_kcal_mol^2)
train_e_krr =  (pred_train_y_krr - train_target)*HA_to_kcal_mol
test_e_krr =  (pred_test_y_krr - test_target)*HA_to_kcal_mol
print('No CV results')
print(c('krr train rmse = ',sqrt(train_mse_krr),' kcal/mol'))
print(c('krr train MAE = ',mean(abs(train_e_krr)),' kcal/mol'))
print(c('krr test rmse = ',sqrt(test_mse_krr),' kcal/mol'))
print(c('krr test MAE = ',mean(abs(test_e_krr)),' kcal/mol'))




## now, repeat the above using 10-fold cross validaiton 
print('now doing cross validation, standby...')
## set parameters for CV
params_CVST_krr = constructParams(kernel = 'rbfdot',sigma=10^(seq(-8,-4,length=5)),lambda=10^(seq(-12,-8,length=5)),nblocks=4)
## conduct 10-fold CV
CV_ret_krr <-  CV(data= train_data_CVST, learner = krr_learner,params =  params_CVST_krr,fold = 10, verbose = TRUE)

## capture the optimal parameter choices
params_krr <- CV_ret_krr[[1]]



## train model
krr_trained = krr_learner$learn(train_data_CVST, params_krr)
## use model for prediction
test_krr = krr_learner$predict(krr_trained, test_data_CVST)
train_krr = krr_learner$predict(krr_trained, train_data_CVST)
pred_test_y_krr =  as.vector(test_krr*train_scale["u0"] +  train_center["u0"])
pred_train_y_krr = as.vector(train_krr* train_scale["u0"] +  train_center["u0"])

pred_test_y_krr = as.vector(test_krr*train_scale["u0"] + train_center["u0"])
pred_train_y_krr = as.vector(train_krr*train_scale["u0"] + train_center["u0"])

test_target = as.vector(test_data_CVST$y*train_scale["u0"]  +  train_center["u0"])
train_target = as.vector(train_data_CVST$y*train_scale["u0"]  +  train_center["u0"])

## evaluate
train_mse_krr = mse(pred_train_y_krr,train_target)*(HA_to_kcal_mol^2)
test_mse_krr = mse(pred_test_y_krr,test_target)*(HA_to_kcal_mol^2)
train_e_krr =  (pred_train_y_krr - train_target)*HA_to_kcal_mol
test_e_krr =  (pred_test_y_krr - test_target)*HA_to_kcal_mol
print('CV results')
print(c('krr train rmse = ',sqrt(train_mse_krr),' kcal/mol'))
print(c('krr train MAE = ',mean(abs(train_e_krr)),' kcal/mol'))
print(c('krr test rmse = ',sqrt(test_mse_krr),' kcal/mol'))
print(c('krr test MAE = ',mean(abs(test_e_krr)),' kcal/mol'))

