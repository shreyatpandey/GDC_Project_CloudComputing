#cell 0
import pandas as pd
import pylab as pl
from sklearn.cluster import KMeans

#cell 1
class elbow_curve:
    def elbow_curve_determination(self,string_file):
        Nc = range(1, 20)
        input_data = pd.read_csv(input_file)
        column_names_without_file_id = input_data.drop('file_id',axis = 1)
        kmeans = [KMeans(n_clusters=i) for i in Nc]
        score = [kmeans[i].fit(column_names_without_file_id).score(column_names_without_file_id) for i in range(len(kmeans))]
        pl.plot(Nc,score)
        pl.xlabel('Number of Clusters')
        pl.ylabel('Score')
        pl.title('Elbow Curve')
        pl.show()

    


#cell 2
if __name__ == "__main__" :
    input_file = r'C:\Users\pande\Downloads\EE542Cho\project\data_source\dataset\miRNAseq_matrix_original.csv'
    result_elbow_curve = elbow_curve()
    result_elbow_curve.elbow_curve_determination(input_file)
    
    
    


#cell 3


