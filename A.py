import streamlit as st
import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):    
        self.df = pd.read_csv(self.file_path)

    def preview_data(self):
        st.write("Vista previa de los primeros 10 datos:")
        st.dataframe(self.df.head(10))

    def calculate_statistics(self):
        st.write("Estadísticas descriptivas de las columnas numéricas:")
        for column in self.df.select_dtypes(include=['float64', 'int64']).columns:
            st.write(f"=======================> Columna: {column}")
            st.write(f"Media: {self.media(column)}")
            st.write(f"Mediana: {self.mediana(column)}")
            st.write(f"Desviación Estándar: {self.std(column)}")

    def media(self, column):
        suma = 0
        n = 0
        for valor in self.df[column]:
            suma=suma+valor
            n = n + 1
        return suma/n

    def mediana(self, column):
        a = sorted(self.df[column])
        n = len(a)
        if n % 2 == 0:
            return (a[n//2-1]+a[n//2])/2
        else:
            return a[n//2]

    def std(self, column):
        m = self.media(column)
        suma = 0
        n = 0
        for valor in self.df[column]:
            suma = suma + (valor - m) ** 2
            n = n + 1
        return (suma / n) ** 0.5

if __name__ == "__main__":
    st.title("Aplicación de Análisis de Datos")
    file_path = "datos4.csv"
    data_handler = DataHandler(file_path)
    data_handler.load_data()
    data_handler.preview_data()
    data_handler.calculate_statistics()
