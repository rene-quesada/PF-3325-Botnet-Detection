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
from dataset import dataset

def EDA(top_n_features = 115):
    #read content
    data_obj = dataset('../content')
    EDA_malicious_benign(data_obj,top_n_features)
    EDA_devices(data_obj,top_n_features)
    EDA_attacks(data_obj,top_n_features)

def EDA_malicious_benign(data_obj,top_n_features):
    #load data
    data_obj.load_mal_benign_data()
    #set datasets
    df_malicious = data_obj.get_mal_dataframe()
    df = data_obj.get_benign_dataframe()
    features = data_obj.get_feature_list(top_n_features)
    df = df[list(features)]
    
    # take samples
    x_train, x_opt, x_test = np.split(df.sample(frac=1, random_state=17), [int(1/3*len(df)), int(2/3*len(df))])
    df_benign = pd.DataFrame(x_test, columns=df.columns)
    
    #set labels
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
    #plt.show()
    plt.savefig('./EDA/MI_dir_L3_variance_benign_hist.png')
    
    df_malicious['MI_dir_L3_variance'].hist()
    plt.title('Traffic from host weight variance (malicious)',
          fontweight ="bold")
    #plt.show()
    plt.savefig('./EDA/MI_dir_L3_variance_malicious_hist.png')
    
    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host; 
    df_benign['HH_L3_covariance'].hist()
    plt.title('Traffic from host to host weight covariance (benign)',
          fontweight ="bold")
    #plt.show()
    plt.savefig('./EDA/HH_L3_covariance_benign_hist.png')
    
    df_malicious['HH_L3_covariance'].hist()
    plt.title('Traffic from host to host weight covariance (malicious)',
          fontweight ="bold")
    #plt.show()
    plt.savefig('./EDA/HH_L3_covariance_malicious_hist.png')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host
    df_benign['HH_jit_L3_variance'].hist()
    plt.title('Traffic from host to host jitter weight variance (benign)',
          fontweight ="bold")
    #plt.show()
    plt.savefig('./EDA/HH_jit_L3_variance_benign_hist.png')
    
    df_malicious['HH_jit_L3_variance'].hist()
    plt.title('Traffic from host to host jitter weight covariance (malicious)',
          fontweight ="bold")
    #plt.show()
    plt.savefig('./EDA/HH_jit_L3_variance_malicious_hist.png')

    #HpHp stats, which summarizes the recent traffic going from this packet's host+port (IP)
    df_benign['HpHp_L3_covariance'].hist()
    plt.title('Traffic from host port to host port weight covariance (benign)',
          fontweight ="bold")
    #plt.show()
    plt.savefig('./EDA/HpHp_L3_covariance_benign_hist.png')
    
    df_malicious['HpHp_L3_covariance'].hist()
    plt.title('Traffic from host port to host port weight covariance (malicious)',
          fontweight ="bold")
    #plt.show()
    plt.savefig('./EDA/HpHp_L3_covariance_malicious_hist.png')

    df_correlation = pd.DataFrame()
    df_correlation = df_benign[['MI_dir_L3_weight','H_L3_weight','HH_L3_weight','HH_jit_L3_weight','HpHp_L3_weight']]
    #corrmax = df_correlation.corr()
    fig, ax = plt.subplots()
    sns.heatmap(df_correlation.corr(method='pearson'), annot=True, fmt='.4f', 
            cmap=plt.get_cmap('coolwarm'), cbar=False, ax=ax)
    #ax.set_yticklabels(ax.get_yticklabels(), rotation="horizontal")
    #plt.show()
    plt.savefig('./EDA/correlation_benign.png')

    df_correlation2 = pd.DataFrame()
    df_correlation2 = df_malicious[['MI_dir_L3_weight','H_L3_weight','HH_L3_weight','HH_jit_L3_weight','HpHp_L3_weight']]
    sns.heatmap(df_correlation2.corr(method='pearson'), annot=True, fmt='.4f', 
            cmap=plt.get_cmap('coolwarm'), cbar=False, ax=ax)
    #fig.show()
    fig.savefig('./EDA/correlation_malicious.png')

