# Taller 5: Mínimos Cuadrados

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-blue)
![Numerical Methods](https://img.shields.io/badge/Numerical%20Methods-Least%20Squares-blueviolet)

Este proyecto es una herramienta interactiva para la interpolación parabólica de tres puntos, desarrollada en Python usando PyQt5 y Matplotlib. Permite mover el punto intermedio y ver en tiempo real cómo cambia la parábola ajustada.

## Características

- **Interpolación parabólica** de tres puntos.
- **Interfaz gráfica** profesional y estética en escala de azules.
- **Punto intermedio movible** con el mouse.
- **Visualización en tiempo real** de la curva y las coordenadas del punto movible.
- **Ventana maximizada** al iniciar.
- **Cuadrícula fina y ejes con numeración clara**.

## Requisitos

- Python 3.7+
- PyQt5
- matplotlib
- numpy

Puedes instalar las dependencias con:

```bash
pip install pyqt5 matplotlib numpy
```

## Uso

1. Clona este repositorio.
2. Ejecuta el archivo principal:

   ```bash
   python python\ interactivo.py
   ```

3. Mueve el punto azul (p2) con el mouse para ver cómo cambia la parábola y las coordenadas.

## Archivos principales

- `python interactivo.py`: Código fuente de la aplicación interactiva.
- `.gitignore`: Exclusiones recomendadas para Python, Jupyter, VSCode y entornos virtuales.
- `Ejercicio 1.ipynb`: Enunciado y explicación del ejercicio.

## Créditos

Desarrollado para el Taller de Métodos Numéricos - Interpolación por mínimos cuadrados.

---