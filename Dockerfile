FROM ubuntu:18.04
RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv python3-pip

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt $VIRTUAL_ENV
WORKDIR $VIRTUAL_ENV

RUN pip install -r requirements.txt

COPY app.py .
COPY tests.py .
LABEL author="STINSLEY"
ENTRYPOINT ["python", "app.py"]
CMD ['array1 ', 'array2' ]