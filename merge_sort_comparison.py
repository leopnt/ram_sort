import time
import random
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from ram_sort import *

def tri_std(data):
    # Basic sorting algorithm

    tab = data.copy()
    for i in range(len(tab) - 1):
        for j in range(len(tab) - 1):
            if tab[j + 1] < tab[j]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]
    
    return tab

def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    
    return True

def get_dt_per_size(algorithm, data, data_size, resolution, avg_resolution):
    """ sort and evaluate time taken """

    x = []
    z = []

    step = data_size / resolution

    for i in np.arange(0, data_size, step):
        avg = 0
        sub_data = data[:int(i)]
        for _j in range(avg_resolution):
            start = time.time()
            tri = algorithm(sub_data)
            end = time.time()

            avg += (end - start)

            # DEBUG: check if array is well sorted
            """
            check_sorted = is_sorted(tri)
            if not check_sorted:
                print("not sorted")
                return
            """

        x.append(i)
        z.append(avg/5)

        print(" ", round(map(i, 0, data_size - step, 0, 100)), "%", end="\r")

    print()

    return (x, z)


def main():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    ax.set_xlabel('Array range')
    ax.set_ylabel('Array size')
    ax.set_zlabel('Avg time taken')

    x = []

    nb_points = 20

    for max_rand in range(1, nb_points + 1):
        data = []
        max_nb_data = 4000
        for _k in range(max_nb_data):
            data.append(float(random.uniform(0, 1000 * max_rand)))

        dt1 = get_dt_per_size(merge_sort, data, max_nb_data, nb_points, 10)
        z = dt1[1]
        y = dt1[0]
        x = [1000 * max_rand] * nb_points
        
        if (max_rand == 1):
            ax.plot3D(x, y, z, 'gray', label="Merge sort")
        else:
            ax.plot3D(x, y, z, 'gray')

    for max_rand in range(1, nb_points + 1):
        data = []
        max_nb_data = 4000
        for _k in range(max_nb_data):
            data.append(float(random.uniform(0, 1000 * max_rand)))

        dt1 = get_dt_per_size(ram_sort, data, max_nb_data, nb_points, 10)
        z = dt1[1]
        y = dt1[0]
        x = [1000 * max_rand] * nb_points
        
        if (max_rand == 1):
            ax.plot3D(x, y, z, 'red', label="Ram sort")
        else:
            ax.plot3D(x, y, z, 'red')

    ax.legend()

    fig.show()

    input()

    """
    start = time.time()
    tri_2 = ram_sort(data)
    #print(tri_2)
    end = time.time()

    start = time.time()
    tri_3 = merge_sort(data)
    #print(tri_2)
    end = time.time()
    print("merge method done in ", end - start, "seconds")
    """

if __name__ == "__main__":
    main()
 