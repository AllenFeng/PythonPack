import csv,random

#load data
def loadDataset(filename):
    with open(filename,'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        dataset.sort(reverse=False)
    return dataset

#mean
def CalcuMean(Dataset):
    print('mean =' + repr(float(sum(Dataset)/len(Dataset))))

#median
def CalcuMedian(Dataset):
    a=Dataset
    a.sort(reverse=False)
    s=len(a)/2
    if len(a)%2==0:
        print('median =' + repr(float((a[s-1]+a[s]))/2))
    else:
        print('median =' + repr(float(a[s])))


loadDataset('datasetfile.txt')
'''
a=[7,8,4,5,16,20,20,24,19,30,23,30,25,19,29,29,30,30,40,56]
CalcuMean(a)
CalcuMedian(a)
'''