# Task-8

# 1.Create a python class called Circle with Construtor which will take list as an argument for the task. the list is [10,501,22,37,100,999,87,351]
class Circle:
    #construtor
    def __init__(self):
        #passing argument to class using self keyword
        self.List = [10,501,22,37,100,999,87,351]
         #above line we intialize instance variableusing costructor
# 2.create a proper member variables inside the task if required use them when necessary.
class Rectangle:
    # intialize private variable using __
    #once we created private variable it can use only inside class and methods
    __length = 40 # private variable
    __breath = 20
    __pi = 3.14
    # creting method
    def area(self):#it is a instance method
        #self keyword refers to calling object
        # in this method we using self keyword to intialize a variable
        return f'area of rectangle : {self.__length * self.__breath}'
    #creting another method
    def circumfrance(self, radius):
        #in this method we using classname to intialize a variable
        return f'circumfrance of circle : {2 * self.__pi * radius}'
    def area_of_circle(self, radius):
        return f'area of circle : {self.__pi * radius**2}'
#creating object for class
result = Rectangle()
#using that object to call methods
print(result.area())# call instance method
print(result.circumfrance(5))
print(result.area_of_circle(2))

#3.from the given list create two class methods Area and Perimeter which will be going to calaculate Area and Radius

class Circle2:
    List = [10,501,22,37,100,999,87,351]
    pi = 3.14
    def area_of_circle2(self):
        area_list = []
        for get_list in range(len(self.List)):
            area_list.append(self.pi * self.List[get_list]**2)
        return area_list
    def perimeter_of_circle(self):
        perimeter_list = []
        for set_list in range(len(self.List)):
            perimeter_list.append(2 * self.pi * self.List[set_list])
        return perimeter_list
#creating object for class
solution = Circle2()
#using that object to call method
print("area of circle for given List: "+ str(solution.area_of_circle2()))
print("perimeter of circle for given List: "+ str(solution.perimeter_of_circle()))


#4.convert uml diagram into python class and methods:
#Part-A
#1.Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
#2.Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
#3.Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel.
#4.Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).
#5.It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75".
class Tv:
    channel = 1 #default channel is 1
    volume = 50 #default volume is 50
    price = 25,000
    inches = 40
    ON = True
    off = False
    def __init__(self, brand):#instance method
        self.brand = brand  #instance variable
    def default_status_tv(self):
         return print(f'{self.brand} is {self.off} and its default channel is {self.channel} and default volume is {self.volume}')
    def tv_on(self):
        print(f' Tv is {self.ON}')
    def increase_volume(self, inc_vol):
        if (inc_vol <= self.volume):
            return f' given volume is {inc_vol}'
        else:
            return " given volume is reached max"
    def decrease_volume(self, dec_vol):
        if dec_vol > 0:
            return f'channel {self.channel} volume is {dec_vol}'
        else:
            return "please increase the volume"
    def set_channel(self, no_channel, current_channel):
        if no_channel > 50:
            return f'you reached maxlimit so, stay in current channel {current_channel}'
        else:
            return no_channel
    def reset_tv(self):
        return f'The {self.brand}tv in defaultchannel no:{self.channel} and its defaultvolume is {self.volume}'

object = Tv("sony")
object.default_status_tv()
print(object.increase_volume(49))
print(object.decrease_volume(9))
print(object.set_channel(60, 5))
print(object.reset_tv())
#part-B
#Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate , functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV

class LED(Tv):
    #in above we inherit base class Tv in child class LED
    #so we can use all properties & method from base class
    def __init__(self, brand, Screen_thickness, Energy_usage, Life_span, Refresh_rate):
        self.screen_thickness = Screen_thickness
        self.energy_usage = Energy_usage
        self.life_span = Life_span
        self.refresh_rate = Refresh_rate
        super().__init__(brand)
    def Display_details(self):
        return f'The {self.brand} is {self.screen_thickness} thickness usage is {self.energy_usage} and warranty {self.life_span} its refresh-rate is {self.refresh_rate}'

obj = LED('ledtv' ,'32inch','70%','10yrs','0.7sec')
print(obj.Display_details())

class Plasmatv(LED):
    #now, we inherit child class to another child class
    # in this we can access or use both base and child class properties
    def __init__(self, brand, Screen_thickness, Energy_usage, Life_span, Refresh_rate):
        super().__init__( brand, Screen_thickness, Energy_usage, Life_span, Refresh_rate)
obj2 = Plasmatv('plasmatv','38inch','80%','15yrs','1min')
print(obj2.Display_details())



