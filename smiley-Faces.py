'''
Created on Dec 4, 2020

@author: Salzaidy
'''

def count_smileys(arr):
    
    smileyFaces = [':~)', ':)', ':-)', ';~)', ';-)', ':D', ';~D', ';-D', ':-D',  ';D']
    
    count = 0
    
    for face in arr:
        if face in smileyFaces:
            count += 1    
    return count
    
    

s1 = count_smileys([':D',':~)',';~D',':)']) # 4
s2 = count_smileys([':)',':(',':D',':O',':;']) # 2
s3 = count_smileys([';]', ':[', ';*', ':$', ';-D']) # 1
print(s1)
print(s2)
print(s3)

d1 = count_smileys([':)', ';(', ';}', ':-D']) # 2
d2 = count_smileys([';D', ':-(', ':-)', ';~)']) # 3
d3 = count_smileys([';]', ':[', ';*', ':$', ';-D']) # 1
print(d1)
print(d2)
print(d3)