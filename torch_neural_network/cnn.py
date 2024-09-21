import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

# Define the CNN architecture
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # First convolutional layer (input channels = 1, output channels = 32, kernel size = 3x3)
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        # Second convolutional layer (32 input channels, 64 output channels)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        # Fully connected layer after flattening the output from conv layers
        self.fc1 = nn.Linear(64 * 7 * 7, 128) # Adjust for image size (28x28 -> 14x14 -> 7x7 after pooling)
        self.fc2 = nn.Linear(128, 10)  # Output 10 classes (for digits 0-9)
        self.pool = nn.MaxPool2d(2, 2)  # Max pooling layer with a 2x2 window
        # Dropout to avoid overfitting, this "kills" 50% of the neurons so the nn doesn't depend on specific ones
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        # Convolutional layers followed by ReLU and Max Pooling
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        # Flatten the tensor for fully connected layers
        x = x.view(-1, 64 * 7 * 7)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
