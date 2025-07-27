from sklearn.preprocessing import MinMaxScaler

X = [[1], [2], [3], [4], [5]]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
