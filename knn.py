import math
dataset = [
[20, 35, 4, "Low"],
[22, 38, 5, "Low"],
[24, 40, 6, "Low"],
[25, 42, 5, "Low"],
[27, 45, 6, "Low"],
[28, 48, 7, "Low"],
[30, 50, 8, "Low"],
[32, 52, 9, "Low"],
[34, 55, 10, "Low"],
[36, 57, 11, "Low"],
[38, 58, 12, "High"],
[40, 60, 13, "High"],
[42, 62, 14, "High"],
[44, 64, 15, "High"],
[46, 66, 16, "High"],
[48, 68, 17, "High"],
[50, 70, 18, "High"],
[52, 72, 19, "High"],
[54, 74, 20, "High"],
[56, 76, 21, "High"],
[29, 47, 7, "Low"],
[31, 49, 8, "Low"],
[33, 53, 9, "Low"],
[37, 59, 11, "High"],
[41, 63, 14, "High"],
[45, 67, 16, "High"],
[26, 44, 6, "Low"],
[35, 56, 10, "Low"],
[47, 69, 17, "High"],
[53, 73, 19, "High"]
]
def euclidean_dist(new,given):
    return math.sqrt(sum((n - g)**2 for n, g in zip(new, given)))
def knn_algoritm(dataset,k,new_customer):
    dist_list=[]
    index=0
    for node in dataset:
        dist_list.append((index,euclidean_dist(node[:-1],new_customer),node[-1]))
        index+=1
    dist_list.sort(key=lambda x: x[1])
    print("Kth nearest neighbours are:",dist_list[:3])
    nearest_neigh=dist_list[:3]
    high_count=0
    low_count=0
    for index,dist,tag in nearest_neigh:
        if tag == 'High':
            high_count+=1
        elif tag =='Low':
            low_count+=1
    if high_count>low_count:
        return 'High'
    else:
        return 'Low'
k=3
new_customer = [38, 58, 11]
print("Predicted outcome for:",new_customer," is ",knn_algoritm(dataset,k,new_customer))
