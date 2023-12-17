FROM jekap1chenka/for_server_test:1.0

RUN pip install aiogram==2.22.1

COPY . /project
WORKDIR /project

ENTRYPOINT ["python3", "TELE_BOT/main.py"]
#ENTRYPOINT ["ls", "-R"]