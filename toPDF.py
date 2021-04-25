import requests
import json
from docx2pdf import convert
from docx import Document

#request = requests.get("http://localhost:63342/convertFormToPDF/index.html?_ijt=kphnndsr7rs7f1mqful3aed4f9")

#print(request)

document = Document("Шаблон.docx")

src = dict()
with open("data.json", "r") as inputfile:
    src = json.load(inputfile)

for paragraph in document.paragraphs:
    if "[1]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[1]", src.get("surname") + " " + src.get("name") + " " + src.get("lastname"))
    if "[2]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[2]", src.get("sex"))
    if "[3]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[3]", src.get("date"))
    if "[4]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[4]", src.get("region"))
    if "[5]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[5]", src.get("city"))
    if "[6]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[6]", src.get("email"))
    if "[7]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[7]", src.get("phone"))
    if "[8]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[8]", src.get("vk"))
    if "[9]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[9]", src.get("food"))
    if "[10]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[10]", src.get("Tshirtsize"))
    if "[11]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[11]", src.get("bootSize"))
    if "[12]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[12]", src.get("study"))
    if "[13]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[13]", src.get("degree"))
    if "[14]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[14]", src.get("additional"))
    if "[15]" in paragraph.text:
        paragraph.text = paragraph.text.replace("[15]", src.get("personalData"))

document.save("Документ.docx")
convert("Документ.docx", "Документ.pdf")
