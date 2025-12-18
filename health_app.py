def calculate_risk(metrics):
    """
    MODIFIED VERSION: Branch-Logic-Mod
    This version changes the risk threshold logic.
    """
    risk_count = 0
    thresholds = [140, 200, 25] 
    metric_names = ["Blood Pressure", "Cholesterol", "BMI"]
    
    print("--- Starting Health Risk Assessment (Logic Mod) ---")
    
    for i in range(len(metrics)):
        if metrics[i] > thresholds[i]:
            risk_count += 1
            
    # MODIFICATION: Changed logic from '>= 2' to '> 2'
    # Now it requires ALL THREE metrics to be high to trigger the warning.
    if risk_count > 2: 
        return "RESULT: High Risk Warning"
    else:
        return "RESULT: Normal Status"

test_user_data = [150, 240, 22]
print("\n" + calculate_risk(test_user_data))
