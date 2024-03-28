from airflow import DAG
from pendulum import yesterday
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
import requests
from hdfs import InsecureClient
import os
import csv

def fetch_and_save_data():
        startpage = ['1','1000','2000']
        endpage  = ['999','1999','2999']
        now_time = datetime.now().strftime('%Y%m%d_%H%M')

        with open(f'/home/ktu//airflow_data/air02/{now_time}.csv', 'w', newline='', encoding='utf-8-sig') as  f:
                            writer = csv.writer(f)
                            headers_written = False  # 헤더를 한 번만 쓰기 위한 변수

                            for x,y in zip(startpage,endpage):
                              api_url ="http://openapi.seoul.go.kr:8088/664c747774656f6e3130384667614e49/json/bikeList/"+x+"/"+y+"/"
                              response = requests.get(api_url)
                              data = response.json()
                              bike_info = data['rentBikeStatus']['row']
                              for obj in bike_info:
                                  obj["datetime"] = now_time
 
                              if not headers_written:
                                  headers = list(bike_info[0].keys())
                                  writer.writerow(headers)
                                  headers_written = True

                              for row in bike_info:
                                row_value = list(row.values())
                                writer.writerow(row_value)

        return f'/home/ktu//airflow_data/air02/{now_time}.csv'

def save_to_hdfs(csv_filename):
	# HDFS 클라이언트 초기화
	hdfs_client = InsecureClient('http://localhost:50070', user='hadoop')

	# 로컬 CSV 파일을 HDFS에 복사
	hdfs_path = '/air02/'
	hdfs_client.upload(hdfs_path, csv_filename, overwrite=True)

def clear_dir():
          dir = '/home/ktu/airflow_data/air02/'
          file_list = os.listdir(dir)
          for filename in file_list:
                file_path = os.path.join(dir, filename)
                os.remove(file_path)

default_args={
       'owner':'airflow',
       'depends_on_past':False,
       'start_date':datetime(224,3,26),
       'email_on_failure':False,
       'email_on_retry':False,
       'retries':1,
       'retry_delay':timedelta(minutes=5)
}

dag = DAG(
    	dag_id="air02",
        start_date=yesterday("Asia/Seoul"),
        schedule_interval=timedelta(minutes=5),
        catchup=False
)

fetch_data_task = PythonOperator(
    	dag=dag,
    	task_id='fetch_data',
    	python_callable=fetch_and_save_data
)

save_to_hdfs_task = PythonOperator(
    	dag=dag,
    	task_id='save_to_hdfs',
    	python_callable=save_to_hdfs,
    	op_kwargs={'csv_filename': fetch_data_task.output}
)

clear_dir_task = PythonOperator(
               dag=dag,
               task_id='clear_dir',
               python_callable=clear_dir
)

fetch_data_task >> save_to_hdfs_task >> clear_dir_task
