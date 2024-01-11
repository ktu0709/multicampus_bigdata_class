import xml.etree.ElementTree as ET
# json형식의 데이터를 xml로 저장하자.
data ={ "STUDENT" :[
  {"NAME" :"Dominica","SCORE" : {"KOR":10,"ENG":20,"MATH":30,"mus":66}}, #<student/>
  {"NAME" :"Dominico","SCORE" :{"KOR": 90,"ENG":40, "MATH":100,"mus":70}}, #<student/>
  {"NAME" :"RuRe", "SCORE" :{"KOR": 90,"ENG":90, "MATH":90,"mus":40}}#<student/>
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

#3.xml만들자
tree  = ET.ElementTree(root)
#4. xml생성된 tree를 파일로 저장
tree.write("student.xml",encoding="utf-8", xml_declaration=True)


