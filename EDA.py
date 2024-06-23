import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos
sales_data = pd.read_csv('sales_data.csv')

# Explorar el conjunto de datos
print(sales_data.head())

# Verificar la información del conjunto de datos
print(sales_data.info())

# Limpiar los datos
# Eliminar filas con valores nulos
sales_data_cleaned = sales_data.dropna()

# Crear una nueva característica: total de ventas
sales_data_cleaned['total_sales'] = sales_data_cleaned['price'] * sales_data_cleaned['quantity']

# Visualización: histograma de precios
plt.figure(figsize=(10, 6))
sns.histplot(sales_data_cleaned['price'], bins=20, kde=True)
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.title('Distribución de precios')
plt.show()

# Visualización: gráfico de barras de las categorías de productos más vendidas
top_categories = sales_data_cleaned['category'].value_counts().nlargest(10)
plt.figure(figsize=(12, 8))
sns.barplot(x=top_categories.index, y=top_categories.values)
plt.xlabel('Categoría')
plt.ylabel('Número de ventas')
plt.title('Top 10 de categorías de productos más vendidas')
plt.xticks(rotation=45)
plt.show()

# Visualización: gráfico de dispersión de ventas totales por mes
sales_data_cleaned['date'] = pd.to_datetime(sales_data_cleaned['date'])
sales_data_cleaned['month'] = sales_data_cleaned['date'].dt.month
sales_data_cleaned['year'] = sales_data_cleaned['date'].dt.year
total_sales_by_month = sales_data_cleaned.groupby(['year', 'month'])['total_sales'].sum().reset_index()
plt.figure(figsize=(12, 8))
sns.scatterplot(x='month', y='total_sales', hue='year', data=total_sales_by_month, s=100)
plt.xlabel('Mes')
plt.ylabel('Ventas totales')
plt.title('Ventas totales por mes')
plt.legend(title='Año')
plt.show()
