import pandas as pd
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import torch.optim as optim
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('your_weather_data.csv')

# Convert the date column to datetime and set as index
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# Create features and target variable
features = data[['temp_max']]
target = data['temp_min']

# Use the last 'look_back' days to predict the next day
look_back = 230

def create_sequences(data, target, look_back):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:i + look_back])
        y.append(target[i + look_back])
    return np.array(X), np.array(y)

X, y = create_sequences(features.values, target.values, look_back)
X = X.reshape((X.shape[0], look_back, 1))  # Ensure the correct shape

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert to PyTorch tensors
train_encodings = torch.tensor(X_train, dtype=torch.float32)
train_labels = torch.tensor(y_train, dtype=torch.float32)

test_encodings = torch.tensor(X_test, dtype=torch.float32)
test_labels = torch.tensor(y_test, dtype=torch.float32)

class WeatherDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        return self.encodings[idx], self.labels[idx]

    def __len__(self):
        return len(self.labels)

train_dataset = WeatherDataset(train_encodings, train_labels)
test_dataset = WeatherDataset(test_encodings, test_labels)

class SimpleRegressionModel(nn.Module):
    def __init__(self, input_dim):
        super(SimpleRegressionModel, self).__init__()
        self.linear1 = nn.Linear(input_dim, 128)  # input_dim should be 1
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(128, 64)
        self.linear3 = nn.Linear(64, 1)
        self.dropout = nn.Dropout(p=0.3)  # Drop 50% of the neurons randomly during training

    def forward(self, x):
        # Flatten the sequence dimensions
        x = x.view(-1, look_back)
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.relu(x)
        x = self.linear3(x)
        return x

def custom_loss(predictions, targets):
    loss = criterion(predictions, targets)
    under_penalty = 150  # Adjust this factor to penalize underestimation
    underestimation = (targets - predictions).clamp(min=0) * under_penalty
    return loss + underestimation.mean()

# In your training loop, replace criterion with custom_loss


model = SimpleRegressionModel(input_dim=look_back)
predictions_list = []
for loops in range(10):
    learning_rate = 0.0001
    batch_size = 16
    epochs = 3000

    # DataLoader
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    # Optimizer and Loss
    optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=1e-4)
    criterion = nn.MSELoss()

    # Training Loop
    model.train()
    for epoch in range(epochs):
        epoch_loss = 0
        for X_batch, y_batch in train_loader:
            # Ensure X_batch has the shape (batch_size, look_back, num_features)
            X_batch = X_batch.view(-1, look_back)
            
            # Zero the gradients
            optimizer.zero_grad()
            
            # Forward pass
            predictions = model(X_batch)
            
            # Compute the loss
            loss = custom_loss(predictions, y_batch.unsqueeze(1))
            
            # Backward pass and optimization
            loss.backward()
            # In your training loop, add this line before optimizer.step()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            
            epoch_loss += loss.item()
        
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {epoch_loss / len(train_loader):.4f}")

    # Predict future values
    # Predict future values
    future_days = 7  # Number of future days to predict
    model.eval()

    # Start with the last sequence from the test set
    last_sequence = test_encodings[-1]  # This should have the shape (look_back, num_features)

    # Reshape last_sequence to match the input shape of the model (1, look_back, num_features)
    try:
        last_sequence = last_sequence.view(1, look_back, 1)  # This should give shape (1, look_back)
    except Exception as e:
        print("it no work mum :(")
        print("Tis sag :(")
        print("da exeption is")
        print(e)
        print("and also")
        print("here is the shape of the last seqence to cheer you up :)")
        print(last_sequence.shape)
    predicted_temperatures = []

    with torch.no_grad():
        for _ in range(future_days):
            input_tensor = last_sequence.float()  # Ensure this is correctly shaped and in the right type
            
            # Check the shape of input_tensor
            print(f"Input tensor shape: {input_tensor.shape}")
            
            # Predict the next value
            next_temp_min = model(input_tensor).item()
            
            # Append the prediction
            predicted_temperatures.append(next_temp_min)
            
            # Update the last sequence
            last_sequence = torch.roll(last_sequence, shifts=-1, dims=1)  # Roll along the time dimension
            last_sequence[0, -1, 0] = next_temp_min  # Add the prediction to the end of the sequence

            # Create a pandas series for predicted values
    predicted_dates = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=future_days)
    predictions_list.append(predicted_temperatures)
# Plot the results
final_predictions = []
print(predictions_list)
for loops1 in range(future_days):
    working_preds_to_average = []
    working_average = 0
    for loops2 in range(len(predictions_list)):
        working_preds_to_average.append(predictions_list[loops2 - 1][loops1 - 1])
        print(predictions_list[loops2 - 1][loops1 - 1])
    print(working_preds_to_average)
    working_average = sum(working_preds_to_average) / len(working_preds_to_average)
    print(working_average)
    final_predictions.append(working_average)
predicted_series = pd.Series(final_predictions, index=predicted_dates)
plt.figure(figsize=(10, 6))
plt.plot(data.index[-look_back:], data['temp_min'].values[-look_back:], label='Past Temp Min')
plt.plot(predicted_series.index, predicted_series.values, label='Predicted Temp Min', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Prediction')
plt.legend()
plt.show()

# Model evaluation
model.eval()
predictions = []
with torch.no_grad():
    for X_batch, _ in test_loader:
        X_batch = X_batch.view(-1, look_back)  # Flatten the sequence dimensions
        preds = model(X_batch)
        predictions.extend(preds.squeeze().tolist())

# Convert predictions and actual values back to pandas for easy comparison
predictions = pd.Series(predictions, index=y_test.index)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print(f'MAE: {mae:.4f}, MSE: {mse:.4f}')
