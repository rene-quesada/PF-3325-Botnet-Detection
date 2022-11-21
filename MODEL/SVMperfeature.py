# import SVC classifier
import sys
from dataset import dataset
import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd
import numpy as np
import seaborn as sns

from collections import Counter

# import metrics to compute accuracy
from sklearn.metrics import accuracy_score
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

def train(top_n_features = None):
    #read content
    data_obj = dataset('../content')
    train_with_data(top_n_features, data_obj)

def train_with_data(top_n_features, data_obj):

    original_stdout = sys.stdout # Save a reference to the original standard output

    #load data
    #data_obj.load_mal_benign_data()
    #set datasets
    #all data
    #df_malicious = data_obj.get_mal_dataframe()
    #df_benign = data_obj.get_benign_dataframe()

    #get dataset from a single device to reduce set
    dn_nbaiot = data_obj.get_device_list()
    
    #get malicious
    #using cameras
    df_mal = data_obj.get_nbaiot_device_mal_data(dn_nbaiot[4])
    df_mal = df_mal.append(data_obj.get_nbaiot_device_mal_data(dn_nbaiot[5]))
    #get benign
    df_benign = data_obj.get_nbaiot_device_benign_data(dn_nbaiot[4])
    df_benign = df_benign.append(data_obj.get_nbaiot_device_benign_data(dn_nbaiot[5]))
    #features = data_obj.get_feature_list(top_n_features)
    #df_benign = df[list(features)]

    #Sample for testing
    df_benign = df_benign.sample(n=50000,random_state=17)
    df_mal = df_mal.sample(n=50000,random_state=17)
    #add labels
    df_benign.insert(0,'malicious',0)
    df_mal.insert(0,'malicious',1)

    #unifying the dataframes
    df = df_benign.append(df_mal)

    for column in df:
        if column == 'malicious':
            continue

        #setup data for training
        Y = df['malicious']
        # setting the column
        X = df[column]
        
        #creating the training and test dataset
        X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.20, random_state=42)


        scaler = StandardScaler()
        X_train.shape, X_test.shape
        #Re shape need it when there is a single feature  to have a list of indivual 
        X_train = np.array(X_train).reshape(-1, 1)
        X_test = np.array(X_test).reshape(-1, 1)

        #transform to normalize values
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        #name for result
        result_name = 'MODEL/output/SVM_' + column
        results_path_png = result_name + '.png'
        results_path_txt = result_name + '.txt'
        
        with open(results_path_txt, 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print('The number of records in the training dataset is', X_train.shape[0])
            print('The number of records in the test dataset is', X_test.shape[0])
            print(f"The training dataset has {sorted(Counter(y_train).items())[0][1]} records for the majority class and {sorted(Counter(y_train).items())[1][1]} records for the minority class.")
            sys.stdout = original_stdout # Reset the standard output to its original value

        #create SVC model
        svc=SVC(C=100.0, kernel = 'rbf',gamma= 0.1) 
        
        #train the model
        svc.fit(X_train,y_train)

        prediction = svc.predict(X_test)

        # compute and print accuracy score
        with open(results_path_txt, 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print('Model accuracy score with C =  100.0  and gamma 0.1: {0:0.4f}'. format(accuracy_score(y_test, prediction)))
            sys.stdout = original_stdout # Reset the standard output to its original value  

        cm = confusion_matrix(y_test, prediction)

        with open(results_path_txt, 'a') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print('Confusion matrix\n\n', cm)
            print('\nTrue Positives(TP) = ', cm[0,0])
            print('\nTrue Negatives(TN) = ', cm[1,1])
            print('\nFalse Positives(FP) = ', cm[0,1])
            print('\nFalse Negatives(FN) = ', cm[1,0])
            sys.stdout = original_stdout # Reset the standard output to its original value

        cm_matrix = pd.DataFrame(data=cm, columns=['Actual Positive:1', 'Actual Negative:0'], 
                                    index=['Predict Positive:1', 'Predict Negative:0'])

        sns_plot = sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='YlGnBu')

        plt.savefig(results_path_png, dpi=400)
        
        plt.close()
        
        with open(results_path_txt, 'a') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print(classification_report(y_test, prediction))
            sys.stdout = original_stdout # Reset the standard output to its original value    
    

if __name__ == '__main__':
    train(*sys.argv[1:])
