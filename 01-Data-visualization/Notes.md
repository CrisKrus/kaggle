
- [x]  diferencia entre variables discretas y [categoricas](https://en.wikipedia.org/wiki/Categorical_variable)

    Las variables cuantitativas pueden clasificarse como discretas o continuas.

    **Variable categórica o cualitativa**

    Las variables categóricas contienen un número finito de categorías o grupos distintos. Los datos categóricos pueden no tener un orden lógico. Por ejemplo, los predictores categóricos incluyen sexo, tipo de material y método de pago.

    **Variable discreta**

    Las variables discretas son variables numéricas que tienen un número contable de valores entre dos valores cualesquiera. Una variable discreta siempre es numérica. Por ejemplo, el número de quejas de los clientes o el número de fallas o defectos.

    **Variable continua**

    Las variables continuas son variables numéricas que tienen un número infinito de valores entre dos valores cualesquiera. Una variable continua puede ser numérica o de fecha/hora. Por ejemplo, la longitud de una pieza o la fecha y hora en que se recibe un pago.

- [x]  ordenar las graficas de barras en nuestro notebook
- [ ]  grafico de tartas para categorias por consola
- [ ]  articulo con definiciones de terminos
- [x]  swarm plot
- [x]  revisar histograma y el resto de distribución
- [x]  que es un bin (intervalos?)

---

Definition 1: a correlation is defined as a measure (a metric) to evaluate the relationship between two variables. You can calculate (using an equation) the correlation coefficient that takes values between 1 to -1: a value close to 0 indicates no correlation; a value close to 1 indicates a very strong direct relationship between the two variables; a value close to -1 indicates a very strong inverse relationship between them; values greater than 0.7 or -0.7 indicate, respectively, strong direct or inverse relationships; values below 0.3 or -0.3 indicate weak or null direct or inverse relationships.

Definition 2: a categorical variable, also called qualitative variable, is one that usually takes a limited number of values of mutually exclusive categories or groups. These values can be numerical but do not represent quantities but mutually exclusive groups (i.e. gender: 1- Male; 2- Female; 3- Other).

[https://medium.com/analytics-vidhya/scatter-plots-why-how-3de6e1e32645](https://medium.com/analytics-vidhya/scatter-plots-why-how-3de6e1e32645)

---

[Histograms vs. Bar Charts](https://www.investopedia.com/terms/h/histogram.asp)

Both histograms and bar charts provide a visual display using columns, and people often use the terms interchangeably. More technically, a histogram represents the frequency distribution of variables in a data set. On the other hand, a bar graph typically represents a graphical comparison of discrete or categorical variables.

---

- Tendencias
    - lineas
        - util para ver tendencias a lo largo del  tiempo
        - no poner mas de 5 lineas o los valores no se comprenderan
        - no partir de cero si no es necesario o [no aporta valor al gráfico](https://chartio.com/assets/7119e1/tutorials/charts/line-charts/8170bced5eea17b515870105e3bf4011df66e98a5bd9851d5c9a147a81f5acee/line-chart-misuses-1.png)
        - [ridgeline plot](https://chartio.com/learn/charts/line-chart-complete-guide/#ridgeline-plot)
- Relacion
    - barras
        - util cuando la agrupacion no es periodica (tiempo) o ordenable (numerica) por ejemplo generos de videojuegos
        - para comparativa entre categorias de los datos
        - [se puede poner valores negativos para mostrar la diferencia en ambos sentidos](https://www.chartblocks.com/en/support/faqs/faq/when-to-use-a-bar-chart)
        - empezar desde cero en el eje vertical
        - ordenar los datos hace que se vea mejor los valores y comparativa
        - no usar colores aleatorios para todas las barras, poner color en donde queremos que tenga importancia
        - [graficas verticales molan mas](https://chartio.com/learn/charts/bar-chart-complete-guide/#horizontal-bars-vs-vertical-bars)
        - [incluir anotaciones de valores](https://chartio.com/learn/charts/bar-chart-complete-guide/#include-value-annotations), poner dentro de la barra el valor que toma
    - mapa de calor
        - ordenar
        - [correlogram](https://chartio.com/learn/charts/heatmap-complete-guide/#correlogram)
    - scatter plot
        - graficos de puntos
        - son utiles para [explorar relaciones entre datos](https://www.pluscharts.com/scatter-charts/), por ejemplo accidentes de coche con velocidad del mismo
        - se puede añadir una clasificación con el color de los puntos
        - util para explorar datos y descubrir relaciones
        - cuidado con el overplotting, superponer muchos puntos, perdidad de vision de los datos
            - solucion poner transparencia para ver la intensidad de la superposición
            - usar un mapa de calor en su lugar
        - cuidado con las interpretaciones de este tipo de gráficos, como vemos una correlación entre los datos [podemos pensar que hay una causualidad](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation) y no tiene porque ser de esta forma
        - añadir una línea de tendencias es típico y útil
        - podemos darle mayor tamaño a los puntos que según su peso (si lo tienen)
    - categorical scatter plot aka swarm plot
        - show the relationship between a continuous variable and a categorical variable
        - solucion cuando hay muchos puntos en un mismo punto en un scatter plot
- Distribucion
    - histogramas
        - muestra una distribución de un valor único numérico
        - [https://corporatefinanceinstitute.com/resources/excel/study/histogram/](https://corporatefinanceinstitute.com/resources/excel/study/histogram/)
        - agrupa valores por rangos que indicamos en lugar de puntos concretos
        - las barras de un histograma no se pueden ordenar segun el peso o romperia el  sentido del grafico porque no veriamos la continuacion de los intervalos
        - bin —> rango que cubre cada barra del histograma bin o clase
    - [KDE kernel density estimate](https://ajaytech.co/2020/05/03/kdeplots/#kernel-density-estimate)
        - is another widely used technique for estimating the distribution of data
        - [https://i0.wp.com/ajaytech.co/wp-content/uploads/2020/05/KDEplot.png?w=1091&ssl=1](https://i0.wp.com/ajaytech.co/wp-content/uploads/2020/05/KDEplot.png?w=1091&ssl=1)

- diferencia entre dataFrame y serie en pandas
    - dataframe es un array de dos dimensiones donde cada columna puede ser un tipo de dato diferente (int, str, etc)
    - una serie es un array de una dimesion donde cada campo (comlumna) puede ser de un tipo
    - un dataframe viene a ser una colección de series
    - en python los array de una o dos dimensiones tienen que tener los valores siempre del mismo tipo
