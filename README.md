# Proyecto Demo - Animaciones Matemáticas con Manim

Este proyecto contiene animaciones educativas de matemáticas creadas con Manim para contenido de TikTok.

## Instalación de Manim

Primero, instala Manim en tu sistema:

```bash
pip install manim
```

O si usas conda:

```bash
conda install -c conda-forge manim
```

## Cómo renderizar las animaciones

### Para video de alta calidad (1080p):
```bash
manim -pql linear_equations.py LinearEquations
```

### Para video de calidad media (720p):
```bash
manim -pqm linear_equations.py LinearEquations
```

### Para video de alta calidad (1080p):
```bash
manim -pqh linear_equations.py LinearEquations
```

### Para formato vertical (TikTok/Reels):
```bash
manim -pql linear_equations.py LinearEquations --format=mov -r 1080,1920
```

## Archivos incluidos

- `linear_equations.py` - Animación de Ecuaciones Lineales

## Contenido de la animación

La animación de Ecuaciones Lineales incluye:
1. Definición de ecuación lineal
2. Forma general: ax + b = 0
3. Fórmula de solución: x = -b/a
4. Ejemplo práctico: 2x + 6 = 0
5. Resolución paso a paso
6. Verificación de la solución

## Salida

El video se generará en la carpeta `media/videos/linear_equations/` con el nombre correspondiente a la calidad seleccionada.
