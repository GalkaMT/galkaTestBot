FROM python:3-slim
ENV TOKEN='place your token here'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py