# Kaggle
Lugar donde guardar notas de los directos de 100 horas de datos. Estos directos
los hago en [Twitch]. Además de esto, cada sesión la subo al canal de 
[youtube de directos][youtube-directos] dentro de una 
[lista de reproducción][lista-directos]

# Sesiones

1. [Repasando Python](00-Repasando-python)
2. [Introducción data visualization](01-Data-visualization)

# Trabajar en local

Para poder trabajar en local necesitarás tener jupyter notebook instalado. Pero,
no te preocupes he creado una imagen de docker para que puedas arrancarlo sin
muchas complicaciones. Para ello ejecuta los siguientes comandos:

1. `docker build -t criskrus/jupyter -f .docker/jupyter/Dockerfile .`
2. `docker run --rm --user root -p 8888:8888 -v $(pwd):/home/cristian.suarez/notebooks -e NB_UID=$(id -u) -e NB_GID=$(id -g) criskrus/jupyter`
3. En el terminal apareceran enlaces para poder acceder a jupyterlab sin problema, deben de ser similares a este `https://127.0.0.1:8888/lab?token=e823c5883ce7a1196249c94cc3ad14afa6a608bc58a4c00d`

## Redes sociales

No olvides que puedes seguirme o preguntarme lo que quieras por mis redes sociales!

- [Instagram 📷][instagram]
- [Blog ✍🏼][blog]
- [Twitch 📺][Twitch]
- [Youtube 🎥][youtube]
- [Youtube directos 📺🎥][youtube-directos]

[instagram]:http://bit.ly/cristian-suarez-instagram
[blog]:http://bit.ly/cristian-suarez-blog
[youtube]:http://bit.ly/cristian-suarez-youtube
[Twitch]:http://bit.ly/cristian-suarez-twitch
[youtube-directos]:http://bit.ly/cristian-suarez-directos
[lista-directos]:https://www.youtube.com/playlist?list=PLZh1qmaTeQ-qvyJ9GOLNEwESIGTQdHAoI
