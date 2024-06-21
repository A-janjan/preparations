#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#



def minimumBribes(q):
    sums = 0
    for i in range(len(q)):
        diff = q[i] - (i+1)
        if(diff > 2):
            print("Too chaotic")
            return
        else:
            sums += sum(1 for item in q[i+1:] if item<q[i])
        
    print(sums)
    return

q = [1, 2, 5, 3, 7, 8, 6, 4]

minimumBribes(q)