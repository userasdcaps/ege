f=open("27-73b.txt")
N=int(f.readline())
nums=[]
for i in range(N):
    nums.append(int(f.readline()))
#print(nums)
tails_even = {0:0}
tails_odd = {}
cursum=0
bestsum=0
for i in range(N):
    cursum+=nums[i]
    #print(nums[i],cursum, cursum%93)
    if cursum % 2 == 0:
        if cursum%93 in tails_odd.keys():
            bestsum=max(bestsum, cursum - tails_odd[cursum%93])
        if cursum%93 not in tails_even.keys():
            tails_even[cursum%93] = cursum
    else:#cursum odd
        if cursum%93 in tails_even.keys():
            bestsum=max(bestsum, cursum - tails_even[cursum%93])
        if cursum%93 not in tails_odd.keys():
            tails_odd[cursum%93] = cursum
print(bestsum)