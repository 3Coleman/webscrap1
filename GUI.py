from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd

def clicked():
    http_response = requests.get("https://www.iplt20.com/auction/2022")
    soup = BeautifulSoup(http_response.content, "html.parser")
    table = soup.find("table", class_="ih-td-tab auction-tbl")
    title = table.find_all("th")
    header = []
    for i in title:
        name = i.text
        header.append(name)
    df = pd.DataFrame(columns=header)
    row = table.find_all("tr")
    for i in row[1:]:
        first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
        data = i.find_all("td")[1:]

        row = [tr.text for tr in data]
        row.insert(0, first_td)
        l = len(df)
        df.loc[l] = row
    df.to_csv("ipl auction details 2024.csv")


def windows():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("htmlextractor")

    label=QtWidgets.QLabel(win)
    label.setText("quicksrapper")
    label.move(50,50)

    b1=QtWidgets.QPushButton(win)
    b1.setText("Extract now")
    b1.clicked.connect(clicked)
    win.show()
    sys.exit(app.exec())

windows()
