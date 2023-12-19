FROM jekap1chenka/for_server_test:1.0

RUN apt-get install -y ffmpeg

COPY . /project
WORKDIR /project

RUN pip install -r requirements.txt

RUN chmod -R 777 bot
RUN chmod 777 script.sh

ENTRYPOINT ["bash", "script.sh"]