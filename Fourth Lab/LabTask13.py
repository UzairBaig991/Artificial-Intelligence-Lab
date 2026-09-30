import pandas as pd

s = pd.Series(['100', '200', 'python', '300.12', '400'])
print(pd.to_numeric(s, errors='coerce'))