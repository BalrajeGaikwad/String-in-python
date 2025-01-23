#4.Write a program that accepts a sentence and calculate the number of letters and digits

def count_letters_digits(sentence):
  """
  Counts the number of letters and digits in a given sentence.

  Args:
    sentence: The input sentence.

  Returns:
    A tuple containing the count of letters and digits.
  """

  letter_count = 0
  digit_count = 0

  for char in sentence:
    if char.isalpha():
      letter_count += 1
    elif char.isdigit():
      digit_count += 1

  return letter_count, digit_count

# Get input from the user
sentence = input("Enter a sentence: ")

# Calculate the number of letters and digits
letters, digits = count_letters_digits(sentence)

# Print the results
print(f"Number of letters: {letters}")
print(f"Number of digits: {digits}")