# 1. Unit Conversions
# Pounds to Kilograms (1 lb = 0.453592 kg)
pounds = 180.5
kilograms = pounds * 0.45359237
# Miles to Kilometers (1 mi = 1.60934 km)
miles = 12.5
kilometers = miles * 1.609344
# Fahrenheit to Celsius (°C = (°F - 32) * 5 / 9)
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9
# 3. Average Age of 10 Students
student_ages = [18, 20, 19, 21, 22, 18, 19, 20, 23, 19]
average_age = sum(student_ages) / len(student_ages)
# Output - Part 1: First Fantasy Story
story_one=
        ("CHAPTER I: THE CALL TO ADVENTURE\n"
+ "Deep within the Whispering Woods, " + hero_name + " grasped the hilt of the legendary
" + weapon_name + "
+ "Alongside " + companion_name + ", they prepared to traverse the shadowed lands.\n"
+ "Before stepping into the portal, " + hero_name + " consumed a single drop of the " +
item_name + ",\n"
+ "feeling a rush of power as they readied their signature ability, " + ability_name + "."
)

print(story_one)

# Output - Part 2: Unit Conversions
print("UNIT CONVERSIONS")
print(f"Weight: {pounds} lbs = {kilograms:.2f} kg")
print(f"Distance: {miles} mi = {kilometers:.2f} km")
print(f"Temperature: {fahrenheit}°F = {celsius:.2f}°C")
print()
# Output - Part 3: Student Ages & Average
print("STUDENT AGE CALCULATOR")
print("Ages of the 10 students:", ", ".join(map(str, student_ages)))
print(f"Average Age: {average_age:.1f} years old")
print()
# Output - Part 4: Second Fantasy Story

print(story_two)
"CHAPTER II: THE BATTLE AT THE CITADEL\n"
+ "The Citadel walls crumbled as " + companion_name + " drew back her bowstring.\n"
+ hero_name + " charged forward, wielding the gleaming " + weapon_name + " against the
darkness.\n"
+ "Cornered by the shadow guards, " + hero_name + " uncorked the emergency " +
item_name + " to restore strength\n"
+ "before unleashing a devastating " + ability_name + " that shattered the enemy forces!"

print(story_three)
# Output - Part 5: Summary & Quest Log
story_three 
"CHAPTER III: THE QUEST LOG & JOURNEY SUMMARY\n"
+ hero_name + " and " + companion_name + " stood victorious amidst the quiet ruin.\n"
+ "With the " + weapon_name + " sheathed and the last vial of " + item_name + "
emptied,\
+ "they looked toward the horizon, ready for whatever shadows remained.\n"
+ "Their legends would echo forever, born from the fire of the " + ability_name + "."
