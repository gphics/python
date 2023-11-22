from .sort import sort


def search(alist, search_param):
    sorted_list = sort(alist)
    result = searcher(sorted_list, search_param)
    # print(result)
    result_type = str(type(result))
    if result_type == "<class 'list'>":
        # print("in the if")
        return search(result, search_param)
    else:
        # print("after the if")
        return result


def searcher(sorted_list, search_param):
    end_index = len(sorted_list) - 1
    mid_index = end_index // 2
    # if the length of the list is equals 1
    if len(sorted_list) == 1:
        # checking if the list content is equals the search param,
        if sorted_list[0] == search_param:
            return result_constructor(search_param, 0)
        # returning not found if list content != search param
        return f"the provided list does not contain the search param {search_param}"
    # if the length of the list is 2
    elif len(sorted_list) == 2:
        # checking if the first element == search param
        if sorted_list[0] == search_param:
            return result_constructor(search_param, 0)
        # checking if the second element == search param
        elif sorted_list[1] == search_param:
            return result_constructor(search_param, 1)
        # returning not found
        return f"the provided list does not contain the search param {search_param}"
    # if the sorted_list middle value == search param
    elif sorted_list[mid_index] == search_param:
        return result_constructor(search_param, mid_index)
    # if the sorted_list middle value > search param
    elif search_param > sorted_list[mid_index]:
        return sorted_list[mid_index : end_index + 1]
    # if the sorted_list middle value < search param
    else:
        return sorted_list[0:mid_index]


def result_constructor(search_param, index):
    return {"search_param": search_param, "index": index}
