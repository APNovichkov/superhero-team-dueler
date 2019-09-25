import dog

my_dog = dog.Dog("Alex", "Chiwawa")
print("Dogs name: {}".format(my_dog.name))
print("Dogs breed: {}".format(my_dog.breed))
my_dog.bark()

my_other_dog = dog.Dog("Annie", "SuperDog")
print("Dogs name: {}".format(my_other_dog.name))
print("Dogs breed: {}".format(my_other_dog.breed))
my_other_dog.bark()
