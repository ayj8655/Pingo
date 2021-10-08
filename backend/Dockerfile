FROM python:3.7
WORKDIR /usr/src/app

## Install packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Copy all src files
COPY . .

## Run the application on the port 8080
EXPOSE 8000

# python3 명령어
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "backend.asgi:application"]
