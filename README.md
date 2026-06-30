# Python


# 🐍 Python Functions — Practice

Python functions from basics to advanced concepts.

---

## 📁 File
`function.ipynb`

---

## 🧠 Topics Covered

---

### 1️⃣ Function Basics
A function is a reusable block of code that runs only when called.
```python
def greet():
    print("Good morning")

greet()   # calling the function
```

---

### 2️⃣ return vs print
- `print` → just displays the value, returns `None`
- `return` → sends the value back so you can store and reuse it

```python
# ❌ print — result is None
def add(x, y):
    print(x + y)
result = add(4, 5)   # result = None

# ✅ return — result is 9
def add(x, y):
    return x + y
result = add(4, 5)   # result = 9
```

---

### 3️⃣ Return Multiple Values
When you return multiple values, Python packs them as a **tuple**
```python
def add_sub(x, y):
    return x+y, x-y

result = add_sub(4, 5)        # → (9, -1) tuple
r, r1 = add_sub(4, 5)        # → unpacking → r=9, r1=-1
```

---

### 4️⃣ Positional Argument
Arguments passed in **order** — position matters
```python
def person(name, age):
    print(name, age)

person("nit", 23)   # name=nit, age=23 ✅
person(23, "nit")   # name=23, age=nit ❌ wrong order!
```

---

### 5️⃣ Keyword Argument
Arguments passed by **name** — order doesn't matter
```python
person(age=24, name="nk")   # ✅ works fine
```

---

### 6️⃣ Default Argument
A default value used when no argument is passed
```python
def person(name, age=19):   # age=19 is default
    print(name, age)

person("rk")        # → rk 19 (uses default)
person("rk", 45)    # → rk 45 (overrides default)
```

---

### 7️⃣ Variable Length Argument (`*args`)
When you don't know how many arguments will be passed — collects as **tuple**
```python
def total(*nums):
    print(sum(nums))

total(1, 2, 3, 4, 5)   # works with any number of args
```

---

### 8️⃣ Keyword Variable Length (`**kwargs`)
Collects unknown keyword arguments as a **dictionary**
```python
def info(**data):
    print(data)

info(name="nit", age=23, city="Delhi")
# → {'name': 'nit', 'age': 23, 'city': 'Delhi'}
```

---

### 9️⃣ Lambda Function
A small anonymous one-line function
```python
# normal function
def add(x, y):
    return x + y

# same as lambda
add = lambda x, y: x + y
add(5, 6)   # → 11
```

---

### 🔟 map()
Applies a function to **every item** in a list
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda n: n*2, nums))
# → [2, 4, 6, 8]
```

---

### 1️⃣1️⃣ filter()
Filters items from a list based on a condition
```python
nums = [3, 2, 6, 8, 4, 9]
evens = list(filter(lambda n: n%2==0, nums))
# → [2, 6, 8, 4]
```

---

### 1️⃣2️⃣ reduce()
Reduces a list to a **single value** by applying a function cumulatively
```python
from functools import reduce
nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a+b, nums)
# → 10  (1+2+3+4)
```

---

### 1️⃣3️⃣ Decorator
A function that **wraps another function** to add extra behaviour
```python
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# → before
# → Hello!
# → after
```

---

## 🛠️ Tool
Python 3 · Jupyter Notebook
