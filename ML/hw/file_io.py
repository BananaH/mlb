class Stock:
	def _init_(self,name,date, opening,closing,highest,lowest,volume,adj_close):
		self.name = name;
		self.date = date;
		self.opening = opening;
		self.closing = closing;
		self.highest = highest;
		self. lowest =  lowest;
		self.volume = volume;
		self.adj_close = adj_closing;
	def set_all(self,name,date, opening,closing,highest,lowest,volume,adj_close):
		self.name = name;
		self.date = date;
		self.opening = opening;
		self.closing = closing;
		self.highest = highest;
		self. lowest =  lowest;
		self.volume = volume;
		self.adj_close = adj_closing;

class files(list):
	def __init__(self,name,date):
		self.name = name
		self.date = date
	def set_all(self,name,date):
		self.name = name
		self.date = date




import csv
import os

StockName = []
Stock_list = []
FileName =[]
file_list = []

folder = '../raw'
#fin = open(file_name,'r')


j=0
k=0
target = 20150922
#target = raw_input(">>>Start date:")
for file_tuple in os.walk(folder):#filesNames is a list of all files in the direction of folder
	j+=1
	
f = open('twse20150922.csv', 'r')  
for row in csv.reader(f):  
	print j,
	
for i in range(len(row[0])):
	StockName.append(row[0][i])
	print StockName

f.close()  	
