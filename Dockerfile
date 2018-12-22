FROM python:3.6
EXPOSE 80/tcp
LABEL name="padorubot"
ADD padorubot.py /
ADD revsearch.py /
ADD dubstosubs.py /
ADD functions.py /
ADD config.py /
ADD musumecollection.py /
RUN pip install discord.py
RUN pip install requests
RUN pip install yandex-translater
CMD [ "python", "./padorubot.py" ]
