4.def permute(s, l, r):
    if l == r:
        print("".join(s))  
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l]  
            permute(s, l + 1, r)  
            s[l], s[i] = s[i], s[l]  
string = input("Enter a string: ")
n = len(string)
permute(list(string), 0, n - 1)




5.import re

text = "Hello World"

match = re.match(r'^Hello', text)
print("Match Start Pattern:", bool(match))

search = re.search(r'World', text)
print("Search Pattern:", bool(search))

all_occurrences = re.findall(r'l', text)
print("Find All Occurrences:", all_occurrences)

replaced_text = re.sub(r'World', 'Everyone', text)
print("Replaced Text with RE:", replaced_text)

split_by_re = re.split(r' ', text)
print("Split by RE:", split_by_re)

s1 = "Hello"
s2 = "World"
concat_str = s1 + " " + s2
print("Concatenation:", concat_str)

s = "Python"
reversed_str = s[::-1]
print("Reversed String:", reversed_str)

substring = s[1:4]
print("Sliced String:", substring)

upper_str = s.upper()
lower_str = s1.lower()
print("Upper Case:", upper_str)
print("Lower Case:", lower_str)

index = concat_str.find("World")
print("Substring found at index:", index)

replaced_str = concat_str.replace("World", "Everyone")
print("Replaced String:", replaced_str)

split_str = concat_str.split(" ")
print("Split String:", split_str)

joined_str = "-".join(split_str)
print("Joined String:", joined_str)

alphanumeric_check = s.isalnum()
print("Is Alphanumeric:", alphanumeric_check)

count_occurrences = concat_str.count("l")
print("Occurrences of 'l':", count_occurrences)





6.with open('eg.txt','w') as file:
    file.write("Hello this is some random Text.\n")
    file.write("This is VKZ.\n")

with open('eg.txt', 'a') as file:
    file.write("Appending new content to the file.\n")

with open('eg.txt','r') as file:
    contents=file.read()
print("Contents in the file:")
print(contents)




7.stack = []

while True:
    print("\nChoose an operation: 1) Push 2) Pop 3) Peek 4) Display 5) Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':  
        element = input("Enter element to push: ")
        stack.append(element)
        print(f"{element} pushed to stack")

    elif choice == '2':  
        if stack:
            print(f"Popped element: {stack.pop()}")
        else:
            print("Stack is empty")

    elif choice == '3':  
        if stack:
            print("Top element:", stack[-1])
        else:
            print("Stack is empty")

    elif choice == '4':  
        print("Stack:", stack)

    elif choice == '5':  
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please try again.")



8.import pandas as pd

df = pd.read_csv(r'C:\Users\vikaa\OneDrive\Documents\sam1.csv')

print("DataFrame:\n", df)

print("\nStatistics:\n", df.describe())
print("\nShape:\n", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nNames:\n", df['Name'])

high_salary = df[df['Salary'] > 55000]
print("\nEmployees with Salary > 55000:\n", high_salary)

df['Salary after Tax'] = df['Salary'] * 0.8
print("\nDataFrame with Salary after Tax:\n", df)

average_salary_by_age = df.groupby('Age')['Salary'].mean().reset_index()
print("\nAverage Salary by Age:\n", average_salary_by_age)



9.import matplotlib.pyplot as plt
import numpy as np

data = [1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5]

counts, bins, patches = plt.hist(data, bins=5, edgecolor='black', alpha=0.6)

bin_centers = 0.5 * (bins[:-1] + bins[1:]) 
plt.plot(bin_centers, counts, color='red', marker='o', linestyle='-', label='Line connecting bars')

plt.title('Histogram with Marked Bars and Line')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()




10.import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([("Protein1", "Protein2"), ("Protein1", "Protein3"), ("Protein2", "Protein4"), ("Protein3", "Protein4")])

nx.draw(G, with_labels=True, node_size=500, node_color="gray")
plt.title("Protein-Protein Interaction Graph")
plt.show()