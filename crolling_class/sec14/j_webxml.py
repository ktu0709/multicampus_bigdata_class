import xml.etree.ElementTree as ET
import xml.dom.minidom
# json형식의 데이터를 minidom 모듈의 xml로 저장하자.
# minidom = 문서를  XML  Document로 만들어서 관리한다.
data ={ "STUDENT" :[
  {"NAME" :"Dominica","SCORE" : {"KOR":10,"ENG":20,"MATH":30}, "PROPERTY" :"Good"}, #<student/>
  {"NAME" :"Dominico","SCORE" :{"KOR": 90,"ENG":40, "MATH":100},"PROPERTY" :"A1"}, #<student/ >
  {"NAME" :"RuRe", "SCORE" :{"KOR": 90,"ENG":90, "MATH":90}, "PROPERTY" :"Average"}#<student/>
  ]}

#1. Document를 만들자.
doc  = xml.dom.minidom.Document()

# 2. root 요소를 만들고 문서에 추가한다,
root = doc.createElement("STUDENT")
doc.appendChild(root)
#3. xml 서식으로 하위 요소를 생성해서 추가하자.
for student_data  in data["STUDENT"]:
    student  =doc.createElement("student")
    name = doc.createElement("NAME")  #요소만들고
    name.appendChild(doc.createTextNode(student_data["NAME"] ))    #text 생성하고  #name 추가하고
    student.appendChild(name)
    score    = doc.createElement("SCORE")
    #"SCORE" : {"KOR":10,"ENG":20,"MATH":30}}
    for subj , marks in student_data["SCORE"].items():
        subj_e = doc.createElement(subj)
        subj_e.appendChild(doc.createTextNode(str(marks)))
        score.appendChild(subj_e)
    student.appendChild(score)
    ##  PROPERTY 추가.
    property_e   = doc.createElement("PROPERTY")
    property_e.appendChild (doc.createTextNode(student_data["PROPERTY"] ))
    student.appendChild(property_e)
    root.appendChild(student)
#3.예쁘게  만들자 .
xml_string =doc.toprettyxml(indent="  ", encoding="utf-8")
#4. 저장하자.
with open("students_dom03.xml", "wb") as file:
    file.write(xml_string)

