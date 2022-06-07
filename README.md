# Airflow and Spark: Running Spark jobs on Airflow (Docker-based solution)

Here in this repository, we have designed a simple ETL process that extract data from an API and we are transforming this data using Spark and loading this data into an AWS S3 bucket. We running this batch processes using Airflow by Spark job submit Operator in Airflow. All the processes described here are happening on a Docker containers. You can look at this [repository](https://github.com/yTek01/apache-airflow-spark) if you are interested in local deployment as opposed to Docker-based solution. 

## Things to do;

*  Clone the Github repository 
*  Build the Spark and the Airflow image
*  Create your dags, logs, plugins folder
*  Create your environment variable
*  Start and run the Spark and Airflow containers 
*  Run your Spark jobs to confirm if the Spark job completed successfully before moving it to Airflow 
*  Design the Airflow DAG to trigger and schedule the Spark jobs.

## Clone the Github repository.
```bash
git clone https://github.com/yTek01/docker-spark-airflow.git
```

## Build the Spark image.
```bash
docker build -f Dockerfile.Spark . -t spark-air
```

## Build the Airflow image.
```bash
docker build -f Dockerfile.Airflow . -t airflow-spark
```

## Create your dags, logs, plugins folder.
```bash
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

## Your environment variable would look like this.
```bash
AIRFLOW_UID=33333
AIRFLOW_GID=0
AWS_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXX
AWS_SECRET_KEY=XXXXXXXXXXXXXXXXXXXX
```

## Start and run the Spark and Airflow containers.
```bash
docker-compose -f docker-compose.Spark.yaml -f docker-compose.Airflow.yaml up -d
```
When all the services all started successfully, now go to http://localhost:8080/ to check that Airflow has started successfully, and http://localhost:8090/ that Spark is up and running. 


* Run your Spark jobs to confirm if the Spark job completed successfully before moving it to Airflow.

```bash
docker exec -it <Spark-Worker-Contianer-name> \
    spark-submit --master spark://XXXXXXXXXXXXXX:7077 \
    spark_etl_script_docker.py
```

If all is fine with the setup, i.e. the Spark job completed successfully, then move forward to scheduling the Spark job on Airflow. 