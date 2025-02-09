def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list to prevent ZeroDivisionError
    return sum(numbers) / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Further Improvement
def calculate_average(numbers):
  """Calculate the average of numbers in a list.

  Args:
      numbers: A list of numbers.

  Returns:
      The average of the numbers in the list. Returns 0 if the list is empty.
      Raises TypeError if input is not a list or if the list contains non-numeric values.
  """
  if not isinstance(numbers, list):
    raise TypeError("Input must be a list.")
  if not numbers:
    return 0
  if not all(isinstance(num, (int, float)) for num in numbers):
    raise TypeError("List must contain only numbers.")
  return sum(numbers) / len(numbers)