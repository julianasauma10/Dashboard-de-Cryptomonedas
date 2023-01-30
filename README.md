# Dashboard-de-Cryptomonedas
Proyecto Final de Python
# Memoria Dashboard de Criptomonedas

El presente documento tiene como propósito describir los detalles del proyecto final del curso "Python para Análisis de Datos (MBDS)". Este proyecto consiste en la creación de un dashboard de información sobre criptomonedas. Es importante mencionar que aunque este documento hace referencia a un código escrito en PyCharm, no debe ser considerado un código ejecutable, sino más bien una memoria ilustrativa de los trabajos realizados.

Asimismo, es necesario destacar que la herramienta utilizada en este proyecto, llamada "streamlit", es una biblioteca de Python que ofrece una interfaz intuitiva para crear gráficos, tablas, formularios y otros elementos. Para que funcione correctamente, el código debe ser ejecutado en un servidor local o en un ambiente en la nube, y acceder a través de un navegador web. De lo contrario, el resultado puede no ser el esperado. Cabe destacar que, una de las desventajas que tiene la librería de streamlit es que se tiene que trabajar sobre los archivos .py, de otra forma puede traer problemas al momento de ejecutar el código.

El código que se presenta a continuación realiza un análisis técnico de los precios de una criptomoneda en particular, utilizando la API de Kraken. Este análisis incluye un gráfico de precios, la media móvil y un gráfico que muestra el indicador técnico RSI.

**1. Instalación de paquetes**

El primer paso del proyecto es la instalación de librerías para poder llevar a cabo su ejecución. Para poder llevarlo a cabo, las librerías instaladas en el entorno virtual son las siguientes:
pandas
krakenex
Streamlit
plotly
pykrakenapi

Para realizar la instalación de las librerías se escribió el siguiente código:
![imagen1](ruta/a/la/imagen.jpg)

Luego, el siguiente paso fue importarlas de la siguiente forma:


Estas librerías fueron instaladas para cumplir las siguientes funciones:
pykrkaenapi: son de utilidad para la conexión a la API de kraken
krakenex: descarga de datos OHLC
pandas: manipulación y creación de DataFrames
streamlit: para la creación de los gráficos

**2. Conexión a la API de Kraken**
Para poder realizar correctamente el proyecto es necesario conectarse a la API de kraken con la librería de krakenex, de esta forma se pueden hacer uso de sus funciones y descargar los datos. Para conectarse de forma correcta el código utilizado fue el siguiente:



En el código anterior, se puede ver que se utiliza la función de try y except para manejar posibles errores en la conexión con la API de Kraken. La parte try intenta conectarse a la API y si encuentra un error, en lugar de detener la ejecución del programa, pasa al bloque except y muestra un mensaje de error al usuario, informando sobre el problema en la conexión con la API.

**3. Selección de criptomoneda**
A continuación, se genera un bucle "FOR" para seleccionar solo los pares de criptomonedas que deseamos ver en la conversión, ya sea dólares (USD) o ethereum (ETH). Además, se permite seleccionar el intervalo de tiempo, que está limitado a 5, 60, 1440 (que corresponde a minutos), con el siguiente código:



**4. Cálculo de RSI**
El Relative Strength Index (RSI) es un indicador técnico utilizado para evaluar la fortaleza o debilidad relativa de un activo financiero. Para calcular el RSI, es necesario primero calcular el Relative Strength (RS). El RS se obtiene a través del siguiente proceso:

Promedio ganadoPromedio perdido

Una vez que se ha obtenido el valor del Relative Strength (RS) para cada período, se puede calcular el Relative Strength Index (RSI) de cada criptomoneda de la siguiente manera:

RSI = 100 - 1001 + RS

Teniendo en cuenta lo anterior, se agregó una función para el cálculo correspondiente del Relative Strength Index (RSI). La función recoge los valores de df (datos históricos del precio de cierre), periods (el número de períodos a considerar para calcular las medias móviles) y ema (una bandera que indica si se debe calcular una media móvil exponencial o simple para el RSI). De esta manera, se asegura que el cálculo del RSI se realice de manera eficiente y precisa. La función quedó definida de la siguiente manera:



