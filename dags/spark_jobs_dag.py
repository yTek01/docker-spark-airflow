
import airflow
from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',    
    'retry_delay': timedelta(minutes=5),
}

Spark_docker_dag = DAG(
        dag_id = "Spark_DAG",
        default_args=default_args,
        schedule_interval='@daily',	
        dagrun_timeout=timedelta(minutes=60),
        description='Run Spark containers using the Docker Operator',
        start_date = airflow.utils.dates.days_ago(1)
)

start = DummyOperator(task_id="start", dag=Spark_docker_dag)

Extract = DockerOperator(
    task_id='spark_docker_runner.Extract',
    container_name='spark_container',
    image='spark-air:latest', 
    command='spark-submit --master spark://master:7077 spark_etl_script_docker.py', 
    docker_url='unix://var/run/docker.sock', 
    network_mode='bridge', 
    xcom_all=True, 
    auto_remove=True, 
    mount_tmp_dir=False,
    dag=Spark_docker_dag
)

end = DummyOperator(task_id="end", dag=Spark_docker_dag)
start >> Extract >> end
