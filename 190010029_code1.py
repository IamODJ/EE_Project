import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter 


df = pd.read_csv("data_190010029.csv",header=None) #change filename if required to check other datasets
df.values.tolist()
k_values=[2,3,4]
dist_values=["Exponential Distribution","Rayleigh Distribution","Half Normal Distribution"]
dist_para=[]
meanDS=np.mean(df)
varDS=np.var(df)
result=-1
finalk=-1

print('Total number of samples: {}'.format(len(df)))
print('Average of dataset given is {}'.format(meanDS[0]))
print('Variance of dataset given is {}'.format(varDS[0]))


commonK= ((meanDS[0])**2)/(varDS[0]-3)         # since Var(X)=3 in this case, required equations in report.
expK=commonK
rayleighK=commonK*((4-np.pi)/np.pi)
normalK= commonK*((np.pi-2)/2)  

exppara= (varDS[0]-3)/(10*meanDS[0])          # hardcoding the parameter values after solving equations
raypara = ((varDS[0]-3)*np.sqrt(np.pi))/(5*np.sqrt(2)*(4-np.pi)*meanDS[0])
hnpara= ((varDS[0]-3)*np.sqrt(2*np.pi))/(10*meanDS[0]*(np.pi-2))

print('\nValue of k (rounded off to closest integer), if ') 
print('W has exponential distribution, is {} (rounded from {})'.format(round(expK),round(expK,2)))
print('W has Rayleigh distribution, is {} (rounded from {})'.format(round(rayleighK),round(rayleighK,2)))
print('W has Half-normal distribution, is {} (rounded from {})'.format(round(normalK),round(normalK,2)))
print('\n')
input("Press Enter to continue...")

if(round(expK) in k_values):
	print("\nExponential distribution is an eligible candidate for W. k={}".format(round(expK)))
	resultMeanExpo=[]
	resultVarExpo=[]
	print("\n Generating 10 datasets of Z using exponential distribution for W i's to\n check if calculated mean and variance of Z is close to Original dataset\n")
	print('\n')
	input("Press Enter to continue...")
	for i in range(10):
		newexp=np.zeros(10**5)
		for j in range(round(expK)):
			newexp+=np.random.exponential(exppara,10**5)*10

		newexp+=np.random.uniform(-3,3,10**5)
		resultMeanExpo.append(np.mean(newexp))
		resultVarExpo.append(np.var(newexp))
		print('Test {},mean(Z): {}'.format(i+1,resultMeanExpo[i]))
		print('Test {},variance(Z): {}'.format(i+1,resultVarExpo[i]))
		print('\n')
	print('\nAverage mean(Z) for the test cases generated: {}'.format(np.mean(resultMeanExpo)))
	print('Average variance(Z) for the test cases generated: {}'.format(np.mean(resultVarExpo)))
	print('\nAverage(Z) calculated of  given dataset is {}'.format(meanDS[0]))
	print('Variance(Z) of dataset given is {}'.format(varDS[0]))
	print('\n')
	input("Press Enter to continue...")
	if(np.mean(resultMeanExpo)>=meanDS[0]-(meanDS[0]/100)  and np.mean(resultMeanExpo)<=meanDS[0]+(meanDS[0]/100)): #99% accuracy for mean
		if(np.mean(resultVarExpo)>=varDS[0]-(varDS[0]/50)  and np.mean(resultVarExpo)<=varDS[0]+(varDS[0]/50)):    
			print("\nWe could see that the mean and variance of newly generated sets is nearly equal to that of original dataset")
			print("To finally conclude distribution for each W is exponential,")
			print("Let us plot histograms of original dataset and newly generated datasets using exponential distribution")
			finalexp=np.zeros(10**5)

			for j in range(round(expK)):
				finalexp+=np.random.exponential(exppara,10**5)*10       #generating new dataset

			finalexp+=np.random.uniform(-3,3,10**5)


			fig, (originalplot,newplot) = plt.subplots(1, 2, sharey=False, tight_layout=True)   #plotting required data
			originalplot.hist(df, bins=200, density=True, color = "green")
			newplot.hist(finalexp, bins=200, density=True, color = "skyblue")
			originalplot.set_title('Original Dataset')
			newplot.set_title('Generated Dataset')
			newplot.set(xlabel='Value of Z')
			originalplot.set(xlabel='Value of Z', ylabel='Density')
			print("\n(Close the plot window for further execution)")
			finalK=round(expK)
			result=0
			dist_para.append(1/exppara)

			plt.show()
	else:
		print("\nWe could see that the mean and variance of newly generated sets highly differs from of original dataset")
		print("Let us consider the next candidate, if any.")
		print('\n')
		input("Press Enter to continue...")

