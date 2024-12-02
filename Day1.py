def populate_lists(file_path,separator):
    list1 = []
    list2 = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by space and convert to integers
            first, second = map(int, line.split(separator))
            list1.append(first)
            list2.append(second)
    
    return list1, list2


def calculate_distance(left,right):
    total_sum=0
    left.sort()
    right.sort()
    print(left)
    print(right)
    for i in range(len(left)):
        total_sum+=abs(left[i]-right[i])
    return total_sum

def similarity_score(left,right):
    score = 0
    for i in range(len(left)):
        count = right.count(left[i])
        score+=left[i]*count
    return score


# Example usage
file_path = "input.txt"  # Replace with your file path
separator = "   "
list1, list2 = populate_lists(file_path,separator)

answer=calculate_distance(list1,list2)
print(answer)
answer2=similarity_score(list1,list2)
print(answer2)


