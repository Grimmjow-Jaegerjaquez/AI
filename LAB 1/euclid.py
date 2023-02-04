def Euclid_distance(x, y):
    return ((x - y) ** 2) ** 0.5

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1],arr[j]

    return arr

no = int(input("Enter number of points : "))

x = []
y = []

for i in range(no):
    x.append(int(input()))
    y.append(int(input()))


dis = []

for i in range(no):
    dis.append([i,Euclid_distance(x[i],y[i])])

sorted_dis = bubble_sort(dis)
print(sorted_dis)