def hello():
    print("hello, user")

hello()

def pack(a, b, c):
    packed_list = [a, b, c]
    print(packed_list)

pack('Toast', 'Eggs', 'Turkey')

def eat_lunch(packed_list):
    if not packed_list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {packed_list[0]}")
        for item in packed_list[1:]:
            print(f"Next I eat {item}")
            
lunch_items = ['Toast', 'Eggs', 'Turkey']
eat_lunch(lunch_items)

