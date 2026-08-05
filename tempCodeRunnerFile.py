# Corporate State Initialization
employees = [
    {"name": "Rohan", "base": 50000, "overtime": 10, "attendance": "Excellent"},
    {"name": "Sita", "base": 40000, "overtime": 5, "attendance": "Low"},
    {"name": "John", "base": 60000, "overtime": 4, "attendance": "Good"}
]

total_company_expense = 0
print("--- Initialising Payroll Processor ---")

# Processing Loop
for emp in employees:
    current_pay = emp["base"]
    print(f"\nProcessing payroll for: {emp['name']}")
    print(f"  Initial base salary entry: INR {current_pay}")
    
    # Rule 1: Penalty assessment for low attendance records
    if emp["attendance"] == "Low":
        penalty = emp["base"] * 0.10
        current_pay -= penalty  # 10% Deduction applied
        total_company_expense += current_pay
        print(f"  [ATTENTION] Low Attendance! Applied 10% fine (INR {penalty}).")
        print(f"  [STATUS] Final Payout computed: INR {current_pay}. Overtime processing skipped.")
        continue  # Move directly to the next employee profile
        
    # Rule 2: Budget protection checkpoint for corporate bonuses
    if total_company_expense > 50000:
        total_company_expense += current_pay  # Append baseline salary structure only
        print(f"  [RESTRICTION] Corporate expense budget threshold breached (> INR 50,000).")
        print(f"  [STATUS] Final Payout computed: INR {current_pay}. Overtime allowance denied.")
        continue  # Skip calculation of any supplementary benefits
        
    # Rule 3: Execution of premium overtime payout metrics
    overtime_bonus = emp["overtime"] * 500
    current_pay += overtime_bonus
    total_company_expense += current_pay
    print(f"  [BONUS] Standard Attendance verified. Overtime allowance added: INR {overtime_bonus}.")
    print(f"  [STATUS] Final Payout computed: INR {current_pay}.")

print("\n--- Payroll Compilation Finalised ---")
print(f"Total Combined Budget Disbursed by Corporate: INR {total_company_expense}")
