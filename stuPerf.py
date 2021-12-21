import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")

mathList = df["math score"].to_list()
readList = df["reading score"].to_list()
writeList = df["writing score"].to_list()

mathMean = statistics.mean(mathList)
readMean = statistics.mean(readList)
writeMean = statistics.mean(writeList)

mathMedian = statistics.median(mathList)
readMedian = statistics.median(readList)
writeMedian = statistics.median(writeList)

mathMode = statistics.mode(mathList)
readMode = statistics.mode(readList)
writeMode = statistics.mode(writeList)

print("Mean, median and mode of math score is {}, {} and {}".format(mathMean,mathMedian,mathMode))
print("Mean, median and mode of reading score is {}, {} and {}".format(readMean,readMedian,readMode))
print("Mean, median and mode of writing score is {}, {} and {}".format(writeMean,writeMedian,writeMode))

print()

mathStdDev = statistics.stdev(mathList)
readStdDev = statistics.stdev(readList)
writeStdDev = statistics.stdev(writeList)

print("Standard deviation of math score is "+str(mathStdDev))
print("Standard deviation of reading score is "+str(readStdDev))
print("Standard deviation of writing score is "+str(writeStdDev))

print()


first_msd_start,first_msd_end = mathMedian-mathStdDev,mathMean+mathStdDev
second_msd_start,second_msd_end = mathMedian-2*mathStdDev,mathMean+2*mathStdDev
third_msd_start,third_msd_end = mathMedian-3*mathStdDev,mathMean+3*mathStdDev

first_rsd_start,first_rsd_end = readMedian-readStdDev,readMean+readStdDev
second_rsd_start,second_rsd_end = readMedian-2*readStdDev,readMean+2*readStdDev
third_rsd_start,third_rsd_end = mathMedian-3*readStdDev,readMean+3*readStdDev

first_wsd_start,first_wsd_end = writeMedian-writeStdDev,writeMean+writeStdDev
second_wsd_start,second_wsd_end = writeMedian-2*writeStdDev,writeMean+2*writeStdDev
third_wsd_start,third_wsd_end = writeMedian-3*writeStdDev,writeMean+3*writeStdDev

math_listOfDataWithin1StandardDeviation = [results for results in mathList if results > first_msd_start and results < first_msd_end]
math_listOfDataWithin2StandardDeviation = [results for results in mathList if results > second_msd_start and results < second_msd_end]
math_listOfDataWithin3StandardDeviation = [results for results in mathList if results > third_msd_start and results < third_msd_end]

read_listOfDataWithin1StandardDeviation = [results for results in readList if results > first_rsd_start and results < first_rsd_end]
read_listOfDataWithin2StandardDeviation = [results for results in readList if results > second_rsd_start and results < second_rsd_end]
read_listOfDataWithin3StandardDeviation = [results for results in readList if results > third_rsd_start and results < third_rsd_end]

write_listOfDataWithin1StandardDeviation = [results for results in writeList if results > first_wsd_start and results < first_wsd_end]
write_listOfDataWithin2StandardDeviation = [results for results in writeList if results > second_wsd_start and results < second_wsd_end]
write_listOfDataWithin3StandardDeviation = [results for results in writeList if results > third_wsd_start and results < third_wsd_end]

print("{}% of data of math score that lies within 1 standard deviation".format(len(math_listOfDataWithin1StandardDeviation)*100.0/len(mathList)))
print("{}% of data of math score that lies within 2 standard deviations".format(len(math_listOfDataWithin2StandardDeviation)*100.0/len(mathList)))
print("{}% of data of math score that lies within 3 standard deviations".format(len(math_listOfDataWithin3StandardDeviation)*100.0/len(mathList)))

print()

print("{}% of data of reading score that lies within 1 standard deviation".format(len(read_listOfDataWithin1StandardDeviation)*100.0/len(readList)))
print("{}% of data of reading score that lies within 2 standard deviations".format(len(read_listOfDataWithin2StandardDeviation)*100.0/len(readList)))
print("{}% of data of reading score that lies within 3 standard deviations".format(len(read_listOfDataWithin3StandardDeviation)*100.0/len(readList)))

print()

print("{}% of data of writing score that lies within 1 standard deviation".format(len(write_listOfDataWithin1StandardDeviation)*100.0/len(writeList)))
print("{}% of data of writing score that lies within 2 standard deviations".format(len(write_listOfDataWithin2StandardDeviation)*100.0/len(writeList)))
print("{}% of data of writing score that lies within 3 standard deviations".format(len(write_listOfDataWithin3StandardDeviation)*100.0/len(writeList)))
