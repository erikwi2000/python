""" test """
inputFile = open('httpd-access.txt', 'r+')
count = 0
for cheese in inputFile:
    xx = cheese.split()
    zz = len(xx)
    strdd = ''.join(xx[zz-1:])    
    if strdd != '-':
        pp = int(strdd)
        pp_string = str(pp)
      #  print(pp_string[:2])
       # print(pp_string[-1:])
        strss = int(pp_string[-1:])
    if strss % 2 == 0:
        count = count + strss

print("count  " + str(count))   

