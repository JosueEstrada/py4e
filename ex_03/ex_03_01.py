# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate:")
r = float(rate)

if h <= 40:
    print(h * r)
else:
    extra = h - 40
    print(40 * r + extra * r * 1.5)

# Video con otra solucion que multiplica por 0.5 https://www.youtube.com/watch?v=crLerB4ZxMI50