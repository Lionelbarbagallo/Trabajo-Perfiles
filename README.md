# Social Network Profile Analysis

Bienvenido al repositorio del proyecto Social Network Profile Analysis!

Acá encontrarás todo el material necesario para entender nuestro proyecto, analizar y replicar los resultados.

Los archivos que puedes ver en el root del repositorio corresponden a la persistencia de los modelos generados. En la carpeta imágenes encontrarás las 
imágenes de perfiles utilizadas para entrenar y validar los modelos. En la carpeta labels encontrarás los archivos .txt que contienen las labels de cada imagen. En base a estos archivos se han preparado los datasets, que puedesen verlos en la carpeta honónima. Por último, en la carpeta
scripts hallarás el código de las funciones accesorias utilizadas en el proyecto y un Jupyter Notebook con el trabajo final de análisis de los datos,
construcción de los modelos y evaluación de los resultados. Este notebook se encuentra comentado con Insights y conclusiones respecto al avance del trabajo,
por lo que es recomendable su lectura. Siguiendo el siguiente link podrás acceder a una visualización On-Line de este notebook:

https://github.com/Lionelbarbagallo/Trabajo-Perfiles/blob/master/scripts/Social%20Network%20Profile%20Analysis.ipynb

Finalmente, si vas a descargar este repositorio tené en cuenta que aunque revisamos atentamente todos los path a las ubicaciones de archivos y capetas,
quizás algo pudo haberse pasado por alto! Así que si intentás replicar los resultados, cuidado y suerte!

# Sobre el proyecto

Estamos en un mundo que genera cada vez mayor cantidad de datos. Entre ellos, los datos no estructurados tienden a ganar relevancia. Y dentro de los datos no estructurados, la proliferación de información bajo la forma de imágenes es una de las tendencias centrales. De forma creciente, nuestra vida tiende a quedar registrada en imágenes, ya sea a través de las redes sociales, o mediante imágenes captadas en entornos públicos.Y estas imágenes, cuentan una historia. Imitando el trabajo del antropólogo, o mejor dicho, trabajando como antropólogos de los medios digitales, el desarrollo de herramientas, métodos y frameworks para interpretar estas fuentes, permitirá generar importantes  insights sobre las tendencias y comportamientos sociales que las subyacen. Este es el campo más general - y ambicioso - en el que se despliega nuestro proyecto.

Como el título lo indica, este proyecto se focaliza en el estudio de las imágenes de los perfiles de redes sociales. Pero ¿Por qué estudiar las imágenes de los perfiles? ¿Cuál es su utilidad? En principio, estas imágenes poseen ciertas características que hacen valioso su estudio. En primer lugar, son grandes portadoras de significados sociales. Una imagen de perfil dista de ser aleatoria, si bien como veremos más adelante existe un nivel no despreciable de ruido en las distribuciones. En general, cuando un individuo elige una foto de perfil, realiza una evaluación racional y emocional de la misma, es decir, no son imágenes asépticas. La idea central es que la elección de una imagen de perfil representa una escala de valores, de comportamientos, y de experiencias de los individuos.

El objetivo específico del trabajo es llevar a cabo una prueba de concepto de los principios antes expuestos. En concreto, se busca desarrollar un modelo que permita la identificación del nivel socioeconómico de los individuos y poblaciones en base al análisis de las imágenes de perfiles. En este sentido, otras variables intervinientes, como edad y género, no serán tenidas en cuenta (al menos en la primera etapa de desarrollo). Si los resultados de esta primera etapa fuesen satisfactorios, más adelante se podría seguir complejizando el desarrollo de los modelos.

Si leiste hasta aquí probablemente estés interesado en el proyecto!!! En el Jupyter Notebook del proyecto podrás seguir leyendo acerca del diseño del experimento, la construcción de los datasets, la extracción de atributos y el entrenamiento y evaluación de los modelos. 


