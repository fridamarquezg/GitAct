import polars as pl

# Crear un DataFrame de ejemplo
data = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Barcelona"},
    {"nombre": "Pedro", "edad": 28, "ciudad": "Sevilla"},
    {"nombre": "María", "edad": 41, "ciudad": "Valencia"}
]

df = pl.DataFrame(data)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Obtener algunas estadísticas básicas
print(df.select(pl.col("edad")).stat().describe())