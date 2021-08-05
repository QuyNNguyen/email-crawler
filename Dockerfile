FROM python:3




ADD act2.py /
RUN pip install beautifulsoup4
CMD [ "python", "./act2.py" ]