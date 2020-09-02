import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

from tblr.models import ConstantModel

# Set random seed
seed = 42

# Load in the data
x_full = pd.read_csv('data/raw/train.csv')
y_full = x_full.pop('claim')
x_train, x_test, y_train, y_test = train_test_split(x_full, y_full, test_size=0.2, random_state=seed)

model = ConstantModel(constant=0.5)
model.train(x_train, y_train)

y_pred = model.predict(x_test)
score = roc_auc_score(y_test, y_pred)

print(score)
