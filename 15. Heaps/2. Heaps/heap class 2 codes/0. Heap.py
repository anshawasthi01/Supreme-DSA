import heapq
# heapify() default convert in minHeap
# shift + alt

hp = [2,3,4,56,3,2,2,2,5,7,8,8,65,4,2,1,2,4,5,6]
hp1 = hp[:]
hp1 = [-x for x in hp1]
heapq.heapify(hp) # minHeap negative krke element daalo nikaalte time b negative krdo max heap bn jaayega fr
hp1 = [-x for x in hp1]

heapq._heapify_max(hp1)
# heapq.heappush(hp, item)
# heapq.heappop(hp)

print(hp, hp1)