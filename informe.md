# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence  
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Se recibieron tres reportes de ventas provenientes del ERP de sucursales (CSV), la API de fidelización (JSON) y el área de Finanzas (Excel). Se confirmó que los tres archivos contienen la misma información, con 5 filas y 4 columnas, y que sus datos y tipos son consistentes. El análisis identificó a Guayaquil Centro como la sucursal con mayores ventas y a Cuenca como la de menores ventas. Se recomienda estandarizar el reporte en formato CSV por su facilidad de lectura y procesamiento en Python y R.

## 1. ¿Los tres formatos contienen la misma información?

Se cargaron los tres archivos en Python y R, comparando sus dimensiones, estructura y contenido.

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---:|---:|---|
| CSV | ERP de sucursales | 5 | 4 | Python: `pd.read_csv()` / R: `read_csv()` |
| JSON | API de fidelización | 5 | 4 | Python: `json.load()` + `pd.json_normalize()` / R: `fromJSON()` |
| Excel | Consolidado de Finanzas | 5 | 4 | Python: `pd.read_excel(sheet_name="ventas")` / R: `read_excel(sheet = "ventas")` |

**¿La estructura interna del archivo cambia el contenido?**

No. Se comprobó que los tres reportes contienen exactamente la misma información. En Python, las comparaciones mediante `DataFrame.equals()` devolvieron `True` para CSV–JSON y CSV–Excel. Por tanto, el formato cambia la forma de leer y procesar los datos, pero no su contenido.

## 2. Tipos de datos y calidad

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | `int64` | `num` (valores enteros) | Variable numérica que permite sumar y calcular promedios. |
| `clientes` | `int64` | `num` (valores enteros) | Variable numérica que representa el número de clientes. |
| `sucursal` | `object` | `chr` | Texto que identifica el nombre de cada sucursal. |
| `region` | `object` | `chr` | Variable categórica almacenada como texto; contiene las categorías Sierra y Costa. |

Los tipos inferidos fueron los esperados para las variables analizadas. No se encontraron señales de datos sucios en la entrega.

**¿Qué habría indicado un dato sucio si `ventas` llegara como texto?**

Si `ventas` se leyera como texto (`object` en Python o `chr` en R), podría indicar la presencia de símbolos monetarios, separadores de miles, espacios o valores como `N/A`. Esto dificultaría las operaciones matemáticas y sería necesario limpiar y convertir la columna a un tipo numérico antes de calcular indicadores.

## 3. Particularidades técnicas encontradas

- **CSV:** fue el formato más sencillo de leer. En Python se utilizó `pd.read_csv()` y en R `read_csv()`. No fue necesario realizar transformaciones adicionales para obtener la tabla.
- **JSON:** en Python, `json.load()` devolvió una lista de diccionarios que se transformó en una tabla mediante `pd.json_normalize()`. En R, `fromJSON()` convirtió directamente el contenido en un `data.frame`.
- **Excel:** el libro contenía una sola hoja llamada `ventas`, que se indicó explícitamente al leerlo. En Python se utilizó `pd.read_excel()` con `sheet_name="ventas"` y se necesitó la biblioteca `openpyxl`. En R se empleó `read_excel()` con `sheet = "ventas"`.

En cuanto a las variables categóricas, Python las identificó como `object` y R como `chr`, es decir, texto. Aunque representan categorías, no se convirtieron a tipos categóricos específicos porque no fue necesario para este análisis.

## 4. Indicadores para la reunión del lunes

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | 12 008 |
| Ticket promedio (ventas ÷ clientes) | 38,29 (promedio simple de los tickets por sucursal) |
| Sucursal con mayor venta | Guayaquil Centro (15 200) |
| Sucursal con menor venta | Cuenca (8 540) |
| Región con mayor venta total | Sierra (30 860; frente a 29 180 de la Costa) |

**Nota sobre el ticket promedio:** el promedio simple de los cinco tickets por sucursal es 38,29. Si se divide la suma de las ventas para el total de clientes, el resultado es 38,07. Este último representa el ticket promedio global ponderado por el número de clientes.

Además, aunque la Sierra registra la mayor venta total, tiene tres sucursales frente a las dos de la Costa. Por sucursal, la Costa presenta un promedio de ventas superior: 14 590 frente a 10 287 en la Sierra. Cuenca registra las menores ventas y cuenta con 210 clientes.

## 5. Conclusiones y recomendación

1. Los tres formatos contienen la misma información. CSV, JSON y Excel se leyeron como tablas de 5 filas y 4 columnas. Las comparaciones realizadas en Python devolvieron `True`, confirmando la igualdad del contenido.

2. Los tipos de datos fueron los esperados. Las variables `ventas` y `clientes` se reconocieron como numéricas, mientras que `sucursal` y `region` se identificaron como texto. No se detectaron problemas de calidad de datos en esta práctica.

3. Recomendación: estandarizar el reporte en CSV. Se leyó en una sola instrucción, sin aplanar como el JSON ni indicar hoja o instalar librerías extra como el Excel, y dio exactamente los mismos datos. 
