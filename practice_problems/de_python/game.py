target=["apple","orange","ananas","banana","pear"]
sample=["apple","pear","pineapple","blue"]
def transformer(target,sample):
    for i in sample:
        if i not in target:
            sample.remove(i)
    for index,x in enumerate(target):
        if x not in sample:
            sample.insert(index,x)
 
    return sample
    

print(transformer(target,sample))

