import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("financial_dataset.csv")

# Convert amount to string
first_digits = df['amount'].astype(str).str[0]
# Get the first digit for every value
first_digits = first_digits[first_digits != '0']
# Get Series with occurences of each first digit
result = first_digits.value_counts().sort_index()
# Plot the frequency of each digit on bar graph
result.plot(kind='bar', title= "Frequency of First Digit Number in Spendings Amount")
plt.show()
