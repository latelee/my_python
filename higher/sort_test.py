#!/usr/bin/python3
# encoding: utf-8

# 排序示例

from operator import itemgetter, attrgetter

print(sorted('123456', key=None, reverse=True)); # 反序

print(sorted([1,4,5,2,3,6]));

print(sorted({1:'q',3:'c',2:'g'}.items()));

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]

# itemgetter为要排序的对象的序号
# 如0表示根据字符，1表示根据数字
print(sorted(data, key=itemgetter(0)));

teamitems = [{'team':'France'     , 'P':1 , 'GD':-3 , 'GS':1 , 'GA':4},
            {'team':'Uruguay'     , 'P':7 , 'GD':4  , 'GS':4 , 'GA':0},
            {'team':'SouthAfrica' , 'P':4 , 'GD':-2 , 'GS':3 , 'GA':5},
            {'team':'Mexico'      , 'P':4 , 'GD':1  , 'GS':3 , 'GA':2}]

# 依次根据P、GD、GS、GA排序，升序
a = sorted(teamitems ,key = itemgetter('P','GD','GS','GA'),reverse=True)
#print(a)

# 冒泡排序
# 感觉这个正宗一些
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        print("before-------------");
        print(lists); 
        print("<<<<<<<<<<<<<[%d] %d" % (i, lists[i])); 
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]  # 交换
            print(lists);
        print(">>>>>>>>>>>>>>");
        print("after-------------");
        print(lists);
    return lists

def bubble_sort1(lists):
    for i in range(len(lists)-1):    # 这个循环负责设置冒泡排序进行的次数
        print("before-------------");
        print(lists); 
        print("<<<<<<<<<<<<<[%d] %d" % (i, lists[i])); 
        #for j in range(len(lists)-i-1):  # ｊ为列表下标
        for j in range(i):  # ｊ为列表下标
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
            print(lists);
        print(">>>>>>>>>>>>>>");
        print("after-------------");
        print(lists);
    return lists

# 插入排序
def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):

        key = lists[i]
        j = i - 1
        print("before--key: %d j: %d-----------" % (key, j));
        print(lists); 
        print("<<<<<<<<<<<<<");        
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
            
            print(lists);
        print(">>>>>>>>>>>>>>");
        print("after--------------------------");
        print(lists);
        print("--------------------------");
    return lists

list = [5, 4, 9, 1, 3, 7, 10]
print(bubble_sort(list))

print("+++++++++++++++++++++++++++++++++");
#print(insert_sort(list))
