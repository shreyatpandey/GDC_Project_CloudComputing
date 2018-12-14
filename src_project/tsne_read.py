import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LassoCV
from sklearn.linear_model import Lasso
from sklearn.manifold import TSNE



input_file = r'C:\Users\pande\Downloads\EE542Cho\project\data_source\dataset\miRNAseq_matrix_original.csv'
input_data = pd.read_csv(input_file)
column_names_without_file_id = input_data.drop('file_id',axis = 1)
column_names_without_file_id_label = column_names_without_file_id.drop('label',axis=1)
only_labels = input_data.pop('label').values

feature_list = list(column_names_without_file_id_label.columns)
features = np.array(column_names_without_file_id_label)
labels = np.array(only_labels)
print("Length_Labels:",len(labels))


#split-function
x_random_train,x_random_test, y_random_train,y_random_test = train_test_split(features,labels,train_size = 0.6)
pca_50 = PCA(n_components=20)
pca_result_50 = pca_50.fit_transform(x_random_train)
tsne_output = TSNE(n_components=20, method='exact').fit_transform(pca_result_50)