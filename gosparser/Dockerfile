FROM python:3.9-slim

RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc build-essential  && \
  apt-get autoremove -y


RUN pip3 install pipenv

COPY Pipfile ./gosparser/
COPY Pipfile.lock ./gosparser/

#RUN cd gosparser/ && pipenv install
RUN cd /gosparser && pipenv lock --requirements > requirements.txt 
RUN cd /gosparser && pip install -r requirements.txt

COPY . ./gosparser

# set working directory
WORKDIR /gosparser

#EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]