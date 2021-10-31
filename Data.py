import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
mathScore = df["math score"].to_list()
readingScore = df["reading score"].to_list()
writingScore = df["writing score"].to_list()

#MEAN
mathMean = statistics.mean(mathScore)
readingMean = statistics.mean(readingScore)
writingMean = statistics.mean(writingScore)

#MEDIAN
mathMedian = statistics.median(mathScore)
readingMedian = statistics.median(readingScore)
writingMedian = statistics.median(writingScore)

#MODE
mathMode = statistics.mode(mathScore)
readingMode = statistics.mode(readingScore)
writingMode = statistics.mode(writingScore)

#STDEV
mathStdev = statistics.stdev(mathScore)
readingStdev = statistics.stdev(readingScore)
writingStdev = statistics.stdev(writingScore)

#print(mathMean, readingMean, writingMean)
#print(mathMedian, readingMedian, writingMedian)
#print(mathMode, readingMode, writingMode)
#print(mathStdev, readingStdev, writingStdev)


#1, 2 & 3rd stdev of math scores
math_first_stdev_start, math_first_stdev_end = mathMean - mathStdev, mathMean + mathStdev
math_second_stdev_start, math_second_stdev_end = mathMean - (2*mathStdev), mathMean + (2*mathStdev)
math_third_stdev_start, math_third_stdev_end = mathMean - (3*mathStdev), mathMean + (3*mathStdev)

#1, 2 & 3rd stdev of reading scores
reading_first_stdev_start, reading_first_stdev_end = readingMean - readingStdev, readingMean + readingStdev
reading_second_stdev_start, reading_second_stdev_end = readingMean - (2*readingStdev), readingMean + (2*readingStdev)
reading_third_stdev_start, reading_third_stdev_end = readingMean - (3*readingStdev), readingMean + (3*readingStdev)

#1, 2 & 3rd stdev of writing scores
writing_first_stdev_start, writing_first_stdev_end = writingMean - writingStdev, writingMean + writingStdev
writing_second_stdev_start, writing_second_stdev_end = writingMean - (2*writingStdev), writingMean + (2*writingStdev)
writing_third_stdev_start, writing_third_stdev_end = writingMean - (3*writingStdev), writingMean + (3*writingStdev)

#Percentage of math list in 1, 2 & 3rd stdev
math_within_1stdev= [result for result in mathScore if result > math_first_stdev_start and result < math_first_stdev_end]
math_within_2stdev= [result for result in mathScore if result > math_second_stdev_start and result < math_second_stdev_end]
math_within_3stdev= [result for result in mathScore if result > math_third_stdev_start and result < math_third_stdev_end]

#Percentage of reading list in 1, 2 & 3rd stdev
reading_within_1stdev= [result for result in readingScore if result > reading_first_stdev_start and result < reading_first_stdev_end]
reading_within_2stdev= [result for result in readingScore if result > reading_second_stdev_start and result < reading_second_stdev_end]
reading_within_3stdev= [result for result in readingScore if result > reading_third_stdev_start and result < reading_third_stdev_end]

#Percentage of writing list in 1, 2 & 3rd stdev
writing_within_1stdev= [result for result in writingScore if result > writing_first_stdev_start and result < writing_first_stdev_end]
writing_within_2stdev= [result for result in writingScore if result > writing_second_stdev_start and result < writing_second_stdev_end]
writing_within_3stdev= [result for result in writingScore if result > writing_third_stdev_start and result < writing_third_stdev_end]

print("Math scores data: ")
print("Percent of data within 1 stdev:")
print(len(math_within_1stdev)*100/len(mathScore))
print("Percent of data within 2 stdev:")
print(len(math_within_2stdev)*100/len(mathScore))
print("Percent of data within 3 stdev:")
print(len(math_within_3stdev)*100/len(mathScore))

print("")

print("Reading scores data:")
print("Percent of data within 1 stdev:")
print(len(reading_within_1stdev)*100/len(readingScore))
print("Percent of data within 2 stdev:")
print(len(reading_within_2stdev)*100/len(readingScore))
print("Percent of data within 3 stdev:")
print(len(reading_within_3stdev)*100/len(readingScore))

print("")

print("Writing scores data:")
print("Percent of data within 1 stdev:")
print(len(writing_within_1stdev)*100/len(writingScore))
print("Percent of data within 2 stdev:")
print(len(writing_within_2stdev)*100/len(writingScore))
print("Percent of data within 3 stdev:")
print(len(writing_within_3stdev)*100/len(writingScore))