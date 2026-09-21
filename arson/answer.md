### Section A
#### Q1:

a) if the model predicts 0 for every applicant means acc to the model prediction every applicant is not defaulter. so our model is performing very poorly. as our target distribution is bout 92 and 8. 
b) 
c) because accuracy matters.

#### Q2: 
-> we use stratify = y to get equal percent of our target distribution in our train test. equal proportation. 

### Q3:
1) Training set: it is part of our data, where we train our model, 

2) validation/development data:  Validation data is something 

3) final test data: it is dataset where we test the accuracy of our model. 

#### Q4:
-> median will be same for the entire numerical col, it hardly matter whether we take median first or later. 
but this is not a correct approach, as model will peek into test data this.


### Section B:
#### Q5:


#### Q6:
a) high VIF means columns are much very dependent on each, having them in our training model, will only be noise, they wont make any difference. 

b) 

c) High VIF means the model predictive performancce will be poor, because we are giving the columns that high co-related with eacch other.
so our model wont be able to learn the pattern in the dataset.

#### Q7:

because ratio contain how our one column changes with respect to the other column.
so by replacing the highly co-related variables will add more meaningful data for our model to train on.

#### Q8:

a) 365243 days is an outlier (365243 = 1000 years), it is nothing but noise in our data. if we train our model on it, our model will definitely learn wrong pattern. nd perform poorly.

b) 
c) because 18% of applicants has this value, replacing this value with median wont be a good approach for this. 

#### Q9:
-> we created these featured columns, because the age_years was in -ve. and for income, we took log, to scale the value in one range.


### Section C:

#### Q10:
a) p represents the proability of (0 to 1)
b) when z increase to + infty, p value get close to 1.
c) same when z is - infty, p value becomes close 0.

### Section F
#### Q19:
a) higher AUC indicate , better model. (higher the score, better the model predicts)

b) 

Q20: precision and recall represent:
precision: in confusion matrix, out of all the cases model predicted postive, how many were actually postive
recall: out of cases actually postive, how many our model is avble to predict.