"""
Supreme Court

A program taht requests the name of a justice and displays the justice's data.
"""

import pickle

def main():
	dicLst = createDictFromBinaryFile("JusticesDict.dat")
	justice = input("Enter the name of a justice: ")
	getData(dicLst, justice)

def createDictFromBinaryFile(file):
	infile = open(file, 'rb')
	dicLst = pickle.load(infile) 
	infile.close()	
	
	return dicLst

def getData(dicLst, justice):
	for k in dicLst:
		if k == justice:
			print("Appointed by", dicLst[k]['pres'])
			print("State:", dicLst[k]['state'])
			print("Year of appointment:", dicLst[k]['yrAppt'])
			if dicLst[k]['yrLeft'] == 0:
				print("Currently serving on Supreme Court.")
			else:
				print("Left court in", dicLst[k]['yrLeft'])
		else:
			pass
	
main()