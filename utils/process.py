from sklearn.model_selection import KFold
import numpy as np

#1. 还原KFold测试集顺序
#2. 最大最小归一化数字的范围
#3. 归一化一整个表格，9126及十折交叉验证


#将KFold数按照顺序进行排列
def reverse_KFold(data):
    kf = KFold(10,True,0)
    #index = []
    for i,[train_index, test_index] in enumerate(kf.split(data)):
        if i==0:
            index = test_index
        else:
            index = np.append(index,test_index,axis=0)
    new_data = [0]*len(data)
   #print(len(new_data))
    for i in range(len(data)):
        new_data[index[i]] = data[i]
    
    return np.array(new_data)

def normalize(data):
    """
    对数组进行最大最小值归一化，返回归一化后的数组
    """
    # 计算数组中的最大值和最小值
    max_value = max(data)
    min_value = min(data)
    # 对数组中每个元素进行归一化
    normalized_data = [(x-min_value)/(max_value-min_value) for x in data]
    return normalized_data

#归一化一个表
def normalize_big(data):
    list_ = [913,913,913,913,913,913,912,912,912,912]
    
    for i in range(len(data[0])):
        sum_ = 0
        for j in range(len(list_)):
            
            data[sum_:sum_+list_[j],i] = normalize( data[sum_:sum_+list_[j],i] )
            sum_+= list_[j]
    return data

#归一化一个表
def normalize_normal(data):
    for i in range(len(data[0])):
        data[:,i] = normalize(data[:,i])
    return data

#归一化一个表
def normalize_test(data1,data):
    
    list_ = [913,913,913,913,913,913,912,912,912,912]
    col = 0
    for i in range(len(data1[0])):
        sum_ = 0
        for j in range(len(list_)):
            max_value = max( data1[sum_:sum_+list_[j],i] )
            min_value = min( data1[sum_:sum_+list_[j],i] )
            data[:,col] = [(x-min_value)/(max_value-min_value) for x in data[:,col]]
            sum_+= list_[j]
            col+=1
    return data