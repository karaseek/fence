FROM python:3

WORKDIR /usr/src/textcorrupt

RUN pip install pyTelegramBotAPI

COPY __main__.py .

COPY config ./config

COPY corrupt ./corrupt

CMD ["python", "."]