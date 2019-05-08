import random

a = 'DCNP'

def get_rand(a,b):
    return str(random.randint(a,b))
arr = [[0 for i in range(5)] for j in range(20)]
#arr1 = ["" for i in range(20)]
print("MONEY COUNTING \n")
for i in range(20):
    arr[i][0] = get_rand(1,100)
    arr[i][1] = get_rand(1,100)
    arr[i][2] = get_rand(1,100)
    arr[i][3] = get_rand(1,100)
    arr[i][4] = get_rand(1,100)
    z = ((arr[i][0])+" Dollar + " + (arr[i][1])+" Q + " + (arr[i][4])+" Dime + " + (arr[i][2])+" N + " +(arr[i][3]) + " P = __________ Cent and  $ ___________")
    #arr1[i] = ((arr[i][0]) + " Dollar + " + (arr[i][1]) + " Q + " + (arr[i][4])+" Dime "+ (arr[i][2])+" N + "+ (arr[i][3]) + " P")
    print(z)
    print('\n')

#for j in range(1):
   # arr2 = ["" for i in range(20)]
   # print("money-counting random Addition")
   # print()
    #for i in range(20):
      #  r = get_rand(2,4)
       # l = random.sample(a,int(r))
       # z = ""
       # k = []
       # if 'Dollar' in l:
       #     k.append('Dollar')
       # if 'C' in l:
       #     k.append('Q')
       # if 'N' in l:
       #     k.append('N')
       # if 'P' in l:
        #    k.append('P')

        #for d in k:
           # if d == 'Dollar':
            #    z+=get_rand(1,int(arr[i][0])) +" "+ d + " + "
            #elif d=='P':
            #    z += get_rand(1, int(arr[i][3])) + " " + d + " + "
            #elif d=='Q':
            #    z+=get_rand(1,int(arr[i][1])) +" "+ d +" + "
            #else:
           #     z += get_rand(1, int(arr[i][2])) + " " + d + " + "
        #z = z[:-3]
        #print(z+" =")
       # arr2[i] = z
   # print()

    #print("money-counting")
    #for i in range(20):
     #   print("("+arr1[i] + ") - " + "("+arr2[i]+")" + " =")
    #print(arr1)
    #print(arr2)