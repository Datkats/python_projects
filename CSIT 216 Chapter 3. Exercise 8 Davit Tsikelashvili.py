import math
hot_dog_package=10
hot_dog_bun_package=8
people_amount=int(input("Enter the number of people attending the cookout: "))
hotdog_per_person=(int(input("Enter the number of hot dogs each person will be given: ")))
totalHotDogs=people_amount*hotdog_per_person # calculating the total amount of hot dogs we need
hot_dog_package_need=math.ceil(totalHotDogs/hot_dog_package) # calculating the total amount of hot dog's package we need and round up(in case if total package was 4,2 we will need only one package)
hot_dog_bun_package_need=math.ceil(totalHotDogs/hot_dog_bun_package)# calculating the total amount of hot dog's bun package we need and round up(in case if total package was 4,2 we will need only one package)
leftOver_hotdog=(hot_dog_package*hot_dog_package_need) - totalHotDogs# calculating left overs by subtracting total hot dogs from the full amount of hot dogs
leftOver_hotdog_bun=(hot_dog_bun_package*hot_dog_bun_package_need) - totalHotDogs# calculating left overs by subtracting total hot dog buns from the full amount of hot dog buns
print(f"number of hot dog package need: {hot_dog_package_need}")
print(f"number_of_hot_dog_bun_package_need: {hot_dog_bun_package_need}")
print(f"left over hotdog: {leftOver_hotdog}")
print(f"left over hotdog bun: {leftOver_hotdog_bun}")
