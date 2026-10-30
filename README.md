# ComparandoEcuaciones

Este proyecto consiste en resolver una Ecuación Diferencial ordinaria con dos dsstintos métodos:
1. **Método Analítico (Separación de Variables):** Encuentra una solución exacta en forma cerrada.
2. **Método Numérico (Euler):** Aproxima la solución paso a paso en un intervalo dado.

## Problema a Resolver
* **Ecuación:** $\frac{dy}{dt} = -3y$
* **Condición Inicial:** $y(0) = 2$
* **Intervalo de estudio:** $t \in [0, 1]$
* **Tamaño de paso ($h$):** $0.2$

Para poder ejecutar el programa usando una versión reciente de Python, van a necesitar hacer lo siguiente:
```bash
(Tanto en Windows como Unix o Linux)
python3 -m venv [Nombre de entorno]

Para activar el entorno.
#Windows
```bash
#CDM
venv\Scripts\activate.bat

#Powershell
venv\Scripts\Activate.ps1

#Linux o Unix
source venv/bin/activate
# ComparandoEcuaciones

Este proyecto consiste en resolver una Ecuación Diferencial Ordinaria con dos distintos métodos:
1. **Método Analítico (Separación de Variables):** Encuentra una solución exacta en forma cerrada.
2. **Método Numérico (Euler):** Aproxima la solución paso a paso en un intervalo dado.

## Problema a Resolver
* **Ecuación:** $\frac{dy}{dt} = -3y$
* **Condición Inicial:** $y(0) = 2$
* **Intervalo de estudio:** $t \in [0, 1]$
* **Tamaño de paso ($h$):** $0.2$

## Instrucciones para el Entorno Virtual

Para poder ejecutar el programa usando una versión reciente de Python, sigue los siguientes pasos:

### 1. Crear el entorno virtual
Tanto en Windows como en Unix o Linux, ejecuta el siguiente comando:
```bash
python3 -m venv venv
