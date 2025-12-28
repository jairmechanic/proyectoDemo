# Video Explicativo: Números Enteros con Manim

Este proyecto contiene un video educativo creado con Manim que explica el concepto de los números enteros siguiendo una narrativa pedagógica.

## Estructura del Video

El video sigue este guión:

1. **Problema 1**: Se presenta una situación simple de suma (María tiene 5 manzanas y recibe 3 más)
2. **Solución 1**: Los números naturales funcionan perfectamente para contar y sumar
3. **Problema Peor**: Aparece una resta imposible en naturales (3 - 5 = ?)
4. **Solución Definitiva**: Se introducen los números enteros con negativos, cero y positivos

## Requisitos

```bash
pip install manim
```

O con manim community edition:
```bash
pip install manim-ce
```

## Cómo ejecutar

### Renderizar el video en calidad media:
```bash
manim -pql numeros_enteros.py NumerosEnteros
```

### Renderizar en alta calidad:
```bash
manim -pqh numeros_enteros.py NumerosEnteros
```

### Renderizar en calidad 4K:
```bash
manim -pqk numeros_enteros.py NumerosEnteros
```

## Opciones de renderizado

- `-p`: Reproduce el video automáticamente después de renderizar
- `-ql`: Calidad baja (480p, más rápido)
- `-qm`: Calidad media (720p)
- `-qh`: Calidad alta (1080p)
- `-qk`: Calidad 4K (2160p)

## Contenido del Video

- Animaciones de objetos (manzanas) para visualizar problemas
- Rectas numéricas interactivas
- Transiciones suaves entre secciones
- Visualización de operaciones matemáticas
- Código de colores:
  - **Rojo**: Problemas y números negativos
  - **Verde**: Soluciones y éxito
  - **Azul**: Números naturales
  - **Amarillo/Dorado**: Números enteros (solución final)

## Estructura del código

El archivo `numeros_enteros.py` contiene:
- `NumerosEnteros`: Clase principal de la escena
- `problema_1()`: Primer problema con suma de manzanas
- `solucion_1()`: Introducción a números naturales
- `problema_peor()`: Problema de resta con resultado negativo
- `solucion_definitiva()`: Presentación completa de números enteros

## Duración aproximada

El video tiene una duración aproximada de 2-3 minutos.
