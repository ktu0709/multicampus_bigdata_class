import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.io.BufferedReader;
import java.io.IOException;
import org.json.simple.parser.JSONParser;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

public class App {
    public static void main(String[] args) throws Exception {
        StringBuilder urlBuilder = new StringBuilder("http://apis.data.go.kr/B490007/instiCompCose/getInstiCompCoseList"); /*URL*/
        urlBuilder.append("?" + URLEncoder.encode("serviceKey","UTF-8") + "="); /*Service Key*/
        urlBuilder.append("&" + URLEncoder.encode("numOfRows","UTF-8") + "=" + URLEncoder.encode("10", "UTF-8")); /*한 페이지 결과 수*/
        urlBuilder.append("&" + URLEncoder.encode("pageNo","UTF-8") + "=" + URLEncoder.encode("1", "UTF-8")); /*페이지번호*/
        urlBuilder.append("&" + URLEncoder.encode("dataFormat","UTF-8") + "=" + URLEncoder.encode("json", "UTF-8")); /*응답 데이터 표준 형식 - xml / json (대소문자 구분 없음)*/
        urlBuilder.append("&" + URLEncoder.encode("qualgbCd","UTF-8") + "=" + URLEncoder.encode("C", "UTF-8")); /*자격구분코드 - C : 과정평가형자격 - W : 일학습병행자격*/
        urlBuilder.append("&" + URLEncoder.encode("rgnCd","UTF-8") + "=" + URLEncoder.encode("001", "UTF-8")); /*관할지사 지역코드*/
        urlBuilder.append("&" + URLEncoder.encode("trngYy","UTF-8") + "=" + URLEncoder.encode("", "UTF-8")); /*훈련년도*/
        urlBuilder.append("&" + URLEncoder.encode("instiNm","UTF-8") + "=" + URLEncoder.encode("", "UTF-8")); /*기관/기업명*/
        urlBuilder.append("&" + URLEncoder.encode("coseNm","UTF-8") + "=" + URLEncoder.encode("", "UTF-8")); /*과정명*/
        urlBuilder.append("&" + URLEncoder.encode("jmNm","UTF-8") + "=" + URLEncoder.encode("", "UTF-8")); /*종목명*/
        URL url = new URL(urlBuilder.toString());
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Content-type", "application/json");
        //System.out.println("Response code: " + conn.getResponseCode());
        BufferedReader rd;
        if(conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
            rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        } else {
            rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
        }
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = rd.readLine()) != null) {
            sb.append(line);
        }

        ////json parse
        JSONParser jsonParser = new JSONParser();
        JSONObject jsonObject = (JSONObject)jsonParser.parse(sb.toString());
        JSONObject bodydata = (JSONObject)jsonObject.get("body");
        JSONArray bodyitem = (JSONArray)bodydata.get("items");

        //System.out.println("인덱스 수  = " +bodyitem.size());
        for(int i=0;i<bodyitem.size();i++){
        JSONObject item = (JSONObject)bodyitem.get(i);
        System.out.println("결과코드 : " + item.get("resultCode"));
        System.out.println("결과메시지 : " + item.get("resultMsg"));
        System.out.println("기관/기업명 : " + item.get("instiNm"));
        System.out.println("지역코드 : " + item.get("rgnCd"));
        System.out.println("지역명 : " + item.get("rgnNm"));
        System.out.println("지사코드 : " + item.get("brchCd"));
        System.out.println("지사명 : " + item.get("brchNm"));
        System.out.println("총 과정 수 : " + item.get("totCoseCnt"));
        System.out.println("총 훈련생 수 : " + item.get("totTraineeCnt"));
        System.out.println("총 자격취득 수 : " + item.get("totQualAcquCnt"));
        System.out.println("과정 자격구분코드 : " + item.get("coseQualgbCd"));
        System.out.println("과정 자격구분명 : " + item.get("coseQualgbNm"));
        System.out.println("과정 아이디 : " + item.get("coseId"));
        System.out.println("과정 차수 : " + item.get("coseSeq"));
        System.out.println("과정명 : " + item.get("coseNm"));
        System.out.println("과정 기관구분코드 : " + item.get("coseInstiGbCd"));
        System.out.println("과정 기관구분명 : " + item.get("coseInstiGbNm"));
        System.out.println("과정 운영형태코드 : " + item.get("coseOprTypCd"));
        System.out.println("과정 운영형태명 : " + item.get("coseOprTypNm"));
        System.out.println("과정 훈련시작일자 : " + item.get("coseTrngStartDt"));
        System.out.println("과정 훈련종료일자 : " + item.get("coseTrngEndDt"));
        System.out.println("과정 종목코드 : " + item.get("coseJmCd"));
        System.out.println("과정 종목명 : " + item.get("coseJmNm"));
        System.out.println("과정 종목기준버전코드 : " + item.get("coseOrganStdVerCd"));
        System.out.println("과정 훈련생 수 : " + item.get("coseTraineeCnt"));
        System.out.println("과정 자격취득 수 : " + item.get("coseQualAcquCnt"));
        System.out.println("한 페이지 결과 수 : " + item.get("numOfRows"));
        System.out.println("페이지 수 : " + item.get("pageNo"));
        System.out.println("데이터 총 개수 : " + item.get("totalCount"));
        System.out.println("=======================================");
        }

        rd.close();
        conn.disconnect();
        //System.out.println(sb.toString());
    }
}
