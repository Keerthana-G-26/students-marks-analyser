marks = float(input("Enter marks:"))
stars = 5 if marks>=90 else 4 if marks>=80 else 3 if marks>=70 else 2 if marks>=60 else 1 if marks>=50 else 0

print(f"Stars:{'*'*stars} ({stars}/5)")