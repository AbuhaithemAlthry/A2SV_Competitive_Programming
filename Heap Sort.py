# User function Template for python3

class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l

        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # Index of last non-leaf node
        startIdx = (n // 2) - 1

        # Perform reverse level order traversal
        # from last non-leaf node and heapify
        # each node
        for i in range(startIdx, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        # Build heap (rearrange array)
        self.buildHeap(arr, n)

        # One by one extract an element from heap
        for i in range(n - 1, 0, -1):
            # Move current root to end
            arr[i], arr[0] = arr[0], arr[i]

            # call max heapify on the reduced heap
            self.heapify(arr, i, 0)
