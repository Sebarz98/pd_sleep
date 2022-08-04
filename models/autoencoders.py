import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

from utils import helpers

path = "../data/"
df = pd.read_csv(path + "VBM_data.csv")


class Pd_Dataset(Dataset):
    def __init__(self, X):
        self.X_data = torch.from_numpy(X.values)

    def __getitem__(self, index):
        return self.X_data[index]

    def __len__(self):
        return len(self.X_data)


df_cleaned = df.loc[:, df.columns.drop(["Subjectt", "Sex", "Chr", "PD"])]
df_cleaned = helpers.clean_columns(df_cleaned)
df_cleaned = df_cleaned.astype(np.float32)

dataset = Pd_Dataset(df_cleaned)
data_loader = DataLoader(dataset=dataset, batch_size=8, shuffle=True, num_workers=2)


class AE_model(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(929, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 18),
            nn.ReLU(),
            nn.Linear(18, 2),
        )

        self.decoder = nn.Sequential(
            nn.Linear(2, 18),
            nn.ReLU(),
            nn.Linear(18, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 929),
            nn.Sigmoid(),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded


model = AE_model()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

num_epochs = 50
outputs = []
for epoch in range(num_epochs):
    for data in data_loader:
        recon = model(data)
        loss = criterion(recon, data)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch:{epoch}, Loss:{loss.item():.2f}")
    outputs.append((epoch, data, recon))
