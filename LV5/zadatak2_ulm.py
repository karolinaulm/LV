import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_csv('occupancy_processed.csv')

feature_names=['S3_Temp','S5_CO2']
target_name='Room_Occupancy_Count'

x = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

x_train,x_test,y_train,y_test=train_test_split(
    x,y,
    test_size=0.2,
    stratify=y,
    random_state=51
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=['Class 0','Class 1']
    )

disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("Preciznost:",precision)
print("Odziv:",recall)
print("Tocnost:",accuracy)
print(classification_report(y_test, y_pred))
