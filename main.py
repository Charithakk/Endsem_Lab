# 0/1 Knapsack using Dynamic Programming

# Take number of items
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


# ---------------- OUTPUT ----------------

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


# ---------------- DP TABLE ----------------

print("\nDP TABLE")
print("-" * 60)

# Capacity headings
print(f"{'Item':<15}", end="")

for w in range(W + 1):
    print(f"{w:5}", end="")

print()

# Table rows
for i in range(n + 1):

    if i == 0:
        print(f"{'None':<15}", end="")
    else:
        print(f"{items[i - 1]:<15}", end="")

    for w in range(W + 1):
        print(f"{dp[i][w]:5}", end="")

    print()

print("-" * 60)

# Complexity
print("\nTime Complexity  : O(n × W)")
print("Space Complexity : O(n × W)")