def get_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Collecting user inputs safely
age = get_input("Enter your age (1-100): ", 1, 100)
bmi = get_input("Enter your BMI (20-40): ", 20, 40)
systolic_bp = get_input("Enter your systolic blood pressure (70-200): ", 70, 200)
diastolic_bp = get_input("Enter your diastolic blood pressure (50-150): ", 50, 150)
cholesterol = get_input("Enter your cholesterol level (150-300): ", 150, 300)
glucose = get_input("Enter your glucose level (50-500): ", 50, 500)
