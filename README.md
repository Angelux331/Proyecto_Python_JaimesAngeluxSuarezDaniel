# Gestor de Gastos Personales

Sistema de gestión de gastos desarrollado en Python que permite registrar, visualizar y generar reportes detallados de gastos personales organizados por categorías.

## Descripción

Aplicación de consola interactiva que facilita el control de finanzas personales mediante un sistema de menús intuitivo. Permite agregar gastos, filtrarlos por diversos criterios, calcular totales y generar reportes formateados.

## Características

- **Registro de gastos** con validación de datos (monto, fecha, descripción)
- **Categorización** automática (Transporte, Comida, Servicios, Entretenimiento, Salud, Educación, Otros)
- **Filtros avanzados** por categoría y rango de fechas
- **Cálculos automáticos** de totales (diarios, semanales, mensuales e históricos)
- **Reportes formateados** con interfaz visual de cajas y tablas
- **Persistencia de datos** en formato JSON
- **Validaciones robustas** en todas las entradas del usuario

## Tecnologías

- Python 3.10.6
- JSON para almacenamiento de datos
- Módulo `datetime` para manejo de fechas
- Caracteres Unicode para diseño visual

## Instalación y Uso

### Requisitos
- Python 3.8 o superior

### Instalación

1. Clona o descarga el repositorio:

git clone https://github.com/Angelux331/Proyecto_Python_JaimesAngeluxSuarezDaniel.git

cd Proyecto_Python_JaimesAngeluxSuarezDaniel

2. Ejecuta el programa:

## Guía de Uso

### 1. Registrar Gasto
- Selecciona una categoría de la lista
- Ingresa el monto (solo números positivos)
- Ingresa la fecha en formato YYYY-MM-DD
- Añade una descripción del gasto

### 2. Listar Gastos
- **Ver todos**: Muestra todos los gastos registrados
- **Filtrar por categoría**: Muestra gastos de una categoría específica
- **Filtrar por fechas**: Muestra gastos en un rango de fechas

### 3. Calcular Totales
- **Total diario**: Gastos del día actual
- **Total semanal**: Últimos 7 días
- **Total mensual**: Mes actual
- **Total histórico**: Todos los gastos registrados

### 4. Generar Reportes
Reportes formateados con diseño visual profesional:
- Reporte diario
- Reporte semanal
- Reporte mensual
- Reporte histórico completo

## Ejemplos de Uso

### Agregar un gasto:
Categoría: Transporte
Monto: 5000
Fecha: 2025-12-03
Descripción: Taxi al trabajo

## Funcionalidades Técnicas

### Validaciones Implementadas
- **Montos**: Solo acepta números positivos mayores a 0
- **Fechas**: Formato YYYY-MM-DD con verificación de validez
- **Categorías**: Verifica existencia antes de proceder
- **Rangos**: Valida que fecha inicio ≤ fecha fin
- **Datos vacíos**: Manejo de listas sin gastos

### Funciones Principales
- `AgregarGasto()`: Registra nuevos gastos
- `vetodoslosgastos()`: Lista todos los gastos
- `vergastosporcategoria()`: Filtra por categoría
- `filtrarporfechas()`: Filtra por rango temporal
- `calcularsemanal()`: Calcula totales semanales
- `calcularmensual()`: Calcula totales mensuales
- `generarreporte()`: Genera reportes formateados

## Formato de Datos

El archivo `gastos.json` utiliza la siguiente estructura:

{
  "Gastos": {
    "Categoria": {
      "Transporte": [
        {
          "monto": 5000,
          "fecha": "2025-12-03",
          "descripcion": "Taxi al trabajo"
        }
      ]
    }
  }
}

## Personalización

El proyecto incluye:
- Formateo de números con separadores de miles
- Interfaz limpia y profesional

## Autor

Desarrollado por Angelux331

## Futuras Mejoras

-  Exportar reportes a PDF/Excel
-  Gráficos estadísticos
-  Presupuestos por categoría
-  Alertas de gastos excesivos
-  Múltiples usuarios
-  Backup automático de datos

---

**Nota**: Este proyecto fue desarrollado como parte de un ejercicio de programación en Python, demostrando conocimientos en manejo de archivos, estructuras de datos, validaciones y diseño de interfaces de consola.
