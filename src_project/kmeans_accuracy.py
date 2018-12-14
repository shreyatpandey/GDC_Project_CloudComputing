#cell 0
import numpy as np
import pandas as pd
import pylab as pl
from sklearn.cluster import KMeans
from tsne_read import y_random_train
from tsne_read import y_random_test
from tsne_read import column_names_without_file_id
from tsne_read import tsne_output

#cell 1
class kmeans_accuracy_cluster:
    def kmeans_accuracy_cluster_input(self,labels_kmeans_run,input_list,n_clusters_list,n_cluster_length):
        correct_answer = 0
        for i in range(len(input_list)):
            for j in range(0,n_clusters_length):
                if labels_kmeans_run[i] == n_clusters_list[j]:
                    correct_answer += 1
        print("correct_answer:",correct_answer)
        print("accuracy:",round((correct_answer)/len(y_random_test)*100,2),"%")
    def cluster_map(self,clf,tsne_output_run):
        for i in range(0, tsne_output_run.shape[0]):
            if clf.labels_[i] == 0:
                c1 = pl.scatter(tsne_output[i,0],tsne_output[i,1],c='r',marker='+')
            elif clf.labels_[i] == 1:
                c2 = pl.scatter(tsne_output[i,0],tsne_output[i,1],c='g',marker='o')
            elif clf.labels_[i] == 2:
                c3 = pl.scatter(tsne_output[i,0],tsne_output[i,1],c='b',marker='*')
        pl.legend([c1, c2, c3],['Cluster 1', 'Cluster 0','Cluster 2'])
        pl.title('K-means clusters')
        pl.show()

        

        
        
        

#cell 2
if __name__ == "__main__":
    n_clusters_length = len(np.unique(y_random_train))
    n_clusters_list = np.unique(y_random_train)    
    print("n_clusters:",n_clusters_length)
    print("n_clusters_list:",n_clusters_list)
    clf = KMeans(n_clusters=7,random_state=0).fit(tsne_output)
    print("clf_kmeans:",clf)
    print("len(y_random_test):",len(y_random_test))
    clf.fit_predict(column_names_without_file_id)
    
    labels_kmeans = clf.labels_
    hold_result = kmeans_accuracy_cluster()
    hold_result. kmeans_accuracy_cluster_input(labels_kmeans,y_random_test,n_clusters_list,n_clusters_length)
    hold_result.cluster_map(clf,tsne_output)

#cell 3


