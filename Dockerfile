FROM mrismanaziz/man-userbot:buster

RUN git clone -b TRANS-BOT https://github.com/RyuuXS/TRANS-BOT /home/trans-bot/ \
    && chmod 777 /home/trans-bot \
    && mkdir /home/trans-bot/bin/

COPY ./sample_config.env ./config.env* /home/trans-bot/

WORKDIR /home/trans-bot/

CMD ["python3", "-m", "userbot"]
