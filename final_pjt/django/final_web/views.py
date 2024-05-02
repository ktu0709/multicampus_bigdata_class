from django.shortcuts import render
import requests
import pandas as pd
from django.http import JsonResponse
from datetime import datetime,timedelta
import numpy as np

import os
from keras.models import load_model
from sklearn.preprocessing import StandardScaler



def render_map(request):
    return render(request, 'map.html')

def Hpoint(request):
    return render(request, 'Hpoint.html')

def merchandise(request):
    return render(request, 'merchandise.html')

def get_station():
    startpage = ['1', '1000', '2000']
    endpage = ['999', '1999', '2999']
    stations = ['1124', '1153', '1158', '1160', '1166', '2701', '2715', '2721', '2728', '3798']

    code = {'1124': '11500615', '1153': '11500603', '1158': '11500604', '1160': '11500535', '1166': '11500535',
           '2701': '11500603', '2715': '11500603', '2721': '11500603', '2728': '11500603', '3798': '11500591'}

    res_df = pd.DataFrame()

    for x, y in zip(startpage, endpage):
        api_url = "http://openapi.seoul.go.kr:8088/664c747774656f6e3130384667614e49/json/bikeList/" + x + "/" + y + "/"
        response = requests.get(api_url)
        data = response.json()
        bike_info = data['rentBikeStatus']['row']
        df = pd.DataFrame(bike_info)
        res_df = pd.concat([res_df, df])

    station_name = list(res_df['stationName'])
    station_no = []
    for i in station_name:
        test_list = i.split(".")
        station_no.append(test_list[0])

    res_df['station_no'] = station_no
    res_df = res_df[res_df['station_no'].isin(stations)]
    res_df['adbcode'] = res_df['station_no'].map(code)

    return res_df


def get_people():
    startpage = ['1', '1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000']
    endpage = ['999', '1999', '2999', '3999', '4999', '5999', '6999', '7999', '8999', '9999']
    sum_df = pd.DataFrame()
    res_df = pd.DataFrame()
    gangse_se = ['11500535', '11500603', '11500604', '11500615', '11500591']
    now = datetime.now()
    # now = now + timedelta(hours=1)
    now_time = now.strftime('%Y%m%d_%H%M')
    hour = now_time[9:11]

    for x, y in zip(startpage, endpage):
        api_url = "http://openapi.seoul.go.kr:8088/664c747774656f6e3130384667614e49/json/SPOP_LOCAL_RESD_DONG/" + x + "/" + y + "///"
        # print(api_url)
        response = requests.get(api_url)
        res = response.json()
        data = res['SPOP_LOCAL_RESD_DONG']['row']
        df = pd.DataFrame(data)
        sum_df = pd.concat([sum_df, df])

    for i in gangse_se:
        gangse_df = sum_df[(sum_df['ADSTRD_CODE_SE'] == i) & (sum_df['TMZON_PD_SE'] == hour)]
        res_df = pd.concat([res_df, gangse_df])
    return res_df


def get_weather():
    now_time = datetime.now().strftime('%Y%m%d_%H%M')
    date = now_time[0:8]
    hour = now_time[9:11]
    minute = now_time[11:13]
    if (int(minute) < 10):
        agotime = datetime.now()
        agotime = agotime - timedelta(hours=1)
        agotime = agotime.strftime('%Y%m%d_%H%M')
        hour = agotime[9:11]

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey': 'l1DP/qWK5Y9nHd7cWOdMjVTLwd92c5a0xNf7WwiJUhZgHP0wZUjMuEfKZNJBLsZyiLFcU6QLumN1K6NrIzr6KA==',
              'pageNo': '1', 'numOfRows': '1000', 'dataType': 'json', 'base_date': date, 'base_time': hour + '00',
              'nx': 57, 'ny': 127}

    response = requests.get(url, params=params)
    now_time = datetime.now().strftime('%Y%m%d_%H%M')
    print(response.status_code)

    res = response.json()
    data = res['response']['body']['items']['item']
    weather_df = pd.DataFrame(data)
    weather_df = weather_df.pivot(index=['baseDate', 'baseTime', 'nx', 'ny'], columns='category', values='obsrValue')
    weather_df = weather_df[['PTY', 'REH', 'RN1', 'T1H']]
    return weather_df


