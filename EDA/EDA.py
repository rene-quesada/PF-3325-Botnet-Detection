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

# Plotter for devices
def plot_correlation_matrix(df, title):
    graphWidth = 30
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=200, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90,fontsize=9)
    plt.yticks(range(len(corr.columns)), corr.columns,fontsize=9)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {title}', fontsize=14)
    plt.autoscale()
    plt.savefig('./EDA/HpHp_' + title +'_correlation.png',bbox_inches='tight')
    plt.close()


# Plotter for devices
def plot_hist(df, title,filename):
    df.hist()
    plt.title(f'{title}', fontsize=14)
    plt.autoscale()
    plt.savefig(filename,bbox_inches='tight')
    plt.close()

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
    plot_hist(df_benign['MI_dir_L3_variance'],'Traffic from host weight variance (benign)','./EDA/MI_dir_L3_variance_benign_hist.png')
    plot_hist(df_malicious['MI_dir_L3_variance'],'Traffic from host weight variance (malicious)','./EDA/MI_dir_L3_variance_malicious_hist.png')
    
    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host; 
    plot_hist(df_benign['HH_L3_covariance'],'Traffic from host to host weight covariance (benign)','./EDA/HH_L3_covariance_benign_hist.png')
    plot_hist(df_malicious['HH_L3_covariance'],'Traffic from host weight variance (malicious)','./EDA/HH_L3_covariance_malicious_hist.png')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host
    plot_hist(df_benign['HH_jit_L3_variance'],'Traffic from host to host jitter weight variance (benign)','./EDA/HH_jit_L3_variance_benign_hist.png')
    plot_hist(df_malicious['HH_jit_L3_variance'],'Traffic from host to host jitter weight covariance (malicious)','./EDA/HH_jit_L3_variance_malicious_hist.png')


    #HpHp stats, which summarizes the recent traffic going from this packet's host+port (IP)
    plot_hist(df_benign['HpHp_L3_covariance'],'Traffic from host port to host port weight covariance (benign)','./EDA/HpHp_L3_covariance_benign_hist.png')
    plot_hist(df_malicious['HpHp_L3_covariance'],'Traffic from host port to host port weight covariance (malicious)','./EDA/HpHp_L3_covariance_malicious_hist.png')

    df_hist = df_malicious[df_malicious.columns[df_malicious.columns.str.startswith('HpHp_')]]
    plot_correlation_matrix(df_hist, 'malicious')
    
    df_benign = df_benign[df_benign.columns[df_benign.columns.str.startswith('HpHp_')]]
    plot_correlation_matrix(df_hist, 'benign')



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
    plot_hist(df_mirai['MI_dir_L3_variance'],'Traffic from host weight variance (mirai)','./EDA/MI_dir_L3_variance_mirai_hist.png')
    plot_hist(df_gafgyt['MI_dir_L3_variance'],'Traffic from host weight variance (gafgyt)','./EDA/MI_dir_L3_variance_gafgyt_hist.png')

    #MI which summarizes the recent traffic from this packet's host (IP + MAC)
    plot_hist(df_mirai['MI_dir_L3_weight'],'Traffic from host weight (mirai)','./EDA/MI_dir_L3_weight_mirai_hist.png')
    plot_hist(df_gafgyt['MI_dir_L3_weight'],'Traffic from host weight (gafgyt)','./EDA/MI_dir_L3_weight_gafgyt_hist.png')
    
    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host;    
    plot_hist(df_mirai['HH_L3_covariance'],'Traffic from host to host weight covariance (mirai)','./EDA/HH_L3_covariance_mirai_hist.png')
    plot_hist(df_gafgyt['HH_L3_covariance'],'Traffic from host to host weight covariance (gafgyt)','./EDA/HH_L3_covariance_gafgyt_hist.png')

    #HH summarizes the recent traffic going from this packet's host (IP) to the packet's destination host;   
    plot_hist(df_mirai['HH_L3_weight'],'Traffic from host to host weight (mirai)','./EDA/HH_L3_weight_mirai_hist.png')
    plot_hist(df_gafgyt['HH_L3_weight'],'Traffic from host to host weight (gafgyt)','./EDA/HH_L3_weight_gafgyt_hist.png')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host    
    plot_hist(df_mirai['HH_jit_L3_variance'],'Traffic from host to host jitter weight covariance (mirai)','./EDA/HH_jit_L3_variance_mirai_hist.png')
    plot_hist(df_gafgyt['HH_jit_L3_variance'],'Traffic from host to host jitter weight covariance (gafgyt)','./EDA/HH_jit_L3_variance_gafgyt_hist.png')

    #HH_jit stats, which summarizes the jitter of the traffic going from this packet's host (IP) to the packet's destination host  
    plot_hist(df_mirai['HH_jit_L3_weight'],'Traffic from host to host jitter weight  (mirai)','./EDA/HH_jit_L3_weight_mirai_hist.png')
    plot_hist(df_gafgyt['HH_jit_L3_weight'],'Traffic from host to host jitter weight  (gafgyt)','./EDA/HH_jit_L3_weight_gafgyt_hist.png')

    #HpHp stats, which summarizes the recent traffic going from this packet's host+port (IP)
    plot_hist(df_mirai['HpHp_L3_covariance'],'Traffic from host port to host port weight covariance (mirai)','./EDA/HpHp_L3_covariance_mirai_hist.png')
    plot_hist(df_gafgyt['HpHp_L3_covariance'],'Traffic from host port to host port weight covariance(gafgyt)','./EDA/HpHp_L3_covariance_gafgyt_hist.png')

    #HpHp stats, which summarizes the recent traffic going from this packet's host+port (IP)
    plot_hist(df_mirai['HpHp_L3_weight'],'Traffic from host port to host port weight (mirai)','./EDA/HpHp_L3_weight_mirai_hist.png')
    plot_hist(df_gafgyt['HpHp_L3_weight'],'Traffic from host port to host port weight (gafgyt)','./EDA/HpHp_L3_weight_gafgyt_hist.png')

    #keep all host to host flows
    df_hist = df_gafgyt[df_gafgyt.columns[df_gafgyt.columns.str.startswith('HpHp_')]]
    plot_correlation_matrix(df_hist, 'baschlite')
    
    df_hist = df_mirai[df_mirai.columns[df_mirai.columns.str.startswith('HpHp_')]]
    plot_correlation_matrix(df_hist, 'mirai')
    
    df_benign = df_benign[df_benign.columns[df_benign.columns.str.startswith('HpHp_')]]
    plot_correlation_matrix(df_hist, 'benign')

if __name__ == '__main__':
    EDA(*sys.argv[1:])