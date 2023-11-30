FROM ubuntu:latest

ENV USER ctf 
WORKDIR /home/$USER

RUN groupadd -r ctf && useradd -r -g ctf ctf

RUN apt-get update && apt-get install -yqq socat
RUN apt-get install sudo
RUN apt-get install -yqq python3
RUN apt-get install -yqq python3-pip
RUN pip3 install flask
RUN apt-get install -yqq curl

COPY src/ .
COPY flag.txt . 

RUN chmod 400 flag.txt

# PE
#RUN crontab /etc/cron.d/check_cron
RUN mkdir -p /etc/sudoers.d
RUN echo "ctf ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/ctf

USER ctf 

CMD python3 __init__.py
