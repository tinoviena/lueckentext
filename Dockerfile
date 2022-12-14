FROM python:slim

COPY . .

RUN python3 -mpip install -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]