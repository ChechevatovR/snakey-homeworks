FROM python:3.14-trixie
LABEL authors="chechevatov"

RUN apt update
RUN apt install -y texlive
RUN pip install pdflatex
RUN pip install -i https://test.pypi.org/simple/ python-course-homework-assignments-4438cfe6-9036-4c32-b279-ff960332732a

COPY main.py main.py
COPY resources resources
RUN mkdir "artifacts"

ENTRYPOINT ["python", "main.py"]
