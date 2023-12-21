FROM jekap1chenka/for_server_test:1.0

RUN apt-get install -y ffmpeg

COPY /bot /project
WORKDIR /project

RUN pip install -r requirements.txt

RUN chmod -R 777 .

ENTRYPOINT [ "python3", "main.py" ]