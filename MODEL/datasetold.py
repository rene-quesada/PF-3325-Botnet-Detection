from re import I
import sys
from unicodedata import name
import pandas as pd
import numpy as np
from glob import iglob
import os

class dataset:
    def __init__(self,dirpath):
        self.dir = dirpath
        self.dn_nbaiot = ['Danmini_Doorbell', 'Ecobee_Thermostat', 'Philips_B120N10_Baby_Monitor', 'Provision_PT_737E_Security_Camera', 'Provision_PT_838_Security_Camera', 'SimpleHome_XCS7_1002_WHT_Security_Camera', 'SimpleHome_XCS7_1003_WHT_Security_Camera']
        self.df_benign = pd.DataFrame()
        self.df_mal = pd.DataFrame()
        self.df_mirai = pd.DataFrame()
        self.df_gafgyt = pd.DataFrame()
        self.df_features = pd.DataFrame()
        self.load_features_data()

    def load_mal_benign_data(self):
        self.load_mal_data()
        self.load_benign_data()

    #Load mirai and gaf attacks
    def load_mal_data(self):
        self.df_mirai = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob( self.dir + '/**/mirai_attacks/*.csv.bz2', recursive=True)), ignore_index=True)
        self.df_gafgyt = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob(self.dir + '/**/gafgyt_attacks/*.csv.bz2', recursive=True)), ignore_index=True)   
        self.df_mal = pd.concat([self.df_mirai, self.df_gafgyt])
        return
 
    def load_device_mal_data(self,device):
        df_mirai = pd.DataFrame()
        df_gafgyt = pd.DataFrame()
        df_mirai = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob( self.dir + '/' + device + '/mirai_attacks/*.csv.bz2', recursive=True)), ignore_index=True)
        df_gafgyt = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob(self.dir + '/' + device + '/gafgyt_attacks/*.csv.bz2', recursive=True)), ignore_index=True)   
        df_mal = pd.concat([df_mirai, df_gafgyt])
        return df_mal
    
    #Load benign data
    def load_benign_data(self):
        self.df_benign = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob(self.dir + '/**/benign_traffic.csv.bz2', recursive=True)), ignore_index=True)

    #Load benign data
    def load_device_benign_data(self,device):
        df_benign = pd.concat((pd.read_csv(f,compression='bz2') for f in iglob(self.dir + '/' + device + '/benign_traffic.csv.bz2', recursive=True)), ignore_index=True)
        return df_benign

    #Load features
    def load_features_data(self):
        self.df_features = pd.read_csv(self.dir + '/features.csv')

    #get list of features
    def get_feature_list(self,top_n_features):
        return self.df_features.iloc[0:int(top_n_features)]['Feature'].values

    def get_mal_dataframe(self):
        return self.df_mal

    def get_mirai_dataframe(self):
        return self.df_mirai

    def get_gafgyt_dataframe(self):
        return self.df_gafgyt

    def get_benign_dataframe(self):
        return self.df_benign

    def get_device_list(self):
        return self.dn_nbaiot

    def get_nbaiot_device_mal_data(self,device_name):
        return self.load_device_mal_data(device_name)

    def get_nbaiot_device_benign_data(self,device_name):
        return self.load_device_benign_data(device_name)



