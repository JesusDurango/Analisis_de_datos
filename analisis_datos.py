import numpy as np
from datasets import load_dataset


dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

edades =data["age"]

edades_np = np.array(edades)

promedio_edades = np.mean(edades_np)

print (promedio_edades)