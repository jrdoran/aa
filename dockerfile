
FROM python:3.6
#From debian:testing

# Create app directory
WORKDIR /app





#Install latest patches
#RUN apt-get update && apt-get install -y \
#    && apt-get install -y wget 

#Obtain the package
#RUN wget http://downloads.sourceforge.net/vufind/vufind_3.1.1.deb?use_mirror=osdn -O vufind_3.1.1.deb

#Install it
#RUN dpkg -i vufind_3.1.1.deb

#Install VuFind's dependecies
#RUN apt-get install -y -f











# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app

EXPOSE 8080
CMD [ "python", "server.py" ]