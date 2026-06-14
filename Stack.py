Stack=[]


def push(element):
    Stack.append(element)
    print(f"{element} has been pushed to the Stack")

def pop():
    if is_empty():
        print("Stack is empty. Cannot pop an element. Condition: UNDERFLOW")
    else:
        element=Stack.pop()
        print(F"{element} has been popped fromt the Stack")

def is_empty():
    return len(Stack)==0

def size():
    print(f"The size of the Stack is: {len(Stack)}")

def peek():
    if is_empty():
        print("Stack is empty. Cannot peek an element. Condition: UNDERFLOW")
    else:
        element=Stack[-1]
        print(f"The top element of the Stack is: {element}")