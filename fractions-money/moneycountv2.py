import random

a = 'DCNP'

def get_rand(a,b):
    return str(random.randint(a,b))
arr = [[0 for i in range(4)] for j in range(20)]
arr1 = ["" for i in range(20)]
print("money-counting normal Addition")
for i in range(20):
    arr[i][0] = get_rand(1,100)
    arr[i][1] = get_rand(1,10)
    arr[i][2] = get_rand(1,10)
    arr[i][3] = get_rand(1, 100)
    z = ((arr[i][0])+" D + " + (arr[i][1])+" C + " + (arr[i][2])+" N + " +(arr[i][3]) + " P =")
    arr1[i] = ((arr[i][0]) + " D + " + (arr[i][1]) + " C + " + (arr[i][2]) + " N + " + (arr[i][3]) + " P")
    print(z)

for j in range(1):
    arr2 = ["" for i in range(20)]
    print("money-counting random Addition")
    print()
    for i in range(20):
        r = get_rand(2,4)
        l = random.sample(a,int(r))
        z = ""
        k = []
        if 'D' in l:
            k.append('D')
        if 'C' in l:
            k.append('C')
        if 'N' in l:
            k.append('N')
        if 'P' in l:
            k.append('P')

        for d in k:
            if d == 'D':
                z+=get_rand(1,int(arr[i][0])) +" "+ d + " + "
            elif d=='P':
                z += get_rand(1, int(arr[i][3])) + " " + d + " + "
            elif d=='C':
                z+=get_rand(1,int(arr[i][1])) +" "+ d +" + "
            else:
                z += get_rand(1, int(arr[i][2])) + " " + d + " + "
        z = z[:-3]
        print(z+" =")
        arr2[i] = z
    print()

    print("money-counting random Subtraction")
    for i in range(20):
        print("("+arr1[i] + ") - " + "("+arr2[i]+")" + " =")
    #print(arr1)
    #print(arr2)