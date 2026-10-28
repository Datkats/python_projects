print("Ocean’s level is currently rising at about 1.6 millimeters per year")
per_year_mm=1.6
per_year_in=0.062992126
print("Table shows below for the next 25 years")
print("___"*10)
print(f"{"year":<8}level(mm){"(in)":>9}")
for n in range(1,26):# displaying ocean level in milimeters and in inches for the next 25 years
    print(f"{n:<12} {per_year_mm*n:.1f}{per_year_in*n:>11.3f}")
print(f"In 25 years, the ocean will have risen by {per_year_mm*n:.1f}millimeters or {per_year_in*n:.3f}inches")
