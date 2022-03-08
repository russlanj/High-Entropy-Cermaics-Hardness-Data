## Code written by: Russlan Jaafreh

#import the full dataset with features
df1 = pd.read_csv('Full_dataset_with_features.csv',encoding='latin1') ## please save the full dataset with features as Full_dataset_with_features.csv file
comp = df1['composition']
Before_Features = df1.drop(['composition','hardness','structure'], axis =1)
Y = df1['hardness']

#VT
from sklearn.feature_selection import VarianceThreshold
var_thres = VarianceThreshold(threshold=.8*(1-0.8))
var_thres.fit(Before_Features)
var_thres.get_support()
constant_columns = [column for column in Before_Features.columns if column not in Before_Features.columns[var_thres.get_support()]]
After_Variance = Before_Features.drop(constant_columns,axis=1)

#PC
import matplotlib.pyplot as plt 
import seaborn as sns
d
ef correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    af_corr = dataset.drop(col_corr,axis=1)
    return af_corr

A_cor = af_both2.corr()
plt.figure(figsize=(25,20))
sns.heatmap(A_cor,cmap=plt.cm.CMRmap_r,annot=False)
plt.show()

#Scaling
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df1_scaled = scaler.fit_transform(af_both2)
df_scaled = pd.DataFrame(df1_scaled)
df_scaled.columns =af_both2.columns

#Test,Train Split
X_train, X_test, y_train, y_test = train_test_split(df_scaled, Y, test_size=0.25, random_state=99)

#RF Model
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=500,criterion='mse')
rf_reg.fit(X_train,y_train)
rf_reg.score(X_test,y_test)
y_pred_rf = rf_reg.predict(X_test)

#Vizualize
e = sns.jointplot(x=y_test, y= y_pred_rf)
e.fig.suptitle("RF")
e.ax_joint.set_xlabel('Experimental', fontweight='bold')
e.ax_joint.set_ylabel('Predicted', fontweight='bold')

#Prediction
d_predict = pd.read_csv('cases4prediction.csv') ## please save the prediction cases with full features as cases4prediction.csv
d_predict = d_predict[X_train.columns]
d_predict_scaled = scaler.transform(d_predict)
y_pred_rf = rf_reg.predict(df_predict_scaled)
y_predict_excel = pd.DataFrame(y_pred_rf)
y_predict_excel.to_csv("prediction.csv") ## the predicted cases will be saved as prediction.csv
