# This script uses a mutable list to simulate a single memory location 
# whose address (ID) stays constant even as the value stored inside is overwritten.

# 1. Simulate Allocation and Garbage Value
# The variable 'data_slot' is a list (a container) holding one item: the placeholder.
data_slot = ["OLD_GARBAGE_VALUE"]
print("--- Step 1: Check Memory Slot ---")
print(f"Current Value: {data_slot[0]}")
# The ID of the list itself acts as the fixed 'Conceptual Address' for this storage slot.
print(f"Object ID (Conceptual Address): {id(data_slot)}")

# Simple separator
print("-" * 30)

# 2. User Overwrites the Value at the Same Address
print("--- Step 2: Write New Data IN PLACE ---")
# Ask the user for input. 
user_input = input("Enter your new favorite number or word: ")

# THIS IS THE KEY: We are not reassigning the variable 'data_slot'.
# We are overwriting the content of the first element in the list.
# This simulates changing the value at a fixed memory location.
data_slot[0] = user_input

# Simple separator
print("-" * 30)

# 3. Print the New Contents and Verify the Address
print("--- Step 3: Verify Memory Slot Contents ---")
print(f"Current Value: {data_slot[0]}")
# We check the Object ID again. Because we only modified the content and did not 
# create a new list, the ID (Conceptual Address) remains the same!
print(f"Object ID (Conceptual Address): {id(data_slot)}")

# Lesson Summary: This demonstrates a true 'overwrite'.
# The memory address stayed constant, but the value stored inside was replaced 
# by the user's input. The old value is now completely gone!