gdata = tuple(map(int, input("Enter elements of the tuple separated by spaces: ").split()))

index = next((i for i in range(len(data) - 1) if data[i] == data[i + 1]), -1)

if index != -1:
    print(f"Pair of identical neighbors found at positions: {index} and {index + 1}")
else:
    print("No identical neighboring elements found.")
