FROM ubuntu:latest

ENV USER ctf 
WORKDIR /home/$USER 

RUN groupadd -r ctf && useradd -r -g ctf ctf

RUN apt-get update && apt-get install -yqq socat
RUN apt-get install -yqq python3

COPY src/serv.py . 
COPY flag.txt .
RUN chmod -wr flag.txt 
RUN chown ctf:ctf /etc/passwd
USER ctf 

CMD socat TCP-L:12001,fork,reuseaddr EXEC:"python3 serv.py",pty,ctty,stderr,echo=0