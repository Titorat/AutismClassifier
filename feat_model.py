# This file #2
# Feature selection and SVM model

import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn import svm
from sklearn.metrics import f1_score

# This is a printing function for printing kFold results
def printing(y_true, y_predicted, score):
    print('True\tModel\tMatch')
    for i,j in zip(y_true, y_predicted):
        match = int(i == j)
        print(i,j,match,sep='\t')
    print('The mean accuracy (F-score)', score)
    print('\n')
# This is getting the DEGs from the CDA file named both
with open('both.txt') as f:
    genes = list(line.split()[0] for line in f)
genes = genes[9:]

# Building the CDA from pre_CDA txt file (output of file #1 .py)
df = pd.read_csv('pre_CDA.txt', delimiter='\t', header = None)
df = df.transpose()
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0)).reset_index(drop=True).set_index("IDENTIFIER")
# each cloumn is a feature, each row is an instance
# y is the class label
X = df.values
y = df.index 

# building the reduced model
df_reduced = df.loc[:, df.columns.isin(genes)]
X_reduced = df_reduced.values # y didn't change! we only reduced the feature space

# building a pipeline
# why pipeline? because if we want to add ant other steps, it would be easier in a pipeline format.
pipe = make_pipeline(svm.SVC(kernel="linear")) #StandardScaler(), 
kf = KFold(n_splits=5)
k_scores = []
for train_idx, test_idx in kf.split(X_reduced):
    # splitting into trail and test
    x_train = X_reduced[train_idx]
    y_train = y[train_idx]
    x_test = X_reduced[test_idx]
    y_test = y[test_idx]
    # fit, predict, scoring, and printing
    pipe.fit(x_train, y_train)
    pipe_predicted = pipe.predict(x_test)
    f_score = f1_score(y_test, pipe_predicted, average='micro')
    k_scores.append(f_score)
    printing(y_test, pipe_predicted, f_score)
print('KFold average score=', np.average(k_scores), '\n')
