FROM jupyter/minimal-notebook

ENV JUPYTER_ENABLE_LAB=yes
ENV NB_USER=cristian.suarez
ENV GRANT_SUDO=yes
ENV CHOWN_HOME=yes
ENV CHOWN_HOME_OPTS='-R'
ENV GEN_CERT=yes

# Create conda environment
ARG conda_env=python36
ARG py_ver=3.6

WORKDIR /home/$NB_USER/notebooks

RUN conda create --quiet --yes -p "${CONDA_DIR}/envs/${conda_env}" python=${py_ver} ipython ipykernel && \
    conda clean --all -f -y

# create Python 3.6 environment and link it to jupyter
RUN "${CONDA_DIR}/envs/${conda_env}/bin/python" -m ipykernel install --user --name="${conda_env}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"


# Install dependencies
COPY --chown=${NB_UID}:${NB_GID} requirements.txt ./
RUN conda install --yes --file requirements.txt && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

COPY . .

# prepend conda environment to path and set to default
ENV PATH "${CONDA_DIR}/envs/${conda_env}/bin:${PATH}"
ENV CONDA_DEFAULT_ENV ${conda_env}

EXPOSE 8888
USER $NB_UID
