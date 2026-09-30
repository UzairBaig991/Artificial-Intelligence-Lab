import pandas as pd

df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': ['A', 'B', 'C', 'D', 'E']
})

df = df[df['col1'] != 3]
print(df)