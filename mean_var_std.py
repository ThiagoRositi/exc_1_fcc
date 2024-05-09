import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        #because it was not specified what I should do with more than 9 numbers
        #I also considered it a mistake.
   
    #create the matrix with values of list
    matrix = np.array([list[:3],list[3:6],list[6:]])
    
    #I go through the matrix rows and columns to solve the problems
    
    
    resultdict = {'mean':[[],[]],'variance':[[],[]], 'standard deviation':[[],[]], 'max':[[],[]], 
               'min':[[],[]], 'sum':[[],[]]}
   
    
    row = 0
    column = 0
    for i in matrix[0]:
       #that get all answers of axis 2
        resultdict.get('mean')[1].append(matrix[row].mean())
        resultdict.get('variance')[1].append(matrix[row].var())
        resultdict.get('standard deviation')[1].append(matrix[row].std())
        resultdict.get('max')[1].append(matrix[row].max())
        resultdict.get('min')[1].append(matrix[row].min())
        resultdict.get('sum')[1].append(matrix[row].sum())

        #that for get all answers of axis 1    
        resultdict.get('mean')[0].append(matrix[:,column].mean())
        resultdict.get('variance')[0].append(matrix[:,column].var())
        resultdict.get('standard deviation')[0].append(matrix[:,column].std())
        resultdict.get('max')[0].append(matrix[:,column].max())
        resultdict.get('min')[0].append(matrix[:,column].min())
        resultdict.get('sum')[0].append(matrix[:,column].sum())     

        column += 1 
        row += 1
    #that get the matrix totally analisis
    resultdict.get('mean').append(matrix.mean())
    resultdict.get('variance').append(matrix.var())
    resultdict.get('standard deviation').append(matrix.std())
    resultdict.get('max').append(matrix.max())
    resultdict.get('min').append(matrix.min())
    resultdict.get('sum').append(matrix.sum())

    return resultdict


    
    

    




    return calculations