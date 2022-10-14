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
import seaborn as sns

#Load mirai and gaf attacks
def load_mal_data():
    df_mirai = pd.DataFrame()
    df_gafgyt = pd.DataFrame()
    df_mirai = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob('../content/**/mirai_attacks/*.csv.bz2', recursive=True)), ignore_index=True)
    df_gafgyt = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob('../content/**/gafgyt_attacks/*.csv.bz2', recursive=True)), ignore_index=True)   
    return pd.concat([df_mirai, df_gafgyt])


def EDA(top_n_features = 115):
    EDA_with_data(top_n_features, load_mal_data())

def EDA_with_data(top_n_features, df_malicious):

    # obtain benign content
    df = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob('../content/**/benign_traffic.csv.bz2', recursive=True)), ignore_index=True)
    #get the list of features
    fisher = pd.read_csv('../content/features.csv')
    features = fisher.iloc[0:int(top_n_features)]['Feature'].values
    df = df[list(features)]
    
    # take samples
    x_train, x_opt, x_test = np.split(df.sample(frac=1, random_state=17), [int(1/3*len(df)), int(2/3*len(df))])
    df_benign = pd.DataFrame(x_test, columns=df.columns)
    df_benign['malicious'] = 0
    df_malicious = df_malicious.sample(n=df_benign.shape[0], random_state=17)[list(features)]
    df_malicious['malicious'] = 1

    #we now have the final dataset with labels
    df = pd.concat([df_benign,df_malicious])

    #print head
    #df.head()
    df.describe()

    #lets get some histograms
    print("Histograms for time frame of 500ms")

    #MI which summarizes the recent traffic from this packet's host (IP + MAC)
    df_benign['MI_dir_L3_variance'].hist()
    plt.title('Traffic from host weight variance (benign)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./MI_dir_L3_variance_benign_hist.pdf')
    
    df_malicious['MI_dir_L3_variance'].hist()
    plt.title('Traffic from host weight variance (malicious)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./MI_dir_L3_variance_malicious_hist.pdf')
    
    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host; 
    df_benign['HH_L3_covariance'].hist()
    plt.title('Traffic from host to host weight covariance (benign)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./HH_L3_covariance_benign_hist.pdf')
    
    df_malicious['HH_L3_covariance'].hist()
    plt.title('Traffic from host to host weight covariance (malicious)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./HH_L3_covariance_malicious_hist.pdf')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host
    df_benign['HH_jit_L3_variance'].hist()
    plt.title('Traffic from host to host jitter weight variance (benign)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./HH_jit_L3_variance_benign_hist.pdf')
    
    df_malicious['HH_jit_L3_variance'].hist()
    plt.title('Traffic from host to host jitter weight covariance (malicious)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./HH_jit_L3_variance_malicious_hist.pdf')

    #HpHp stats, which summarizes the recent traffic going from this packet's host+port (IP)
    df_benign['HpHp_L3_covariance'].hist()
    plt.title('Traffic from host port to host port weight covariance (benign)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./HpHp_L3_covariance_benign_hist.pdf')
    
    df_malicious['HpHp_L3_covariance'].hist()
    plt.title('Traffic from host port to host port weight covariance (malicious)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./HpHp_L3_covariance_malicious_hist.pdf')

    df_correlation = pd.DataFrame()
    df_correlation = df_benign[['MI_dir_L3_weight','H_L3_weight','HH_L3_weight','HH_jit_L3_weight','HpHp_L3_weight']]
    #corrmax = df_correlation.corr()
    ax2, ax = plt.subplots()
    sns.heatmap(df_correlation.corr(method='pearson'), annot=True, fmt='.4f', 
            cmap=plt.get_cmap('coolwarm'), cbar=False, ax=ax)
    #ax.set_yticklabels(ax.get_yticklabels(), rotation="horizontal")
    plt.title('Correlation between different flow weight (benign)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./correlation_benign.pdf')

    df_correlation2 = pd.DataFrame()
    df_correlation2 = df_malicious[['MI_dir_L3_weight','H_L3_weight','HH_L3_weight','HH_jit_L3_weight','HpHp_L3_weight']]
    sns.heatmap(df_correlation2.corr(method='pearson'), annot=True, fmt='.4f', 
            cmap=plt.get_cmap('coolwarm'), cbar=False, ax=ax)
    plt.title('Correlation between different flow weight (malicious)',
          fontweight ="bold")
    plt.show()
    plt.savefig('./correlation_malicious.pdf')

if __name__ == '__main__':
    EDA(*sys.argv[1:])