# Plotter for devices
def plot_correlation_matrix(df, title):
    graphWidth = 25
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {title}', fontsize=15)
    plt.savefig('./EDA/HpHp_' + title +'_correlation.png')
    plt.close()

def EDA_devices(data_obj,top_n_features):
    print("Creating EDA for all devices")
    dn_nbaiot = data_obj.get_device_list()
    for device_name in (dn_nbaiot):
        df_mal = data_obj.get_nbaiot_device_mal_data(device_name)
        df_mal = df_mal[df_mal.columns[df_mal.columns.str.startswith('HpHp_')]]
        df = data_obj.get_nbaiot_device_benign_data(device_name)
        features = data_obj.get_feature_list(top_n_features)
        df = df[list(features)]
        df = df[df.columns[df.columns.str.startswith('HpHp_')]]
        # take samples
        x_train, x_opt, x_test = np.split(df.sample(frac=1, random_state=1), [int(1/3*len(df)), int(2/3*len(df))])
        df_benign = pd.DataFrame(x_test, columns=df.columns)
        df_mal = df_mal.sample(n=df_benign.shape[0], random_state=1)
        #we now have the final dataset with labels
        df = pd.concat([df_benign,df_mal])
        #print head
        #df.head()
        print(device_name + " malicious data description")
        print(df_mal.describe(include = 'all'))

        print(device_name + " benign data description")
        print(df_benign.describe(include = 'all'))
        plot_correlation_matrix(df, device_name)


