import pandas as pd
from analisis_datos import data

df = pd.DataFrame(data)
print (df)

df_is_dead = df.loc[df['is_dead'] == 1]
print (df_is_dead)
df_not_dead = df.loc[df['is_dead'] != 1]
print(df_not_dead)

promedio_edad_is_dead = df_is_dead['age'].mean()
print(promedio_edad_is_dead)
promedio_edad_not_dead = df_not_dead['age'].mean()
print(promedio_edad_not_dead)