import requests
import pandas as pd
import json
from datetime import datetime,timedelta
from airflow import DAG
from pendulum import yesterday
from airflow.operators.python_operator import PythonOperator
from hdfs import InsecureClient
import os
import csv

def get_weather():
    now_time = datetime.now().strftime('%Y%m%d_%H%M')
    date = now_time[0:8]
    hour = now_time[9:11]
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'    
    params ={'serviceKey' : 'l1DP/qWK5Y9nHd7cWOdMjVTLwd92c5a0xNf7WwiJUhZgHP0wZUjMuEfKZNJBLsZyiLFcU6QLumN1K6NrIzr6KA==', 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'json', 'base_date' : date, 'base_time' : hour+'00', 'nx' : 57, 'ny' : 127 }

    response = requests.get(url, params=params)
    now_time = datetime.now().strftime('%Y%m%d_%H%M')
    #print(response.status_code)
    
    res = response.json()
    data = res['response']['body']['items']['item']
    weather_df = pd.DataFrame(data)
    weather_df = weather_df.pivot(index=['baseDate', 'baseTime', 'nx', 'ny'], columns='category', values='obsrValue')
    weather_df = weather_df[['PTY','REH','RN1','T1H']]
    return weather_df


def get_bike_station():
    startpage = ['1','1000','2000']
    endpage  = ['999','1999','2999']
    stations = ['1124', '1153', '1158', '1160', '1166', '2701', '2715', '2721', '2728', '3798']
    now_time = datetime.now().strftime('%Y%m%d_%H%M')
    res_df = pd.DataFrame()


    for x,y in zip(startpage,endpage):
        api_url ="http://openapi.seoul.go.kr:8088/664c747774656f6e3130384667614e49/json/bikeList/"+x+"/"+y+"/"
        response = requests.get(api_url)
        data = response.json()
        bike_info = data['rentBikeStatus']['row']
        for obj in bike_info:
            obj["date"] = now_time[0:8]
            obj["time"] = now_time[9:13]
        
        df = pd.DataFrame(bike_info)
        res_df = pd.concat([res_df,df])

        
    station_name = list(res_df['stationName'])
    station_no =[]
    for i in station_name:
        test_list = i.split(".")
        station_no.append(test_list[0])

    res_df['station_no'] = station_no
    res_df = res_df[res_df['station_no'].isin(stations)]
    res_df.drop(columns=["stationId"])
    return res_df


def get_people():
    startpage = ['1','1000','2000','3000','4000','5000','6000','7000','8000','9000']
    endpage  = ['999','1999','2999','3999','4999','5999','6999','7999','8999','9999']
    sum_df = pd.DataFrame()
    res_df = pd.DataFrame()
    gangse_se = ['11500535','11500603','11500604','11500615','11500591'] 
    now_time = datetime.now().strftime('%Y%m%d_%H%M')
    hour = now_time[9:11]

    for x,y in zip(startpage,endpage):
        api_url ="http://openapi.seoul.go.kr:8088/664c747774656f6e3130384667614e49/json/SPOP_LOCAL_RESD_DONG/"+x+"/"+y+"///"
        #print(api_url)
        response = requests.get(api_url)
        res = response.json()
        data = res['SPOP_LOCAL_RESD_DONG']['row']
        df = pd.DataFrame(data)
        sum_df = pd.concat([sum_df,df])
    
    for i in gangse_se:
        gangse_df = sum_df[(sum_df['ADSTRD_CODE_SE'] == i) & (sum_df['TMZON_PD_SE'] == hour)]
        res_df = pd.concat([res_df,gangse_df])
    return res_df


def combine_df():
    weather_df = get_weather()
    bike_station_df = get_bike_station()
    people_df = get_people()
    station_info_df = pd.read_csv("따릉이대여소정보v2.csv")
    code_df = pd.read_csv("행정동코드.csv",encoding='cp949')

    code_df['H_DNG_CD']=code_df['H_DNG_CD'].astype('str')
    station_info_df['addr1'] = station_info_df['addr1'].str.replace(' ', '')
    code_df['addr1'] = code_df['addr1'].str.replace(' ', '')

    comb1 = pd.merge(left=station_info_df , right = code_df , how = "left" ,on ='addr1' )
    comb1['station_no']=comb1['station_no'].astype('str')
    comb2 = pd.merge(left=bike_station_df , right = comb1 , how = "left" ,on ='station_no' )
    comb3 = pd.merge(left=comb2 , right = people_df , how = "inner" ,left_on='H_DNG_CD', right_on='ADSTRD_CODE_SE' )
    comb4 = pd.merge(left=comb3 , right = weather_df , how = "inner" ,left_on='date', right_on='baseDate' )    
    
    res_df = comb4[['date','station_no','stationName_x','time','parkingBikeTotCnt','addr1','addr2','T1H','PTY','RN1','TOT_LVPOP_CO']]
    
    res_df.rename(columns={'date': '일시', 'station_no': '대여소번호','stationName_x': '대여소명','time': '시간대',
                       'parkingBikeTotCnt': '거치대수량','T1H': '기온','PTY': '강수형태','RN1': '강수량','TOT_LVPOP_CO': '총생활인구수'})

    file_name = res_df.iloc[0]['date'] + '_' + res_df.iloc[0]['time']+'.csv'
    #res_df.to_csv(file_name,encoding='utf-8-sig')
    res_df.to_csv(f'/home/ktu/airflow_data/air02/{file_name}',encoding='utf-8-sig')
    return f'/home/ktu/airflow_data/air02/{file_name}'


def save_to_hdfs(csv_filename):
	# HDFS 클라이언트 초기화
	hdfs_client = InsecureClient('http://localhost:9870', user='hadoop')

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
       'start_date':datetime(24,3,29),
       'email_on_failure':False,
       'email_on_retry':False,
       'retries':1,
       'retry_delay':timedelta(minutes=5)
}

dag = DAG(
    	dag_id="air02new",
        start_date=yesterday("Asia/Seoul"),
        schedule_interval=timedelta(minutes=5),
        catchup=False
)

fetch_data_task = PythonOperator(
    	dag=dag,
    	task_id='combine_df',
    	python_callable=combine_df
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
