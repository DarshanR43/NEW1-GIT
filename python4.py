data = {
    'name': ['John,Ram'],
    'age': [22,25],
}
f1= open('python4','w')
f1.write(str(data))
f1.close()
# f2= open('python4','r')
# print(f2.read())
# f2.close()

import pickle
f2 = open('puthon4.pkl','rb')
dict_input = pickle.load(f2)
print(type(dict_input['name','0']))
