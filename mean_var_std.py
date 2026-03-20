import numpy as np

def calculate(values):
  if len(values) < 9:
    return "List must contain nine numbers."
  else:
   
    matrix = np.array(values).reshape(3, 3)
    
    mean_axis0 = np.mean(matrix, axis=0).tolist()
    mean_axis1 = np.mean(matrix, axis=1).tolist()
    mean_flattened = float(np.mean(matrix))

    variance_axis0 = np.var(matrix, axis=0).tolist()
    variance_axis1 = np.var(matrix, axis=1).tolist()
    variance_flattened = float(np.var(matrix))

    std_dev_axis0 = np.std(matrix, axis=0).tolist()
    std_dev_axis1 = np.std(matrix, axis=1).tolist()
    std_dev_flattened = float(np.std(matrix))

    max_axis0 = np.max(matrix, axis=0).tolist()
    max_axis1 = np.max(matrix, axis=1).tolist()
    max_flattened = int(np.max(matrix))

    min_axis0 = np.min(matrix, axis=0).tolist()
    min_axis1 = np.min(matrix, axis=1).tolist()
    min_flattened = int(np.min(matrix))

    sum_axis0 = np.sum(matrix, axis=0).tolist()
    sum_axis1 = np.sum(matrix, axis=1).tolist()
    sum_flattened = int(np.sum(matrix))

    return_val = {
        'mean': [mean_axis0, mean_axis1, mean_flattened],
        'variance': [variance_axis0, variance_axis1, variance_flattened],
        'standard deviation': [std_dev_axis0, std_dev_axis1, std_dev_flattened],
        'max': [max_axis0, max_axis1, max_flattened],
        'min': [min_axis0, min_axis1, min_flattened],
        'sum': [sum_axis0, sum_axis1, sum_flattened]
    }
    return return_val

values = [0,1,2,3,4,5,6,7,8]
print(calculate(values))
