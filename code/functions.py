from sklearn import metrics
from sklearn.model_selection import cross_val_score
import numpy as np

def calc_metrics(true, pred):
    return print ('RMSE '+ str(np.sqrt(metrics.mean_squared_error(true, pred))) + '\n' +
                  'MSE  ' + str(metrics.mean_squared_error (true, pred)) + '\n' +
                  'R2   ' + str(metrics.r2_score (true, pred)) + '\n' +
                  'MAE  ' + str(metrics.mean_absolute_error(true, pred)))

def calc_scores(model, X_train, y_train, X_test, y_test):
    return print ('Train score  ' + str(model.score (X_train, y_train))  + '\n' +
                  'Test score   ' + str(model.score (X_test, y_test)) + '\n' +
                  'Baseline     ' + str(cross_val_score (model, X_train, y_train).mean()))

def ren_col(columns):
    columns = [col.lower() for col in columns]
    columns = [col.replace(' ','_') for col in columns]
    return columns
