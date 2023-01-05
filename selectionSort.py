def selectionSort(self, arr, n):
        # code here
        for ind in range(n):
            min_index = ind
            for j in range(ind + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])
        return arr

