def calculate_risk(metrics):
    """
    Calculates health risk based on input metrics.
    Thresholds: Blood Pressure > 140, Cholesterol > 200, BMI > 25
    """
    risk_count = 0
    thresholds = [140, 200, 25] # BP, Cholesterol, BMI
    metric_names = ["Blood Pressure", "Cholesterol", "BMI"]
    
    print("--- Starting Health Risk Assessment ---")
    
    # Task 1-c Logic: Loop through metrics and check against thresholds
    for i in range(len(metrics)):
        if metrics[i] > thresholds[i]:
            print(f"Alert: {metric_names[i]} ({metrics[i]}) is above threshold ({thresholds[i]})")
            risk_count += 1
        else:
            print(f"Normal: {metric_names[i]} ({metrics[i]}) is within safe limits.")
            
    # Task 1-c Logic: If-Else statement for final warning
    if risk_count >= 2:
        return "RESULT: High Risk Warning - Please consult a doctor."
    else:
        return "RESULT: Normal Status - Continue healthy habits."

# Test Data for Task 1-d (TC-HEALTH-01)
# Inputs: BP=150 (High), Cholesterol=240 (High), BMI=22 (Normal)
test_user_data = [150, 240, 22]

# Execution
final_result = calculate_risk(test_user_data)
print("\n" + final_result)

# Note for Task 3-a: 
# Total Lines of Code (LOC) for logic ~15 lines.
# If you find a bug (e.g. threshold is too low), that is a 'Confirmed Defect'.
