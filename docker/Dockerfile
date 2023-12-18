FROM jekap1chenka/for_server_test:1.0


RUN apt-get install -y ffmpeg
RUN pip install aiogram==2.22.1
RUN pip install SpeechRecognition==3.8.1


COPY . /project
WORKDIR /project

#ENTRYPOINT ["python3", "bot/main.py"]
#ENTRYPOINT ["ls", "-R"]