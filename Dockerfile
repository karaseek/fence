FROM python:3

WORKDIR /usr/src/textcorrupt

RUN pip install pyTelegramBotAPI

COPY src .

CMD ["python", "bot.py"]