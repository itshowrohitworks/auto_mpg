from data.auto_mpg import get_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from .data_preprocessing import preprocessing
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score,root_mean_squared_error

# Importing the Data:
df = get_data()
X,y = preprocessing(data=df)

# Train and Test splitting the Data:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Creation and Training:
linear = LinearRegression()
print(f"Training Linear Regression Model on our Data: {X_train.shape}\n")
linear.fit(X_train,y_train)

pred = linear.predict(X_test)

# Evaluation Metrics:
print("Metrics for Regression:")
print("R2:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))
print("MSE:", mean_squared_error(y_test,pred))
print("RMSE:", root_mean_squared_error(y_test, pred))