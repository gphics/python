# the function that rearrange the list
def sorter(unordered_list):
    start_index = 0
    last_end_index = len(unordered_list) - 1
    end_index = 1
    sorting_state = True
    # if the function state is true
    while sorting_state:
        # checking if the start === current end
        if start_index == last_end_index:
            sorting_state = False
        # if the start index element of the list is greater than the end index element then swap
        elif unordered_list[start_index] > unordered_list[end_index]:
            # getting the values (start and end index ) from the list
            current_start_value = unordered_list[start_index]
            current_end_value = unordered_list[end_index]
            # swapping the values
            unordered_list[end_index] = current_start_value
            unordered_list[start_index] = current_end_value
            # incrementing the start and end index values
            start_index += 1
            end_index += 1
        # if the values are normal
        else:
            start_index += 1
            end_index += 1
    return unordered_list


# the function that check if the list is ordered
# returns true if the list is ordered and return false otherwise


def check_sort(sorted_list):
    last_end_index = len(sorted_list) - 1
    end_index = 1
    start_index = 0
    checking_state = True
    result_state = True

    while checking_state:
        # checking if the start index == last end index
        if start_index == last_end_index:
            checking_state = False
            break
        # checking if the start index sorted list value is greater that
        # the end index sorted list value
        # negating the result state if the condition is true
        # and breaking out of the loop
        elif sorted_list[start_index] > sorted_list[end_index]:
            result_state = False
            break
        # if not , increment the start index and end index values
        else:
            start_index += 1
            end_index += 1

    return result_state


def sort(unordered_list):
    sorted_list = sorter(unordered_list)
    checker = check_sort(sorted_list)
    if not checker:
        sort(sorted_list)
    return sorted_list
