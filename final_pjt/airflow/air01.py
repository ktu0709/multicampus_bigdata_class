from airflow import DAG
from pendulum import yesterday
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
import requests
from hdfs import InsecureClient
import csv
import os

def _is_json_key(json, key):
    try:
        tmp = json[key]
    except KeyError:
        return False
    return True

def fetch_json_and_convert_to_csv():

    date = datetime.today() - timedelta(1)
    date = date.strftime("%Y%m%d")

    with open(f'/home/ktu/airflow_data/air01/{date}.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        headers_written = False  # 헤더를 한 번만 쓰기 위한 변수

        for i in range(0, 24):
                api_url =f"http://openapi.seoul.go.kr:8088/key/json/tbCycleRentUseTimeInfo/1/999/{date}/{i}"
                response = requests.get(api_url)
                res = response.json()
                if(_is_json_key(res,'cycleRentUseTimeInfo') == True):
                        data = res['cycleRentUseTimeInfo']['row']
                        if not headers_written:  # 헤더를 한 번만 쓰기
                            headers = list(data[0].keys())
                            writer.writerow(headers)
                            headers_written = True

                        for row in data:
                            row_value = list(row.values())
                            writer.writerow(row_value)
                else:
                   continue
    return f'/home/ktu/airflow_data/air01/{date}.csv'

def save_to_hdfs(csv_filename):
    # HDFS 클라이언트 초기화
    hdfs_client = InsecureClient('http://localhost:14000', user='ktu')

    # 로컬 CSV 파일을 HDFS에 복사
    hdfs_path = '/air01/'
    hdfs_client.upload(hdfs_path, csv_filename, overwrite=True)


def clear_dir():
          dir = '/home/ktu/airflow_data/air01/'
          file_list = os.listdir(dir)
          for filename in file_list:
                file_path = os.path.join(dir, filename)
                os.remove(file_path)

dag = DAG(
	dag_id="air01",
	schedule_interval="0 8 * * *",
	start_date=yesterday("Asia/Seoul")
)

fetch_data_task = PythonOperator(
        dag=dag,
        task_id='fetch_data',
        python_callable=fetch_json_and_convert_to_csv
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
