import heapq
H=[21,1,45,78,3,5]
heapq.heapify(H)
print(H)
heapq.heappush(H,8) #insertion
print(H)
heapq.heappop(H) #deletion
print(H)
heapq.heapreplace(H,6) #Replace
print(H)