def EDA_attacks(data_obj,top_n_features):
    #load data
    data_obj.load_mal_benign_data()
    print("Creating EDA for types of attacks")

    #set datasets
    df_mirai = data_obj.get_mirai_dataframe()
    df_gafgyt = data_obj.get_gafgyt_dataframe()
    df = data_obj.get_benign_dataframe()
    features = data_obj.get_feature_list(top_n_features)
    df = df[list(features)]

    # take samples
    x_train, x_opt, x_test = np.split(df.sample(frac=1, random_state=17), [int(1/3*len(df)), int(2/3*len(df))])
    df_benign = pd.DataFrame(x_test, columns=df.columns)  
    df_mirai = df_mirai.sample(n=df_benign.shape[0], random_state=17)[list(features)]
    df_gafgyt = df_gafgyt.sample(n=df_benign.shape[0], random_state=17)[list(features)]

    #print head
    #df.head()
    print("benign data description")
    print(df.describe(include = 'all'))

    print("Mirai data description")
    print(df_mirai.describe(include = 'all'))


    print("baschlite data description")
    print(df_gafgyt.describe(include = 'all'))

    #lets get some histograms
    print("Histograms for time frame of 500ms")

    #MI which summarizes the recent traffic from this packet's host (IP + MAC)
    ax= df_mirai['MI_dir_L3_variance'].plot.hist()
    ax.set_title('Traffic from host weight variance (mirai)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/MI_dir_L3_variance_mirai_hist.png')


    #MI which summarizes the recent traffic from this packet's host (IP + MAC)
    ax = df_gafgyt['MI_dir_L3_variance'].plot.hist()
    ax.set_title('Traffic from host weight variance (gafgyt)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/MI_dir_L3_variance_gafgyt_hist.png')


    #MI which summarizes the recent traffic from this packet's host (IP + MAC)
    ax = df_mirai['MI_dir_L3_weight'].plot.hist()
    ax.set_title('Traffic from host weight (mirai)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/MI_dir_L3_weight_mirai_hist.png')
    
    #MI which summarizes the recent traffic from this packet's host (IP + MAC)
    ax = df_gafgyt['MI_dir_L3_weight'].plot.hist()
    ax.set_title('Traffic from host weight (gafgyt)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/MI_dir_L3_weight_gafgyt_hist.png')
    
    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host;    
    ax = df_mirai['HH_L3_covariance'].plot.hist()
    ax.set_title('Traffic from host to host weight covariance (mirai)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HH_L3_covariance_mirai_hist.png')

    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host;    
    ax = df_gafgyt['HH_L3_covariance'].plot.hist()
    ax.set_title('Traffic from host to host weight covariance (gafgyt)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HH_L3_covariance_gafgyt_hist.png')

    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host;    
    ax = df_mirai['HH_L3_weight'].plot.hist()
    ax.set_title('Traffic from host to host weight (mirai)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HH_L3_weight_mirai_hist.png')

    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host;    
    ax = df_gafgyt['HH_L3_weight'].plot.hist()
    ax.set_title('Traffic from host to host weight (gafgyt)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HH_L3_weight_gafgyt_hist.png')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host    
    ax = df_mirai['HH_jit_L3_variance'].plot.hist()
    ax.set_title('Traffic from host to host jitter weight covariance (mirai)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HH_jit_L3_variance_mirai_hist.png')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host    
    ax = df_gafgyt['HH_jit_L3_variance'].plot.hist()
    ax.set_title('Traffic from host to host jitter weight covariance (gafgyt)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HH_jit_L3_variance_gafgyt_hist.png')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host    
    ax = df_mirai['HH_jit_L3_weight'].plot.hist()
    ax.set_title('Traffic from host to host jitter weight (mirai)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HH_jit_L3_weight_mirai_hist.png')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host    
    ax = df_gafgyt['HH_jit_L3_weight'].plot.hist()
    ax.set_title('Traffic from host to host jitter weight covariance (gafgyt)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HH_jit_L3_weight_gafgyt_hist.png')

    #HpHp stats, which summarizes the recent traffic going from this packet's host+port (IP)
    ax = df_mirai['HpHp_L3_covariance'].plot.hist()
    ax.set_title('Traffic from host port to host port weight covariance (malicious)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HpHp_L3_covariance_mirai_hist.png')

    ax = df_gafgyt['HpHp_L3_covariance'].plot.hist()
    ax.set_title('Traffic from host port to host port weight covariance (malicious)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HpHp_L3_covariance_gafgyt_hist.png')

    #HpHp stats, which summarizes the recent traffic going from this packet's host+port (IP)
    ax = df_mirai['HpHp_L3_weight'].plot.hist()
    ax.set_title('Traffic from host port to host port weight (malicious)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HpHp_L3_weight_mirai_hist.png')

    ax = df_gafgyt['HpHp_L3_weight'].plot.hist()
    ax.set_title('Traffic from host port to host port weight (malicious)',
          fontweight ="bold")
    #plt.show()
    ax.figure.savefig('./EDA/HpHp_L3_weight_gafgyt_hist.png')

    df_correlation = pd.DataFrame()
    df_correlation = df_mirai[['MI_dir_L3_weight','H_L3_weight','HH_L3_weight','HH_jit_L3_weight','HpHp_L3_weight']]
    #corrmax = df_correlation.corr()
    fig, ax = plt.subplots()
    sns.heatmap(df_correlation.corr(method='pearson'), annot=True, fmt='.4f', 
            cmap=plt.get_cmap('coolwarm'), cbar=False, ax=ax)
    #ax.set_yticklabels(ax.get_yticklabels(), rotation="horizontal")
    #plt.show()
    plt.savefig('./EDA/correlation_mirai.png')

    df_correlation2 = pd.DataFrame()
    df_correlation2 = df_gafgyt[['MI_dir_L3_weight','H_L3_weight','HH_L3_weight','HH_jit_L3_weight','HpHp_L3_weight']]
    sns.heatmap(df_correlation2.corr(method='pearson'), annot=True, fmt='.4f', 
            cmap=plt.get_cmap('coolwarm'), cbar=False, ax=ax)
    #fig.show()
    fig.savefig('./EDA/correlation_gafgyt.png')


    #keeep all host to host flows
    df_hist = df_gafgyt[df_gafgyt.columns[df_gafgyt.columns.str.startswith('HpHp_')]]
    ax = df_hist.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);
    #ax.set_title('Host to host Baschlite histogram')
    #ax.figure.savefig('./EDA/HpHp_gafgyt_hist.png')

    #keeep all host to host flows
    df_hist = df_mirai[df_mirai.columns[df_mirai.columns.str.startswith('HpHp_')]]
    ax = df_hist.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);
    #ax.set_title('Host to host Mirai histogram')
    #ax.figure.savefig('./EDA/HpHp_mirai_hist.png')

if __name__ == '__main__':
    EDA(*sys.argv[1:])