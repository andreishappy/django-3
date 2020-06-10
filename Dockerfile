FROM python:3.7

COPY ./requirements.txt  /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /code/
WORKDIR /code/
ADD . /code/

# uWSGI will listen on this port
EXPOSE 8000

# Change the user from root to the app user
# Create a group and user to run our app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}
USER ${APP_USER}:${APP_USER}
