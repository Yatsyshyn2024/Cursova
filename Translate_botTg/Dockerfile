FROM python:3.10-slim
WORKDIR /bot
# Install python requirements
RUN pip install python-telegram-bot googletrans==4.0.0-rc1
COPY transbot.py /bot/transbot.py
CMD ["python", "transbot.py"]