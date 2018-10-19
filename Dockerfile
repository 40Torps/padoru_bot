FROM python:3.6
EXPOSE 80/tcp
LABEL name="padorubot"
ADD padorubot.py /
ADD revsearch.py /
ADD config.py /
RUN pip install discord.py
RUN pip install requests
CMD [ "python", "./padorubot.py" ]
