import polars as pl
import numpy as np
import matplotlib.pyplot as plt

# Simular datos de temperatura para 30 días, con 24 mediciones por día
np.random.seed(0)  # Para reproducibilidad
data = np.random.normal(loc=20, scale=5, size=(30, 24))

# Crear un DataFrame de Polars a partir de los datos de Numpy
df = pl.DataFrame(data, columns=[f"hour_{i}" for i in range(24)])

# Calcular el promedio diario de las temperaturas
df["daily_avg"] = df.select(pl.all().mean(axis=1))

# Preparar datos para la visualización
dates = pl.date_range(low="2023-01-01", high="2023-01-30", interval="1d")
df = df.with_column(pl.Series("date", dates))
plot_data = df.select(["date", "daily_avg"]).to_pandas()

# Visualización de las temperaturas promedio diarias
plt.figure(figsize=(10, 5))
plt.plot(plot_data['date'], plot_data['daily_avg'], marker='o')
plt.title("Promedio Diario de Temperaturas en Enero")
plt.xlabel("Fecha")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
