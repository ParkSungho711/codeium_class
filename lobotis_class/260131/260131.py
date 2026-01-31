num = "123.456"
x = len(num.split(".")[0])
y = round(float(num), 2)
print(x+y)

start = 1.25
elapsed = 2.80 
end = start + elapsed  
print(int(end - start))

d = {'apple':1, 'banana': 2}
d['apple'] = 3
print(d['apple'] + d['banana'])

t1 = (0,1,2,3,4) 
t2 = sorted(t1[1:])
result = len(t2)
print(result, t2)