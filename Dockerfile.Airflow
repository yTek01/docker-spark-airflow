FROM apache/airflow:2.2.5-python3.8
USER root

# Install OpenJDK-11
RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow

COPY ./requirements.txt /
RUN pip install -r /requirements.txt

COPY --chown=airflow:root ./dags /opt/airflow/dags