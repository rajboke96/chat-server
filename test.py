# 1.
# import time

# try:
#     while True:
#         print("Program is running. Press Ctrl+C to interrupt.")
#         time.sleep(1)  # Simulate some work
# except KeyboardInterrupt as e:
#     print(e)
#     print("\nKeyboardInterrupt detected! Performing cleanup...")
#     # Add any cleanup code here, like closing files, releasing resources, etc.
#     print("Cleanup complete. Exiting gracefully.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("This block always executes, regardless of whether an exception occurred or not.")

# 2. 
# def fun(sum, *args):
#     sum(*args)

# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# # print(sum_numbers(1, 2, 3))  # Output: 6
# # print(sum_numbers(10, 20, 30, 40)) # Output: 100
# fun(sum_numbers)

# 3.
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        print("Getting radius...")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        print(f"Setting radius to {value}...")
        self._radius = value

c=Circle(10)
c.radius=1
c2=Circle(10)
c2.radius=20
print(c2.radius)
print(c.radius)