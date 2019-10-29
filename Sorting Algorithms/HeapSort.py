class Heap:
      def __init__(self):
               self.arr=[]
               self.Size=len(self.arr)
 
      def maxHeapify(self,idx):
              largest=idx
              left=2*idx+1
              right=2*idx+2
 
              if left<self.Size and self.arr[left] >self.arr[largest]:
                       largest=left
              if right<self.Size and self.arr[right] >self.arr[largest]:
                       largest=right
              if not largest==idx:
                         self.arr[largest],self.arr[idx]=self.arr[idx],self.arr[largest]
                         self.maxHeapify(largest)
 
 
      def buildHeap(self,array):
               self.Size=len(array)
               self.arr=array
               i=(self.Size-2)/2
               while i>=0:
                     self.maxHeapify(i)
                     i-=1
 
 
 
def heapSort(heap):
       while heap.Size >1:
               heap.arr[0],heap.arr[heap.Size-1]=heap.arr[heap.Size-1],heap.arr[0]
               heap.Size-=1
               heap.maxHeapify(0)
 
nos=map(int,raw_input("Enter no's: ").split())
h=Heap()
h.buildHeap(nos)
print nos   
heapSort(h)
print nos 
