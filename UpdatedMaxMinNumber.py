"""
Max and Min Number(python)
Your answer should be returned in an array containing the min and max number, respectively.
"""
def find_max_min(input):
  """
   This function returns the minimum and maximum number in a list
   If the min and max are equal, it returns the number of elements in the list
  """

  resultingList = [] # create a list to hold numbers
  max_num = max(input)
  min_num = min(input)
  if min_num == max_num:
    num_of_elements = len(input)
    resultingList.append(num_of_elements)
  else:
    resultingList.append(min_num)
    resultingList.append(max_num)
  return resultingList