# Exercise 3: Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for
# input.
import sys

str_nota = input("Ingresa nota: ")
try:
    nota = float(str_nota)
    # if nota >= 0.0 and nota >= 1.0: expression imposible
    if nota < 0.0 or nota > 1.0:
        print("nota para procesar....")
    elif nota >= 0.9:
        print("A")
    elif nota >= 0.8:
        print("B")
    elif nota >= 0.7:
        print("C")
    elif nota >= 0.6:
        print("D")
    elif nota < 0.6:
        print("F")
except:
    sys.exit("Nota incorrecta")

# Alternativa utilizando mejor el try-except
# score_str = input("Enter score: ")
#
# try:
#     score = float(score_str)
# except:
#     print("Bad score")
#     quit()
#
# if score < 0.0 or score > 1.0:
#     print("Bad score")
# elif score >= 0.9:
#     print("A")
# elif score >= 0.8:
#     print("B")
# elif score >= 0.7:
#     print("C")
# elif score >= 0.6:
#     print("D")
# else:
#     print("F")
