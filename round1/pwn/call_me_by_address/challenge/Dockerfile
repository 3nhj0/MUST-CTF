# sudo docker build -t call_me_by_address .
# sudo docker run -p 10000:10000 call_me_by_address:latest

FROM ubuntu:22.04

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt install gcc xinetd make cowsay -y

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY Makefile /src
COPY ./src/flag.txt /
COPY ./src/call_me_by_address.c /src
COPY run.sh /src

RUN make

RUN chmod 444 /flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash", "/src/run.sh"]
EXPOSE 10000