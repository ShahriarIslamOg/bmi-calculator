def calculate_bmi(weight, height):
    try:
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        bmi = weight / (height ** 2)
        return bmi
    except ValueError as e:
        return str(e)

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    result = calculate_bmi(weight, height)
    
    if isinstance(result, float):
        print(f"Your BMI is: {result:.2f}")

        if result < 18.5:
            print("BMI Status: Underweight")
            print("Recommendation: Consider gaining weight with a balanced diet and exercise.")

        elif 18.5 <= result < 25:
            print("BMI Status: Normal (Healthy Weight)")
            print("Recommendation: Maintain a balanced diet and regular exercise.")

        elif 25 <= result < 30:
            print("BMI Status: Overweight")
            print("Recommendation: Focus on a healthy diet and increase physical activity.")

        else:
            print("BMI Status: Obese")
            print("Recommendation: Consult with a healthcare professional for personalized advice.")

    else:
        print(f"Error: {result}")

except ValueError:
    print("Error: Please enter valid numerical values for weight and height.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

print("\nAuthor: Shahriar Islam")
