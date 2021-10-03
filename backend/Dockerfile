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
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
