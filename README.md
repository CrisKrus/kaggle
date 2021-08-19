# Kaggle

Lugar donde guardar notas de los directos de 100 horas de datos. Estos directos
los hago en [Twitch]. Además de esto, cada sesión la subo al canal de
[youtube de directos][youtube-directos] dentro de una
[lista de reproducción][lista-directos]

## Sesiones

0. [Repasando Python](00-Repasando-python)
1. [Introducción data visualization](01-Data-visualization)
2. [Trabajamos por nuestra cuenta con el dataset de ventas de videojuegos](02-video-game-sales)
3. [Manipulación de datos con Pandas](03-Pandas)
4. [Modificamos nuestro anterior notebook para trabajar con pandas](04-video-game-sales-with-pandas/videogames-sales.html)
5. [Buscamos datos públicos de Open data y los analizamos](05-open-data)
6. [Data Cleaning](06-data-cleaning)
7. [Intro a machine learning](07-intro-to-machine-learning)
8. [Pycaret](08-pycaret)

## Trabajar en local

Para poder trabajar en local necesitarás tener jupyter notebook instalado. Pero,
no te preocupes he creado una imagen de docker para que puedas arrancarlo sin
muchas complicaciones. Para ello ejecuta el siguiente script:

```shell
sh ./run.sh
```

Esto internamente crea y arranca una imagen de Docker montando el directorio
actual en el contenedor para persistir los cambios en esta misma carpeta.

## Trabajar en la nube

Si quieres trabajar con los notebooks en la nube existen tres alternativas que
yo conozca.

- [Kaggle][kaggle]
- [Google Colab][google-colab]
- [Jupyter notebook][try-jupyter]

## Redes sociales

No olvides que puedes seguirme o preguntarme lo que quieras por mis redes sociales!

- [Blog ✍🏼][blog]
- [Twitch 📺][Twitch]
- [Instagram 📷][instagram]
- [Youtube directos 📺🎥][youtube-directos]

<!-- LINKS -->

[instagram]:http://bit.ly/cristian-suarez-instagram
[blog]:http://bit.ly/cristian-suarez-blog
[youtube]:http://bit.ly/cristian-suarez-youtube
[Twitch]:https://www.twitch.tv/cristian_suarez_dev
[youtube-directos]:http://bit.ly/cristian-suarez-directos
[lista-directos]:https://www.youtube.com/playlist?list=PLZh1qmaTeQ-qvyJ9GOLNEwESIGTQdHAoI
[try-jupyter]:
https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/master?urlpath=lab/tree/demo
[google-colab]:https://colab.research.google.com/
[kaggle]:https://www.kaggle.com/code