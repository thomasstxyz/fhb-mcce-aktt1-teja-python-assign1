# Assignment 1

Jupyter Notebook --> [notebooks/aktt1-teja-assignment1.ipynb](notebooks/aktt1-teja-assignment1.ipynb)



# Run Jupyter Notebook in Docker

    docker run --rm -i -t -p 8888:8888 -v ${PWD}/notebooks:/opt/notebooks continuumio/anaconda3 /bin/sh -c "\                                                  ─╯
        apt-get update && \
        apt-get install -y locales && \
        sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
        sed -i -e 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen && \
        dpkg-reconfigure --frontend=noninteractive locales && \
        conda install jupyter -y --quiet && \
        mkdir -p /opt/notebooks && \
        jupyter notebook \
        --notebook-dir=/opt/notebooks --ip='*' --port=8888 \
        --no-browser --allow-root"
