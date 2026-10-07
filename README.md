# 0/1 Knapsack Using Dynamic Programming

## 1. Problem Statement

A passenger is travelling by train with a limited luggage allowance of **W kg**. Each luggage item has a **weight** and a **usefulness value**. The passenger can either carry or leave each item and cannot carry fractions of an item.

The objective is to select luggage items that maximize the total usefulness without exceeding the maximum luggage capacity.

---

## 2. Objective

To implement the **0/1 Knapsack problem using Dynamic Programming** and display:

- Maximum achievable usefulness
- Selected luggage items
- Total weight
- DP table
- Time and space complexity

---

## 3. Algorithm

1. Read the number of luggage items.
2. Read the name, weight, and usefulness of each item.
3. Read the maximum luggage capacity `W`.
4. Create a DP table of size `(n+1) × (W+1)`.
5. For each item, check whether it can fit into the current capacity.
6. If it fits, calculate both:
   - Usefulness when the item is included.
   - Usefulness when the item is excluded.
7. Store the maximum of the two values in the DP table.
8. Trace the DP table backward to identify the selected items.
9. Display the maximum usefulness, selected items, total weight, and DP table.

---

## 4. Program

```python
# 0/1 Knapsack using Dynamic Programming

n = int(input("Enter number of luggage items: "))

items = []
weights = []
values = []

# Take item details
for i in range(n):
    print(f"\nEnter details for Item {i + 1}")

    name = input("Enter item name: ")
    weight = int(input("Enter weight (kg): "))
    usefulness = int(input("Enter usefulness value: "))

    items.append(name)
    weights.append(weight)
    values.append(usefulness)

# Take maximum capacity
W = int(input("\nEnter maximum luggage capacity (kg): "))

# Create DP table
dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(W + 1):

        if weights[i - 1] <= w:
            include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
            exclude_item = dp[i - 1][w]

            dp[i][w] = max(include_item, exclude_item)

        else:
            dp[i][w] = dp[i - 1][w]

# Find selected items
selected_items = []
w = W

for i in range(n, 0, -1):

    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i - 1)
        w = w - weights[i - 1]

selected_items.reverse()

# Display result
print("\n" + "=" * 60)
print("             0/1 KNAPSACK RESULT")
print("=" * 60)

print("\nMaximum Achievable Usefulness:", dp[n][W])

print("\nSelected Luggage Items:")
print("-" * 60)

total_weight = 0
total_usefulness = 0

for i in selected_items:
    print(
        f"{items[i]} -> "
        f"Weight: {weights[i]} kg, "
        f"Usefulness: {values[i]}"
    )

    total_weight += weights[i]
    total_usefulness += values[i]

print("-" * 60)
print("Total Weight     :", total_weight, "kg")
print("Total Usefulness :", total_usefulness)

# Display DP table
print("\nDP TABLE")
print("-" * 60)

print(f"{'Item':<15}", end="")

for w in range(W + 1):
    print(f"{w:5}", end="")

print()

for i in range(n + 1):

    if i == 0:
        print(f"{'None':<15}", end="")
    else:
        print(f"{items[i - 1]:<15}", end="")

    for w in range(W + 1):
        print(f"{dp[i][w]:5}", end="")

    print()

print("-" * 60)

print("\nTime Complexity  : O(n × W)")
print("Space Complexity : O(n × W)")
```

---

## 5. Sample Input

```text
Enter number of luggage items: 4

Enter details for Item 1
Enter item name: Laptop
Enter weight (kg): 3
Enter usefulness value: 30

Enter details for Item 2
Enter item name: Camera
Enter weight (kg): 2
Enter usefulness value: 20

Enter details for Item 3
Enter item name: Clothes
Enter weight (kg): 4
Enter usefulness value: 40

Enter details for Item 4
Enter item name: Books
Enter weight (kg): 1
Enter usefulness value: 10

Enter maximum luggage capacity (kg): 6
```

---

## 6. Sample Output

```text
============================================================
             0/1 KNAPSACK RESULT
============================================================

Maximum Achievable Usefulness: 60

Selected Luggage Items:
------------------------------------------------------------
Camera -> Weight: 2 kg, Usefulness: 20
Clothes -> Weight: 4 kg, Usefulness: 40
------------------------------------------------------------
Total Weight     : 6 kg
Total Usefulness : 60

DP TABLE
------------------------------------------------------------
Item               0    1    2    3    4    5    6
None               0    0    0    0    0    0    0
Laptop             0    0    0   30   30   30   30
Camera             0    0   20   30   30   50   50
Clothes            0    0   20   30   40   50   60
Books              0   10   20   30   40   50   60
------------------------------------------------------------

Time Complexity  : O(n × W)
Space Complexity : O(n × W)
```

---

## 7. Code Explanation

### Input

The program takes:

- Number of items
- Item name
- Weight of each item
- Usefulness of each item
- Maximum luggage capacity

### DP Table

`dp[i][w]` represents the maximum usefulness obtained using the first `i` items with a capacity of `w`.

### Include or Exclude

For every item, the program checks two possibilities:

```text
Include the item
OR
Exclude the item
```

The option with greater usefulness is selected.

### Finding Selected Items

The program traces the DP table backward from `dp[n][W]` to determine which items were selected.

---

## 8. Time Complexity

**O(n × W)**

where:

- `n` = number of luggage items
- `W` = maximum luggage capacity

The DP table has `(n+1) × (W+1)` entries.

---

## 9. Space Complexity

**O(n × W)**

because the complete DP table is stored in memory.

---

## 10. Result

The 0/1 Knapsack problem was successfully implemented using Dynamic Programming to maximize luggage usefulness within the given weight capacity.

---

# 11. Viva Questions and Answers

### 1. What is 0/1 Knapsack?

**Answer:** It is a problem where each item is either completely selected or not selected.

### 2. Why is Dynamic Programming used?

**Answer:** It avoids repeated calculations by storing solutions to subproblems.

### 3. What does `dp[i][w]` represent?

**Answer:** It represents the maximum usefulness using the first `i` items with capacity `w`.

### 4. What is the time complexity?

**Answer:** The time complexity is **O(n × W)**.

### 5. What is the space complexity?

**Answer:** The space complexity is **O(n × W)**.

### 6. What does `W` represent?

**Answer:** `W` represents the maximum luggage weight capacity.

### 7. What is the main condition in 0/1 Knapsack?

**Answer:** Each item can be either selected completely or rejected.

### 8. How are selected items identified?

**Answer:** We trace the DP table backward from `dp[n][W]` to find the selected items.

---

## 12. Conclusion

The 0/1 Knapsack problem was successfully solved using Dynamic Programming. The program efficiently selects the most useful combination of luggage items without exceeding the given weight capacity.