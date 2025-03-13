# Program to completely remove duplicate elements without keeping any copy

def remove_all_duplicates(lst):
    unique_elements = []
    duplicates = set()
    
    for num in lst:
        if num in unique_elements:
            duplicates.add(num)
        else:
            unique_elements.append(num)
    
    result = [num for num in unique_elements if num not in duplicates]
    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print("List after completely removing duplicates:", remove_all_duplicates(numbers))