def combine_data(station_no):
    res_df = get_station()
    people_df = get_people()
    people_df = people_df[['ADSTRD_CODE_SE', 'TOT_LVPOP_CO', 'STDR_DE_ID', 'TMZON_PD_SE']]

    tmp_df = get_weather()
    tmp = tmp_df['T1H'].astype(float)
    tmp = float(tmp.values)

    combined_df = pd.merge(left=res_df, right=people_df, how='inner', left_on='adbcode', right_on='ADSTRD_CODE_SE')

    stationNm = res_df.loc[res_df['station_no'] == station_no, 'stationName']
    bike_cnt = res_df.loc[res_df['station_no'] == station_no, 'parkingBikeTotCnt']
    tot_cnt = res_df.loc[res_df['station_no'] == station_no, 'rackTotCnt']
    people_cnt = combined_df.loc[combined_df['station_no'] == station_no, 'TOT_LVPOP_CO']

    lat = res_df.loc[res_df['station_no'] == station_no, 'stationLatitude']
    long = res_df.loc[res_df['station_no'] == station_no, 'stationLongitude']

    stationNm = str(stationNm.values)

    bike_cnt = bike_cnt.astype(int)
    bike_cnt = int(bike_cnt.values)

    tot_cnt = tot_cnt.astype(int)
    tot_cnt = int(tot_cnt.values)

    people_cnt = people_cnt.astype(float)
    people_cnt = float(people_cnt.values)


    if(datetime.today().weekday() == 0):
        weekday = 6.0
        isweek = 0.0
    elif(datetime.today().weekday() == 1):
        weekday = 0.0
        isweek = 0.0
    elif(datetime.today().weekday() == 2):
        weekday = 1.0
        isweek = 0.0
    elif (datetime.today().weekday() == 3):
        weekday = 2.0
        isweek = 0.0
    elif(datetime.today().weekday() == 4):
        weekday = 3.0
        isweek = 0.0
    elif(datetime.today().weekday() == 5):
        weekday = 4.0
        isweek = 1.0
    else:
        weekday = 5.0
        isweek = 1.0

    return stationNm,bike_cnt,tot_cnt,people_cnt,tmp,weekday,isweek,lat.values[0],long.values[0]

def predict_GRU(station_no):
    model_save_dir = "dl_models"
    loaded_models2 = []

    stationNm,bike_cnt, tot_cnt, people_cnt, tmp, weekday, isweek, lat, long = combine_data(station_no)

    scaler = StandardScaler()


    #testX = np.array([[bike_cnt, 20.0, 0.0, 0.0, 16402.7422, 16.0, 1.0, 0.0]])
    testX = np.array([[
        [bike_cnt, tmp, 0.0, 0.0, people_cnt, tmp, weekday, isweek]  # 시간 단계 1의 특성
        for _ in range(168)  # 시퀀스 길이
    ]])

    testX_reshaped = testX.reshape(-1, testX.shape[-1])

    # StandardScaler를 사용하여 정규화된 데이터 얻기
    testX_normalized = scaler.fit_transform(testX_reshaped)

    # 정규화된 데이터를 다시 (batch_size, sequence_length, num_features) 형태로 reshape합니다.
    testX_normalized = testX_normalized.reshape(testX.shape)


    for i in range(5):
        model_path2 = os.path.join(model_save_dir, f'gru_model_{station_no}_{i + 1}.h5')
        loaded_model2 = load_model(model_path2)
        loaded_models2.append(loaded_model2)

    predictions2 = []
    for loaded_model2 in loaded_models2:
        pred2 = loaded_model2.predict(testX_normalized)

        mean_values_pred = np.repeat(scaler.mean_[np.newaxis, :], pred2.shape[0], axis=0)
        # 예측값을 첫 번째 컬럼에 대입
        mean_values_pred[:, 0] = np.squeeze(pred2)
        # 역정규화
        y_pred = scaler.inverse_transform(mean_values_pred)[:, 0]

        predictions2.append(y_pred)

    # 예측 평균 계산
    predictions2 = np.array(predictions2)
    mean_predictions2 = np.mean(predictions2, axis=0)
    print(f'배깅모델 평균 : {mean_predictions2}')
    mean_predictions2 = int(mean_predictions2)
    return stationNm,bike_cnt, tot_cnt, people_cnt, tmp, weekday, isweek, lat, long , mean_predictions2


