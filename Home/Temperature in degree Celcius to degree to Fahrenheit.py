# Temperature in degree Celcius to degree Fahrenheit

bp_c = 100  # boiling point of water
fp_c = 0  # freezing point of water
degree = u'\N{Degree Sign}'  # it is the literal for degree sign

# Fahrenheit = ( Celcius*9/5 )+32

bp_f = (bp_c*9/5)+32  # bp_f : boiling point in fahrenheit
fp_f = (fp_c*9/5)+32  # fp_f : freezing point in fahrenheit

print("Bolling point in ", degree + "C : ",
      bp_c, "and in ", degree+"F : ", bp_f)
print("Freezing point in ", degree + "F : ",
      fp_f, "and in ", degree + "F : ", fp_f)