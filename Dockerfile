FROM python:3
USER root

RUN apt update && apt install -y \
	locales 

	localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip && \
	pip  install --upgrade setuptools
RUN python -m pip install -y 
	jupyterlab \
	ipython
