FROM python:3.8-slim

RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc build-essential  && \
  apt-get autoremove -y


RUN pip3 install pipenv

COPY Pipfile ./astra/
COPY Pipfile.lock ./astra/

#RUN cd gosparser/ && pipenv install
RUN cd /astra && pipenv lock --requirements > requirements.txt
RUN cd /astra && pip install -r requirements.txt

COPY . ./astra

# set working directory
WORKDIR /astra/app

#EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]