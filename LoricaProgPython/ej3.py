import seaborn as sns 
import matplotlib.pyplot as plt
# Cargar un conjunto de datos de ejemplo
data = sns.load_dataset("iris")
# Crear un gráfico de dispersión
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")
# Mostrar el gráfico
plt.show()