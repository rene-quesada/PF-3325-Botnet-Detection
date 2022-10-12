import sys
import pandas as pd
import numpy as np
import random
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from glob import iglob
from sklearn.metrics import recall_score, accuracy_score, precision_score, confusion_matrix
import matplotlib.pyplot as plt

#Load mirai and gaf attacks
def load_mal_data():
    df_mirai = pd.DataFrame()
    df_gafgyt = pd.DataFrame()
    df_mirai = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob('./content/**/mirai_attacks/*.csv.bz2', recursive=True)), ignore_index=True)
    df_gafgyt = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob('./content/**/gafgyt_attacks/*.csv.bz2', recursive=True)), ignore_index=True)   
    return pd.concat([df_mirai, df_gafgyt])


def EDA(top_n_features = 115):
    EDA_with_data(top_n_features, load_mal_data())

def EDA_with_data(top_n_features, df_malicious):

    # obtain benign content
    df = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob('./content/**/benign_traffic.csv.bz2', recursive=True)), ignore_index=True)
    #get the list of features
    fisher = pd.read_csv('./content/features.csv')
    features = fisher.iloc[0:int(top_n_features)]['Feature'].values
    df = df[list(features)]
    
    # take samples
    x_test = np.split(df.sample(frac=1, random_state=17), [int(1/3*len(df)), int(2/3*len(df))])
    df_benign = pd.DataFrame(x_test, columns=df.columns)
    df_benign['malicious'] = 0
    df_malicious = df_malicious.sample(n=df_benign.shape[0], random_state=17)[list(features)]
    df_malicious['malicious'] = 1

    #we now have the final dataset with labels
    df = pd.concat([df_benign,df_malicious])

    #print head
    df.head()
    df.describe()

    #lets get some histograms
    print("all data")
    df['MI_dir_L5_variance'].hist()
    plt.savefig('./MI_dir_L5_variance_hist.pdf')
    df['MI_dir_L3_variance'].hist()
    plt.savefig('./MI_dir_L3_variance.pdf')
    df['MI_dir_L1_variance'].hist()
    plt.savefig('./MI_dir_L1_variance.pdf')
    df['MI_dir_L0.1_variance'].hist()
    plt.savefig('./MI_dir_L0.1_variance.pdf')
    df['MI_dir_L0.01_variance'].hist()
    plt.savefig('./MI_dir_L0.01_variance.pdf')
    df['H_L1_variance'].hist()
    plt.savefig('./H_L1_variance.pdf')
    df['HH_L1_covariance'].hist()
    plt.savefig('./HH_L1_covariance.pdf')
    df['HpHp_L1_covariance'].hist()
    plt.savefig('./HpHp_L1_covariance.pdf')



if __name__ == '__main__':
    EDA(*sys.argv[1:])