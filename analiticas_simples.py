import pandas as pd
from carga_de_datos import df

# Obtén los tipos de datos actuales en el DataFrame
tipos_de_datos_actuales = df.dtypes

tipos_de_datos_esperados = {
    'age': 'int64',
    'has_anaemia':'bool',
    'creatinine_phosphokinase_concentration_in_blood': 'float64',
    'has_diabetes': 'bool',
    'heart_ejection_fraction':'float64',
    'has_high_blood_pressure' : 'bool',
    'platelets_concentration_in_blood': 'float64',
    'serum_creatinine_concentration_in_blood': 'float64',
    'serum_sodium_concentration_in_blood': 'float64',
    'is_male' :'bool',
    'is_smoker':'bool',
    'days_in_study':'int64',
    'is_dead' :'int64',  
    
}

# Compara los tipos de datos actuales con los tipos de datos esperados
for columna, tipo_esperado in tipos_de_datos_esperados.items():
    tipo_actual = tipos_de_datos_actuales[columna]
    
    if tipo_actual != tipo_esperado:
        print(f"Advertencia: La columna '{columna}' tiene el tipo de datos {tipo_actual}, pero se esperaba {tipo_esperado}.")



agregacion = df.groupby(['is_male', 'is_smoker']).size().reset_index(name='Cantidad')

hombres_fumadores = agregacion[(agregacion['is_male'] == True) & (agregacion['is_smoker'] == True)]['Cantidad'].values[0]
mujeres_fumadoras = agregacion[(agregacion['is_male'] == False) & (agregacion['is_smoker'] == True)]['Cantidad'].values[0]

print("Cantidad de hombres fumadores:", hombres_fumadores)
print("Cantidad de mujeres fumadoras:", mujeres_fumadoras)
