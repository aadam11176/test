
from random import randint
import pandas as pd
import numpy as np




class Datagenerateor:
    # type of data: 1 -> random type for all columns.
    #               2 -> all columns same type (int)
    #               3 -> all columns same type (float)
    #               4 -> all columns same type (string) 
    #               5 -> all columns same type (time) 
    def __init__(self, number_of_columns, number_of_rows, generator_type = 1 ):
        
        self.number_of_columns = number_of_columns
        self. number_of_rows = number_of_rows
        self.generator_type = generator_type
        self.data = self.Maingenerateor()
        self.mini = 0
        self.maxi = 100
        
    # the main generator: depending on the type it will create the data set 
    def Maingenerateor(self):
        col_name = [str(i) for i in range (self.number_of_columns)]
        df = pd.DataFrame()
        if (self.generator_type == 1): # all columns are random type
            for x in col_name:
                df[x] = self.GenrateColumsData(randint(2,3), self.mini, self.maxi) #change 3 to 5
        
        if (self.generator_type == 2): # all columns are int
            for x in col_name:   
                df[x] = self.GenrateColumsData(2, self.mini, self.maxi)
        
        if (self.generator_type == 3): # all columns are float
           for x in col_name:
                df[x] = self.GenrateColumsData(3, self.mini, self.maxi)
        
        if (self.generator_type == 4): # all columns are string
           for x in col_name: 
                df[x] = self.GenrateColumsData(4, self.mini, self.maxi)
        
        if (self.generator_type == 5): # all columns are time
           for x in col_name: 
                df[x] = self.GenrateColumsData(5, self.mini, self.maxi)
        return df
        
    # help function for creating each row
    def GenrateColumsData(self, typ, mini, maxi):
        if (typ == 2): # int
            return  self.generate_random_int(mini, maxi)
        if (typ == 3): # float
            return  self.generate_random_float(mini, maxi)
        if (typ == 4): #string
            return self.generate_random_string(mini, maxi)
        if (typ == 5): # time
            return self.generate_random_time(mini, maxi)
        
    # very simple help functions to create random data
        
    def generate_random_float(self, mini, maxi, uniform = True): # uniform = false -> normal distruibution
       if (uniform):
           return np.random.uniform(mini, maxi,self.number_of_rows)
       else:
           return np.random.normal(mini, maxi, self.number_of_rows)
    
    
    def generate_random_int(self, mini, maxi):
        return np.random.randint(mini,maxi,self.number_of_rows)
    # to do 
    def generate_random_time(self, mini, maxi):
        pass
    # to do
    def generate_random_string(self, min_length, max_length):
        pass
  

s = Datagenerateor(5, 5).data
print(s)
