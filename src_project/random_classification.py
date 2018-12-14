#cell 0
import pandas as pd
import numpy as np
from tsne_read import tsne_output
from tsne_read import y_random_train
from tsne_read import RandomForestClassifier
from tsne_read import feature_list
from tsne_read import column_names_without_file_id_label
from tsne_read import input_data
from tsne_read import only_labels
from tsne_read import plt


#cell 1
rf_exp = RandomForestClassifier(n_estimators=1000 , random_state=100)
rf_exp.fit(tsne_output, y_random_train)

print("rf_expt.feature_importances:",rf_exp.feature_importances_)

importances = list(rf_exp.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 3)) for feature, importance in zip(feature_list, importances)]
# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
print("feature_importances:",feature_importances)
# Print out the feature and importances 
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]

#cell 2
#creating_reduced_column_file
feature_importances_modified = []
for k in range(0,len(feature_importances)):
    feature_importances_modified.append(feature_importances[k][0])

print("feature_importances_modified:",feature_importances_modified)
df_new = column_names_without_file_id_label[feature_importances_modified]
#print("df_new:",df_new)
print("Length_df_new:",len(df_new))
first_column_only = input_data['file_id']
#print("first_column_only:",first_column_only)
#print("Length_first_column_only:",len(first_column_only))


df_new['file_id'] = first_column_only
#print("df_new:",df_new)
columns_df_new = df_new.columns.tolist()
columns_df_new = columns_df_new[-1:] + columns_df_new[:-1]
print("columns_df_new:",columns_df_new)
df_new = df_new[columns_df_new]
#print("df_new_file_id:",df_new)
df_new['label'] = only_labels
print("df_new_label:",df_new)

out_csv = r'C:\Users\pande\Downloads\EE542Cho\project\data_source\miRNAseq_matrix_original_reduced.csv'
df_new.to_csv(out_csv,encoding='utf-8',index = False)

#cell 3
x_values = list(range(len(importances)))
plt.bar(x_values, importances, orientation = 'vertical', color = 'r', edgecolor = 'k', linewidth = 1.2)
plt.xticks(x_values, feature_list, rotation='vertical')
plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances');

#cell 4
from tsne_read import x_random_train
from tsne_read import x_random_test
# Extract the names of the most important features
important_feature_names = [feature[0] for feature in feature_importances[0:16]]
# Find the columns of the most important features
important_indices = [feature_list.index(feature) for feature in important_feature_names]
# Create training and testing sets with only the important features
important_train_features = x_random_train[:, important_indices]
important_test_features = x_random_test[:, important_indices]

#cell 5
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from tsne_read import y_random_test
# Train the expanded model on only the important features
rf_exp.fit(important_train_features, y_random_train)
# Make predictions on test data
predictions = rf_exp.predict(important_test_features)
#print("predictions:",predictions)
print("predictions_mean:",round(np.mean(predictions),2)*100,"%")
precision = precision_score(y_random_test,predictions,average='macro',labels=np.unique(predictions))
accuracy = accuracy_score(y_random_test,predictions)
f1 = f1_score(y_random_test,predictions,average='macro',labels=np.unique(predictions))
print("precision:",round(precision,2)*100,"%")
print("accuracy:",round(accuracy,2)*100,"%")
print("f1:",round(f1,2)*100,"%")


#cell 6


