# sudo docker build -t register .
# sudo docker run -p 10003:10003 register:latest

FROM ubuntu:22.04

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt install gcc xinetd make cowsay -y

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY Makefile /src
COPY ./src/flag.txt /
COPY ./src/register.c /src
COPY run.sh /src

RUN make

RUN chmod 444 /flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash", "/src/run.sh"]
EXPOSE 10003