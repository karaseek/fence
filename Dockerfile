FROM python:3

WORKDIR /usr/src/textcorrupt

RUN pip install pyTelegramBotAPI

COPY bot.py .

COPY config ./config

COPY corrupt ./corrupt

CMD ["python", "bot.py"]