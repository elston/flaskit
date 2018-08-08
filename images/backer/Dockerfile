FROM python:3.6-slim-jessie
MAINTAINER Den Elston "elstton@yahoo.com"

# ...
RUN apt-get update && apt-get install -y --no-install-recommends locales
RUN sh -c "echo 'LANG="'"'"ru_RU.UTF-8"'"'"' > /etc/default/locale"
ENV LANG='ru_RU.UTF-8' LANGUAGE='ru_RU:ru' LC_ALL='ru_RU.UTF-8'
RUN localedef -i ru_RU -f UTF-8 ru_RU.UTF-8

# ...
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

# ...    
RUN apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
&&  pip install --upgrade \
    pip \
    virtualenv \
&& pip install \
    virtualenvwrapper \
&& pip install --upgrade \
    virtualenvwrapper

# RUN rm -rf /var/lib/apt/lists/*


#..
RUN touch ~/.bashrc \
&& echo " " >> ~/.bashrc \
&& echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

