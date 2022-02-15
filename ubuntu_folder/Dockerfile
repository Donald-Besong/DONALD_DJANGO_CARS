FROM ubuntu:18.04
MAINTAINER Donald Besong 
RUN apt-get clean
RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN apt-get -y install python3-distutils
RUN apt -y install python3
COPY python-pip.py /python-pip.py

RUN useradd remote_user && \
 echo 'remote_user:1234' | chpasswd
RUN mkdir -p /home/remote_user

RUN mkdir /home/remote_user/tmp && \
  chown remote_user:remote_user -R /home/remote_user/tmp
   
RUN chmod 666 -R /tmp

RUN apt -y install mysql-server 

RUN python3 /python-pip.py && \
   pip install awscli==1.22.9 --upgrade
   
CMD ["echo", "hello from remote-host, ubuntu"]

