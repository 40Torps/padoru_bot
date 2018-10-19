FROM python:3.6
ADD padorubot.py /
ADD revsearch.py /
ADD config.py /
RUN pip install discord.py
RUN pip install requests
CMD [ "python", "./padorubot.py" ]