if(round(rayleighK) in k_values):
	print("\nRayleigh distribution is an eligible candidate for W. k={}".format(round(rayleighK)))
	resultMeanRay=[]
	resultVarRay=[]
	print("\n Generating 10 datasets of Z using Rayleigh distribution for W i's to\n check if calculated mean and variance of Z is close to Original dataset\n")
	print('\n')
	input("Press Enter to continue...")
	for i in range(10):
		newray=np.zeros(10**5)
		for j in range(round(rayleighK)):
			newray+=np.random.rayleigh(raypara,10**5)*10

		newray+=np.random.uniform(-3,3,10**5)
		resultMeanRay.append(np.mean(newray))
		resultVarRay.append(np.var(newray))
		print('Test {},mean(Z): {}'.format(i+1,resultMeanRay[i]))
		print('Test {},variance(Z): {}'.format(i+1,resultVarRay[i]))
		print('\n')
	print('\nAverage mean(Z) for the test cases generated: {}'.format(np.mean(resultMeanRay)))
	print('Average variance(Z) for the test cases generated: {}'.format(np.mean(resultVarRay)))
	print('\nAverage(Z) calculated of given dataset is {}'.format(meanDS[0]))
	print('Variance(Z) of dataset given is {}'.format(varDS[0]))
	print('\n')
	input("Press Enter to continue...")

	if(np.mean(resultMeanRay)>=meanDS[0]-(meanDS[0]/100)  and np.mean(resultMeanRay)<=meanDS[0]+(meanDS[0]/100)):
		if(np.mean(resultVarRay)>=varDS[0]-(varDS[0]/100)  and np.mean(resultVarRay)<=varDS[0]+(varDS[0]/100)):
			print("\nWe could see that the mean and variance of newly generated sets is nearly equal to that of original dataset")
			print("To finally conclude distribution for each W is Rayleigh,")
			print("Let us plot histograms of original dataset and newly generated datasets using Rayleigh distribution")
			finalray=np.zeros(10**5)

			for j in range(round(rayleighK)):
				finalray+=np.random.rayleigh(raypara,10**5)*10

			finalray+=np.random.uniform(-3,3,10**5)

			fig, (originalplot,newplot) = plt.subplots(1, 2, sharey=True, tight_layout=True)
			originalplot.hist(df, bins=200, density=True, color = "green")
			originalplot.set(xlabel='Value of Z', ylabel='Density')
			newplot.set(xlabel='Value of Z')
			newplot.hist(finalray, bins=200, density=True, color = "skyblue")
			originalplot.set_title('Original Dataset')
			newplot.set_title('Generated Dataset')
			print("\n(Close the plot window for further execution)")
			finalK=round(rayleighK)
			result=1
			dist_para.append(raypara)
			plt.show()
	else:
		print("\nWe could see that the mean and variance of newly generated sets highly differs from of original dataset")
		print("Let us consider the next candidate, if any.")
		print('\n')
		input("Press Enter to continue...")
if(round(normalK) in k_values):
	print("\nHalf-Normal distribution is an eligible candidate for W. k={}".format(round(normalK)))
	resultMeanNor=[]
	resultVarNor=[]
	print("\n Generating 10 datasets of Z using Half-normal distribution for W i's to\n check if calculated mean and variance of Z is close to Original dataset\n")
	print('\n')
	input("Press Enter to continue...")
	for i in range(10):
		newnor=np.zeros(10**5)
		for j in range(round(normalK)):
			newnor+=np.abs(np.random.normal(0,hnpara,10**5)*10)

		newnor+=np.random.uniform(-3,3,10**5)
		resultMeanNor.append(np.mean(newnor))
		resultVarNor.append(np.var(newnor))
		print('Test {},mean(Z): {}'.format(i+1,resultMeanNor[i]))
		print('Test {},variance(Z): {}'.format(i+1,resultVarNor[i]))
		print('\n')
	print('\nAverage mean(Z) for the test cases generated: {}'.format(np.mean(resultMeanNor)))
	print('Average variance(Z) for the test cases generated: {}'.format(np.mean(resultVarNor)))
	print('\nAverage(Z) calculated of  given dataset is {}'.format(meanDS[0]))
	print('Variance(Z) of dataset given is {}'.format(varDS[0]))
	print('\n')
	input("Press Enter to continue...")
	if(np.mean(resultMeanNor)>=meanDS[0]-(meanDS[0]/100)  and np.mean(resultMeanNor)<=meanDS[0]+(meanDS[0]/100)):
		if(np.mean(resultVarNor)>=varDS[0]-(varDS[0]/100)  and np.mean(resultVarNor)<=varDS[0]+(varDS[0]/100)):
			print("\nWe could see that the mean and variance of newly generated sets is nearly equal to that of original dataset")
			print("To finally conclude distribution for each W is Half-normal,")
			print("Let us plot histograms of original dataset and newly generated datasets using Half-normal distribution.")
			finalnor=np.zeros(10**5)

			for j in range(round(normalK)):
				finalnor+=np.abs(np.random.normal(0,hnpara,10**5)*10)

			finalnor+=np.random.uniform(-3,3,10**5)


			fig, (originalplot,newplot) = plt.subplots(1, 2, sharey=True, tight_layout=True)
			originalplot.hist(df, bins=200, density=True, color = "green")
			newplot.hist(finalnor, bins=200, density=True, color = "skyblue")
			originalplot.set(xlabel='Value of Z', ylabel='Density')
			originalplot.set_title('Original Dataset')
			newplot.set_title('Generated Dataset')
			newplot.set(xlabel='Value of Z')
			print("\n(Close the plot window for further execution)")
			finalK=round(normalK)
			result=2
			dist_para.append(hnpara)
			plt.show()
	else:
		print("\nWe could see that the mean and variance of newly generated sets highly differs from of original dataset")
		print("Let us consider the next candidate, if any.")
		print("No further eligible candidate.")

input("Press enter to continue...")
print("\nFinal Conclusion: The given dataset has W i's with {}, k={} and distribution parameter {}".format(dist_values[result],finalK,dist_para[0]))