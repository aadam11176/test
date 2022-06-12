
from random import randint
import pandas as pd
import numpy as np




class Datagenerateor:
    # type of data: 1 -> random type for all columns.
    #               2 -> all columns same type (int)
    #               3 -> all columns same type (float)
    #               4 -> all columns same type (string) 
    #               5 -> all columns same type (time) 
    def __init__(self, number_of_columns, number_of_rows, randomtype_of_data = 1 ):
        
        self.number_of_columns = number_of_columns
        self. number_of_rows = number_of_rows
        self.randomtype_of_data = randomtype_of_data
        self.data = self.Maingenerateor()
        
        
    def Maingenerateor(self):
        col_name = [str(i) for i in range (self.number_of_columns)]
        df = pd.DataFrame()
        if (self.randomtype_of_data == 1): # all columns are random type
            for x in col_name:
                df[x] = self.GenrateColumsData(randint(2,3), 0, 100) #change 2 to 5
        
        if (self.randomtype_of_data == 2): # all columns are int
            for x in col_name:   
                df[x] = self.GenrateColumsData(2, 0, 100)
        
        if (self.randomtype_of_data == 3): # all columns are float
           for x in col_name:
                df[x] = self.GenrateColumsData(3, 0, 100)
        
        if (self.randomtype_of_data == 4): # all columns are string
           for x in col_name: 
                df[x] = self.GenrateColumsData(4, 0, 100)
        
        if (self.randomtype_of_data == 5): # all columns are time
           for x in col_name: 
                df[x] = self.GenrateColumsData(5, 0, 100)
        return df
        
    def GenrateColumsData(self, typ, mini, maxi):
        if (typ == 2): # int
            return  self.generate_random_int(mini, maxi)
        if (typ == 3): # float
            return  self.generate_random_float(mini, maxi)
        if (typ == 4): #string
            return self.generate_random_string(mini, maxi)
        if (typ == 5): # time
            return self.generate_random_time(mini, maxi)
        
            
        
    def generate_random_float(self, mini, maxi, uniform = True): # uniform = false -> normal distruibution
       if (uniform):
           return np.random.uniform(mini, maxi,self.number_of_rows)
       else:
           return np.random.normal(mini, maxi, self.number_of_rows)
    
    
    def generate_random_int(self, mini, maxi):
        return np.random.randint(mini,maxi,self.number_of_rows)
    
    def generate_random_time(self, mini, maxi):
        pass
    
    def generate_random_string(self, min_length, max_length):
        pass
  

s = Datagenerateor(5, 5).data
print(s)