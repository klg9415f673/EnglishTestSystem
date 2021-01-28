#!/usr/bin/env python
# coding: utf-8

import csv

class CSVProcess():
    # 建構式
    def __init__(self,path='English.csv'): # 路徑若無輸入預設為'English.csv'
        self.path = path  # 路徑屬性
    # 方法(Method)
    def Read_csv(self):
        # 開啟 CSV 檔案
        with open(r''+ self.path,'r',newline='') as csvFile: # r是路徑中\不轉譯，如\tt就顯示出\tt而非t，後方接變數所以用r''+  # newline避免\r\n被python開啟時會轉化為\n
            rows = csv.reader(csvFile)
            return list(rows)   

    def Write_csv(self,writelist=["test1","test2","test3"]):
        # 開啟 CSV 檔案
        with open(r''+ self.path,'a+',newline='') as csvFile: #a+ 是追加，用w會覆蓋原檔
            csvWriter = csv.writer(csvFile)
            for writerow in writelist:
                csvWriter.writerow(writerow)
    


if __name__ == '__main__':

    CSV = CSVProcess() 
    csvdata = CSV.Read_csv() 
    print(csvdata)
    






