import xml.etree.ElementTree as ET
import xml.dom.minidom
# json형식의 데이터를 xml로 저장하자.
data ={ "STUDENT" :[
  {"NAME" :"Dominica","SCORE" : {"KOR":10,"ENG":20,"MATH":30}, "PROPERTY" :"Good"}, #<student/>
  {"NAME" :"Dominico","SCORE" :{"KOR": 90,"ENG":40, "MATH":100},"PROPERTY" :"A1"}, #<student/ >
  {"NAME" :"RuRe", "SCORE" :{"KOR": 90,"ENG":90, "MATH":90}, "PROPERTY" :"Average"}#<student/>
  ]}
# 1. root를 만들자.
root = ET.Element("STUDENT")
#2. xml 서식으로 하위 요소를 생성해서 추가하자.
for student_data  in data["STUDENT"]:
    student  = ET.SubElement(root,"student")
    name    = ET.SubElement(student , "NAME")
    name.text = student_data["NAME"]
    score    =  ET.SubElement(student ,"SCORE")
    #"SCORE" : {"KOR":10,"ENG":20,"MATH":30}}
    for subject , marks in student_data["SCORE"].items():
         sub  = ET.SubElement(score , subject)
         sub.text =  str(marks)
    ##  PROPERTY 추가.
    property    = ET.SubElement(student , "PROPERTY")
    property.text = student_data["PROPERTY"]


#3.예쁘게  만들자 .
xml_string = ET.tostring(root, encoding="utf-8")
xml_pretty = xml.dom.minidom.parseString(xml_string)
pretty_xml_string = xml_pretty.toprettyxml(indent="  ", encoding="utf-8")

#4. 저장하자.
with open("students_dom02.xml", "wb") as file:
    file.write(pretty_xml_string)

