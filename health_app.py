def calculate_risk(metrics):
    """
    MODIFIED VERSION: Branch-Loop-Mod
    This version only checks the first TWO metrics.
    """
    risk_count = 0
    thresholds = [140, 200, 25] 
    metric_names = ["Blood Pressure", "Cholesterol", "BMI"]
    
    print("--- Starting Health Risk Assessment (Loop Mod) ---")
    
    # MODIFICATION: Changed range to only check first 2 metrics (index 0 and 1)
    for i in range(0, 2): 
        if metrics[i] > thresholds[i]:
            print(f"Alert: {metric_names[i]} ({metrics[i]}) is above threshold")
            risk_count += 1
            
    if risk_count >= 2:
        return "RESULT: High Risk Warning"
    else:
        return "RESULT: Normal Status"

test_user_data = [150, 240, 22]
print("\n" + calculate_risk(test_user_data))
