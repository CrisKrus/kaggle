FROM jupyter/minimal-notebook

ENV JUPYTER_ENABLE_LAB=yes
ENV NB_USER=cristian.suarez
ENV GRANT_SUDO=yes
ENV CHOWN_HOME=yes
ENV CHOWN_HOME_OPTS='-R'
ENV GEN_CERT=yes

WORKDIR /home/$NB_USER/notebooks
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888
USER $NB_UID
