# import SVC classifier
import sys
from dataset import dataset
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd
import numpy as np

# import metrics to compute accuracy
from sklearn.metrics import accuracy_score
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

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
    df_benign = df_benign[df_benign.columns[df_benign.columns.str.contains('_L5_')]]
    df_mal = df_mal[df_mal.columns[df_mal.columns.str.contains('_L5_')]]

    #Sample to 

    #add labels
    df_benign['malicious'] = 0
    df_mal['malicious'] = 1
    
    #Sample for testing
    df_benign = df_benign.sample(n=10000,random_state=17)
    df_mal = df_mal.sample(n=10000,random_state=17)
    
    df = df_benign.append(df_mal)

    #setup data for training
    X = df.drop(columns=['malicious'])
    Y = pd.get_dummies(df['malicious'])

    #Split data
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    ''' instead of nu you can use this one
    # identify outliers in the training dataset
    ocs = OneClassSVM(nu=0.01)
    yhat = ocs.fit_predict(X_train)

    # select all rows that are not outliers
    mask = yhat != -1
    X_train, y_train = X_train[mask, :], y_train[mask]

    '''
    one_class_svm = OneClassSVM(nu=0.01, kernel = 'rbf', gamma = 'auto').fit(X_train)
    one_class_svm.fit(X_train)
    y_pred_train = one_class_svm.predict(X_train)
    y_pred_test = one_class_svm.predict(X_test)
    n_error_train = y_pred_train[y_pred_train == -1].size
    n_error_test = y_pred_test[y_pred_test == -1].size
    s = 40
    b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c="white", s=s, edgecolors="k")
    b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c="blueviolet", s=s, edgecolors="k")
    plt.axis("tight")
    plt.xlim((-5, 5))
    plt.ylim((-5, 5))
    plt.legend(
        [a.collections[0], b1, b2],
        [
            "learned frontier",
            "training observations",
            "new regular observations",
        ],
        loc="upper left",
        prop=matplotlib.font_manager.FontProperties(size=11),
    )
    plt.xlabel(
        "error train: %d/200 ; errors novel regular: %d/40"
        % (n_error_train, n_error_test)
    )
    plt.show()
if __name__ == '__main__':
    train(*sys.argv[1:])