def render_json(request):
    stations = ['1124', '1153', '1158', '1160', '1166', '2701', '2715', '2728', '3798']
    #stations = ['1124', '1153']
    pred_list = []

    for i in stations:
        stationNm,bike_cnt, tot_cnt, people_cnt, tmp, weekday, isweek, lat, long, pred_cnt = predict_GRU(i)
        bike_rate = pred_cnt / tot_cnt
        data = {
            'station_id': i,
            'stationNm' : stationNm,
            'bike_cnt': str(bike_cnt),
            'tot_cnt' : str(tot_cnt),
            'people_cnt': str(people_cnt),
            'tmp': str(tmp),
            'weekday': str(weekday),
            'isweek': str(isweek),
            'lat': str(lat),
            'long': str(long),
            'pred_cnt': str(pred_cnt),
            'bike_rate' : str(bike_rate)
        }
        pred_list.append(data)

    stationNm,bike_cnt, tot_cnt, people_cnt, tmp, weekday, isweek, lat, long, pred_cnt = predict_2721('2721')
    bike_rate = pred_cnt / tot_cnt
    data = {
        'station_id': '2721',
        'stationNm': stationNm,
        'bike_cnt': str(bike_cnt),
        'tot_cnt': str(tot_cnt),
        'people_cnt': str(people_cnt),
        'tmp': str(tmp),
        'weekday': str(weekday),
        'isweek': str(isweek),
        'lat': str(lat),
        'long': str(long),
        'pred_cnt': str(pred_cnt),
        'bike_rate': str(bike_rate)
    }
    pred_list.append(data)


    print(pred_list[0])
    return  JsonResponse({'pred_list' : pred_list})


def update_marker(request):
    data_df = get_station()

    station_name = data_df["stationName"]
    lat_list = data_df["stationLatitude"]
    long_list = data_df["stationLongitude"]
    bikecnt = data_df["parkingBikeTotCnt"]
    racktotcnt = data_df["rackTotCnt"]
    markers_data = list(zip(station_name, lat_list, long_list, bikecnt,racktotcnt))

    return  JsonResponse({'markers_data' : markers_data})





def predict_2721(station_no):

    model_path = "dl_models/gru_2721.h5"
    loaded_model = load_model(model_path)

    stationNm,bike_cnt, tot_cnt, people_cnt, tmp, weekday, isweek, lat, long = combine_data(station_no)

    scaler = StandardScaler()

    #testX = np.array([[bike_cnt, 20.0, 0.0, 0.0, 16402.7422, 16.0, 1.0, 0.0]])
    testX = np.array([[
        [bike_cnt, tmp, 0.0, 0.0, people_cnt, tmp, weekday, isweek]  # 시간 단계 1의 특성
        for _ in range(168)  # 시퀀스 길이
    ]])

    testX_reshaped = testX.reshape(-1, testX.shape[-1])

    # StandardScaler를 사용하여 정규화된 데이터 얻기
    testX_normalized = scaler.fit_transform(testX_reshaped)

    # 정규화된 데이터를 다시 (batch_size, sequence_length, num_features) 형태로 reshape합니다.
    testX_normalized = testX_normalized.reshape(testX.shape)


    prediction_optuna = loaded_model.predict(testX_normalized)

    # 예측값을 위한 평균값 배열 생성
    mean_values_pred5 = np.repeat(scaler.mean_[np.newaxis, :], prediction_optuna.shape[0], axis=0)
    # 예측값을 첫 번째 컬럼에 대입
    mean_values_pred5[:, 0] = np.squeeze(prediction_optuna)
    # 역정규화
    y_pred_optuna = scaler.inverse_transform(mean_values_pred5)[:, 0]

    predict_val = int(y_pred_optuna[0])
    return stationNm, bike_cnt, tot_cnt, people_cnt, tmp, weekday, isweek, lat, long, predict_val
