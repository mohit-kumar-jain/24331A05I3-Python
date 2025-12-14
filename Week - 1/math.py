
import math

pie= math.pi
print(f"The value of pi is: ",pie)
num = 16
sqrt= math.sqrt(num)
print(f"The square root of {num} is: {sqrt}")

angle = 60
angle = math.radians(angle)

cos = math.cos(angle)
sin = math.sin(angle)

print(f"For an angle of {angle} degrees ({angle:.4f} radians):")
print(f"  Cosine value: {cos:.4f}")
print(f"  Sine value: {sin:.4f}")

angledegrees = 90
angleradian = math.radians(angledegrees)

cos2 = math.cos(angleradian)
sin2 = math.sin(angleradian)
print(f"For an angle of {angledegrees} degrees ({angleradian:.4f} radians):")
print(f"  Cosine value: {cos2:.4f}")
print(f"  Sine value: {sin2:.4f}")