**5. Descarga de datos**
El código presenta un bloque de try-except que tiene como objetivo descargar datos de precios para un par de criptomonedas específico usando la API de Kraken. El par de criptomonedas y el intervalo de tiempo se seleccionan previamente por el usuario y se almacenan en las variables "seleccion_criptomonedas" y "seleccion_interval", respectivamente.

El bloque try ejecuta la función "k.get_ohlc_data" para descargar los datos OHLC (Open, High, Low, Close) para la criptomoneda seleccionada y el intervalo de tiempo especificados. Los datos se almacenan en una variable llamada "ohlc".

En caso de que ocurra un error durante la descarga de datos, el bloque except se activará y se imprimirá un mensaje de error en la pantalla "Error al obtener datos de la criptomoneda seleccionada".

Después de descargar los datos, se crea un DataFrame en Pandas llamado "df" y se le asigna los datos contenidos en "ohlc[0]". Finalmente, se utiliza el método "reset_index" para restablecer el índice de "df" y guardar los cambios en el mismo objeto.

Se demuestra de la siguiente manera:



**6. Creación de gráficos**


De acuerdo con la imagen anterior se conta que:

En el primer bloque de código crea un gráfico de velas utilizando los datos almacenados del dataframe llamado df. La x axis es la fecha (df['dtime']), mientras que los precios de apertura, máximo, mínimo y cierre se definen por open=df['open'], high=df['high'], low=df['low'], close=df['close']. El título del gráfico y los nombres de los ejes x e y se actualizan con el título del gráfico y el nombre de la criptomoneda seleccionada (seleccion_criptomonedas). Se representa del color Verde/Rosa

El segundo bloque de código agrega una media móvil (media de los precios de cierre en una ventana de 14 períodos) al gráfico. En el gráfico se representa de color azul.

El tercer bloque de código crea un gráfico adicional llamado "RSI", el título del gráfico y los nombres de los ejes x e y también se actualizan. La información que representa se recogen de la función RSI, mencionada anteriormente. En el gráfico se representa del color rojo.

**7. Visualización de gráficas**
Para poder visualizar las dos gráficas, se ocupó la librería de streamlit st.plotly_chart y se distribuye de la siguiente manera:

En el primer llamado, se pasa la variable "fig" para mostrar un gráfico de velas y una línea de media móvil. En el segundo llamado, se pasa la variable "fig_rsi" para mostrar un gráfico de línea que muestra el valor del indicador "RSI" (RSI) para la criptomoneda seleccionada. Ambas gráficas contienen información de la criptomoneda seleccionada, fecha y título adecuado.

Se demuestra a continuación el código de lo mencionado anteriormente.


**8. Visualización final**



**9. Observaciones**
La aplicación presenta un problema que consiste en que cuando se desea cambiar el intervalo de tiempo o la selección de la criptomoneda, la actualización de la gráfica tarda unos segundos en refrescar. Esto es debido a que hay una cantidad significativa de información que debe ser procesada, por ejemplo, el total de monedas en USD/ETH. Además, el cálculo del indicador técnico RSI también es lento, por lo que para mejorar este aspecto, se puede implementar la función de RSI para que se guarde en la caché de nuestro ordenador. Con esta solución, se acelerará el procesamiento de la información y se mejorará la experiencia.


**Referencias**
(2023). Obtenido de Plotly: https://plotly.com/python/candlestick-charts/
Fernando, J. (15 de julio de 2022). Obtenido de Investopedia: https://www.investopedia.com/terms/r/rsi.asp
Martin Villaverde, G. (2022). Streamlit.
Mitchell, C. (1 de abril de 2021). Obtenido de The balance: https://www.thebalancemoney.com/use-relative-strength-to-find-the-best-day-trades-1030883


