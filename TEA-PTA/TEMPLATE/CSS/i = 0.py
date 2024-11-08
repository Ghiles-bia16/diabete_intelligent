dat = [12,19,30,70,7] 
def process_data(data):
     result = []
     for i in range(len(data)):
     if data[i] % 2 == 0:
        result.append(data[i] * 2)
     else:
        temp = data[i] * 3
        result.append(temp)
     return result


print(process_data(dat))