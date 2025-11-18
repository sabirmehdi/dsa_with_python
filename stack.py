stack = []   # stack to store actions

# User types text
stack.append("Typed A")
stack.append("Typed B")
stack.append("Typed C")

print("Actions:", stack)

# User presses Undo
last_action = stack.pop()
print("Undo:", last_action)

print("Remaining actions:", stack)
