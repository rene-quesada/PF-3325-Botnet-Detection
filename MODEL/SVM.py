# import SVC classifier
import sys
from dataset import dataset
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd
import numpy as np
from collections import Counter

# import metrics to compute accuracy
from sklearn.metrics import accuracy_score
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train(top_n_features = None):
    #read content
    data_obj = dataset('../content')
    train_with_data(top_n_features, data_obj)

def train_with_data(top_n_features, data_obj):
    #load data
    #data_obj.load_mal_benign_data()
    #set datasets
    #df_malicious = data_obj.get_mal_dataframe()
    #df_benign = data_obj.get_benign_dataframe()

    #get dataset from a single device to reduce set
    dn_nbaiot = data_obj.get_device_list()
    
    #get malicious
    df_mal = data_obj.get_nbaiot_device_mal_data(dn_nbaiot[2])

    #get benign
    df_benign = data_obj.get_nbaiot_device_benign_data(dn_nbaiot[2])
    #features = data_obj.get_feature_list(top_n_features)
    #df_benign = df[list(features)]

    #filter for time windows
    # df_benign = df_benign[df_benign.columns[df_benign.columns.str.contains('_L5_')]]
    # df_mal = df_mal[df_mal.columns[df_mal.columns.str.contains('_L5_')]]

    #Sample to 

    #add labels
    df_benign['malicious'] = 0
    df_mal['malicious'] = 1
    
    #Sample for testing
    df_benign = df_benign.sample(n=30000,random_state=17)
    df_mal = df_mal.sample(n=30000,random_state=17)
    
    df = df_benign.append(df_mal)

    #setup data for training
    Y = df['malicious']
    X = df.drop(columns=['malicious'])
    #Y = pd.get_dummies(df['malicious'])
    #Y = Y.drop(columns=['malicious'])
    #Split data have 20 % for validation
    #X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
    ''' instead of nu you can use this one
    # identify outliers in the training dataset
    ocs = OneClassSVM(nu=0.01)
    yhat = ocs.fit_predict(X_train)

    # select all rows that are not outliers
    mask = yhat != -1
    X_train, y_train = X_train[mask, :], y_train[mask]

    '''
    print('The number of records in the training dataset is', X_train.shape[0])
    print('The number of records in the test dataset is', X_test.shape[0])
    print(f"The training dataset has {sorted(Counter(y_train).items())[0][1]} records for the majority class and {sorted(Counter(y_train).items())[1][1]} records for the minority class.")

    one_class_svm = OneClassSVM(nu=0.01, kernel = 'rbf', gamma = 'auto').fit(X_train)
    prediction = one_class_svm.predict(X_test)
    # Change the anomalies' values to make it consistent with the true values
    prediction = [1 if i==-1 else 0 for i in prediction]
    # Check the model performance
    print(classification_report(y_test, prediction))
    
    # Get the scores for the testing dataset
    score = one_class_svm.score_samples(X_test)
    # Check the score for 2% of outliers
    score_threshold = np.percentile(score, 2)
    print(f'The customized score threshold for 2% of outliers is {score_threshold:.2f}')
    # Check the model performance at 2% threshold
    customized_prediction = [1 if i < score_threshold else 0 for i in score]
    # # Check the prediction performance
    print(classification_report(y_test, customized_prediction))
    #evaluate_model(X_train, X_test, y_train, one_class_svm)

  

def evaluation_one_class(preds_interest, preds_outliers):
  y_true = [1]*len(preds_interest) + [-1]*len(preds_outliers)
  y_pred = list(preds_interest)+list(preds_outliers)
  return classification_report(y_true, y_pred, output_dict=False)

def evaluate_model(X_train, X_test, X_outlier, model):
  
  one_class_classifier = model.fit(X_train)

  Y_pred_interest = one_class_classifier.predict(X_test)
  
  Y_pred_ruido = one_class_classifier.predict(X_outlier)

  print(evaluation_one_class(Y_pred_interest, Y_pred_ruido))


if __name__ == '__main__':
    train(*sys.argv[1:])
