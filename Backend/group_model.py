import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

rows_to_skip=[154710]
# Load the dataset
file_path = r'Backend\globalterrorismdataset.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1', skiprows=rows_to_skip)  # Update with your dataset filename

# Select useful features
useful_features = ['AttackType', 'Target_type', 'Weapon_type', 'Region', 'Group']

# Filter dataframe with selected features
df = df[useful_features]

# Drop rows with missing values
df.dropna(inplace=True)

# Encode categorical features
df_encoded = pd.get_dummies(df, columns=['AttackType', 'Target_type', 'Weapon_type', 'Region'])

# Split data into train and test sets
X = df_encoded.drop('Group', axis=1)
y = df_encoded['Group']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
x_t = X_train.tail(100)
y_t = y_train.tail(100)
model.fit(x_t, y_t)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'terrorism_prediction_model_useful_columns.pkl')  # Update with your model filename
