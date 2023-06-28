FROM python:3.10

EXPOSE 5000

WORKDIR /src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY /src .

# CMD [ "flask", "--app", "app", "run" ]
CMD ["flask", "run", "--host", "0.0.0.0"]