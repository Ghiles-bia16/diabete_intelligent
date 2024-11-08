dat = [12,19,30,70,7]
def process_data(data): 
       result = [] 
       for i in data: 
              if i % 2 == 0:                                     
                     result.append(i * 2) 
              else:  
                    result.append(i * 3) 
       return result 


print(process_data(dat))