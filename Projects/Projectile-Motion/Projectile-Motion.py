# Weapon variables
weapon = "SV-98"
calibre = "7.62x54mmR"
ammoType = "BS"
projectileSpeed = 785.0
# Building variables
building = "Willis Tower"
height = 526.99
# Separate variables
gravity = 9.81

time = (((2.0*height)/gravity) ** 0.5) # Formula for time
print(f"The amount of time it travels for is "+ time +" seconds")

distance = (projectileSpeed*time) # Formula for distance
print(f"The distance it travels is " + distance + "meters")

# | This code looks to calculate how far a "BS" bullet shot from an SV-98 while on-top of the Willis Tower travels. The projectile speed
# | of the bullet is 785 m/s while the height of the building is 526.99m. To find the distance the bullet travels we need to find time
# | it travels the formula needed to use to find this is (((2*height)/gravity) ** 0.5) after finding the time it travels for we can 
# | find the distance by using this formula (speed*time).

