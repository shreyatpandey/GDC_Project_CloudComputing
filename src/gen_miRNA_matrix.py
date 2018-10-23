# copyright: yueshi@usc.edu
import pandas as pd 
import hashlib
import os 
from utils import logger
def file_as_bytes(file):
    with file:
        return file.read()

def extractMatrix(dirname):
	'''
	return a dataframe of the miRNA matrix, each row is the miRNA counts for a file_id

	'''
	count = 0

	miRNA_data = []
	for idname in os.listdir(dirname):
		# list all the ids 
		if idname.find("-") != -1:
			idpath = dirname +"/" + idname

			# all the files in each id directory
			for filename in os.listdir(idpath):
				# check the miRNA file
				if filename.find("-") != -1:

					filepath = idpath + "/" + filename
					df = pd.read_csv(filepath,sep="\t")
					# columns = ["miRNA_ID", "read_count"]
					if count ==0:
						# get the miRNA_IDs 
						miRNA_IDs = df.miRNA_ID.values.tolist()

					id_miRNA_read_counts = [idname] + df.read_count.values.tolist()
					miRNA_data.append(id_miRNA_read_counts)


					count +=1
					# print (df)
	columns = ["file_id"] + miRNA_IDs
	df = pd.DataFrame(miRNA_data, columns=columns)
	return df

def extractLabel(inputfile):
	df = pd.read_csv(inputfile, sep="\t")
	#
	# print (df[columns])
	df['label'] = df['cases.0.samples.0.sample_type']
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Additional - New Primary"), 'label'] = 0
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Additional Metastatic"), 'label'] = 1
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Cell Lines"), 'label'] = 2
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Control Analyte"), 'label'] =3
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Metastatic"), 'label'] = 4
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Primary Blood Derived Cancer - Bone Marrow"), 'label'] = 5
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Primary Blood Derived Cancer - Peripheral Blood"), 'label'] = 6
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Primary Tumor"), 'label'] = 7
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Recurrent Blood Derived Cancer - Bone Marrow"), 'label'] = 8
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Recurrent Blood Derived Cancer - Peripheral Blood"), 'label'] = 9
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Recurrent Tumor"), 'label'] = 10
	df.loc[df['cases.0.samples.0.sample_type'].str.contains("Solid Tissue Normal"), 'label'] = 11
	
	additional_new_primary = df.loc[df.label == 0].shape[0]
	additional_metastatic = df.loc[df.label == 1].shape[0]
	cell_lines = df.loc[df.label == 2].shape[0]
	control_analyte = df.loc[df.label == 3].shape[0]
	metastatic = df.loc[df.label == 4].shape[0]
	primary_bone_marrow = df.loc[df.label == 5].shape[0]
	primary_peripheral_blood = df.loc[df.label == 6].shape[0]
	primary_tumor = df.loc[df.label == 7].shape[0]
	recurrent_blood_bone_marrow = df.loc[df.label == 8].shape[0]
	recurrent_blood_peripheral = df.loc[df.label == 9].shape[0]
	recurrent_tumor = df.loc[df.label == 10].shape[0]
	solid_tissue_normal = df.loc[df.label == 11].shape[0]
	
	
	logger.info("{} additional_new_primary, {} additional_metastatic,{} cell_lines,{} control_analyte,{} metastatic,{} primary_bone_marrow,{} primary_peripheral_blood,{} primary_tumor,{} recurrent_blood_bone_marrow,{} recurrent_blood_peripheral,{} recurrent_tumor,{} solid_tissue_normal".format(additional_new_primary,additional_metastatic,cell_lines,control_analyte,metastatic,primary_bone_marrow,primary_peripheral_blood,primary_tumor,recurrent_blood_bone_marrow,recurrent_blood_peripheral,recurrent_tumor,solid_tissue_normal))
	columns = ['file_id','label']
	return df[columns]

if __name__ == '__main__':


	data_dir = "/home/student/Lab10_Cho/GDCproject/data/"
	# Input directory and label file. The directory that holds the data. Modify this when use.
	dirname = "/home/student/Lab10_Cho/GDCproject/live_mrna"
	label_file = data_dir + "files_meta_1.tsv"
	
	#output file
	outputfile = data_dir + "miRNA_matrix_1.csv"

	# extract data
	matrix_df = extractMatrix(dirname)
	label_df = extractLabel(label_file)

	#merge the two based on the file_id
	result = pd.merge(matrix_df, label_df, on='file_id', how="left")
	#print(result)

	#save data
	result.to_csv(outputfile, index=False)
	#print (labeldf)

 




