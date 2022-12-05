array = [1,3,5,7,9,2,4,6,8,10]
N = len(array)
def make_heap(array, index, heap_size):
    parent = index
    left_child = 2 * parent + 1
    right_child = 2 * parent + 2

    if left_child < heap_size and array[left_child] > array[parent]:
        parent = left_child
    if right_child < heap_size and array[right_child] > array[parent]:
        parent = right_child
    if parent != index:
        array[parent], array[index] = array[index], array[parent]
        make_heap(array, parent, heap_size)

def up_heapify(index, heap):
    child_index = index
    while child_index != 0:
        parent_index = (child_index - 1) // 2
        if heap[parent_index] < heap[child_index]:
                heap[parent_index] = heap[child_index]
                heap[child_index] = heap[parent_index]
                child_index = parent_index
        else:
            return

    # 부모노드가 되는 노드들만을 골라서 뒤에서부터 heapify를 차례로 실행
for i in range((N - 1) // 2, -1, -1):
    print(i)
    make_heap(array, i, N)
print(array)