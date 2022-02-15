FROM python:3.7.2-slim

ENV PYTHONDONTRUNBYTECODE 1
ENV PYTHONBUFFERED 1

RUN mkdir /app
RUN mkdir /usr/myproject/
WORKDIR /app
RUN apt-get update
RUN apt-get clean

RUN apt install python3-pip -y
RUN apt install default-libmysqlclient-dev -y
RUN apt install build-essential 
RUN pip3 install --upgrade pip 
RUN pip3 install virtualenv 

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
COPY ./myproject/ /usr/myproject/
RUN chmod u+x /usr/myproject/activate_env3.sh
RUN chmod u+x /usr/myproject/re_activate_env3.sh
         
CMD ["echo", "test hello from Django"]
