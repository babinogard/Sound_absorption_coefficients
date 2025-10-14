
def user_interface(): #This function is user interface. It gets dimmensions from user to calcualte surface later.

    print("hello user!\nPlease type in your parameters.\nThis will allow us to complete your calculations:)")
    length, width, height = float(input("Length of room (m) : ")),float(input("Width of room (m) : ")),float(input("Height of room (m) : "))
    print(f"These are dimmensions of your room: {length}x{width}x{height}m")

    #print(user_interface())

    #print(f"These are dimmensions of your room: {length}x{width}x{height}m")

    #def my_func():
    #    return "Python", 42, [1,2,3]

    #print(my_func())

    return length, width, height
 

def calc_surface():

    length, width, height = user_interface()

    walls = length*height*2+width*height*2
    ceilling = length*width
    floor = length*width

    return walls, ceilling, floor


print(calc_surface())


