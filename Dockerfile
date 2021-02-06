# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

# Install node
RUN apt update && apt install nodejs npm -y

# Install node requirements
COPY ./package.json /app/
COPY ./package-lock.json /app/
RUN npm install

# Install pip requirements
COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY . /app

# collect static
RUN python manage.py collectstatic --noinput
RUN python manage.py compress --force
RUN python manage.py collectstatic --noinput

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "church_site.wsgi"]
