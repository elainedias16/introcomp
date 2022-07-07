age_a = int(input("Idade de Ana:\n"))
age_e = int(input("Idade de Eduarda:\n"))

age_b = age_a + 4
age_c = (age_a + age_e) / 2
age_d = (2 * age_e) / 3


print(age_a == age_c)
print(age_a  > age_e)
print(age_d == age_b)
print( (age_b or age_e) > age_d)
print( (age_a and age_b) > age_e )


