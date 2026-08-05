# Problem Description: # 
# Employee Corporate Payroll TrackerThis system manages and computes the monthly payroll for a corporate company using a  
#dataset of employee profiles. The program processes each employee's compensation sequentially based on three core business rules:


# (1)Attendance Penalty Rule: If an employee’s attendance status is classified as "Low", they are penalized for absenteeism. 
# The system applies a 10% deduction fine to their baseline salary (base), forfeits their eligibility for overtime 
# pay, and immediately skips to the next employee profile using a continue statement.

# (2) Budget Safeguard Rule: The company operates under a strict operational threshold.
# If the running cumulative company expenses (total_company_expense) cross INR 50,000, a budget restriction automatically triggers. 
# Any employee evaluated after this limit is breached is denied their overtime allowance and is only credited their standard base pay.


# 3 ) Overtime Allocation Rule: For employees with clean attendance tracking records ("Good" or "Excellent"),
# and as long as the budget cap has not been breached prior to their evaluation, the system calculates an overtime premium.
# They are compensated at a premium rate of INR 500 per overtime hour, which is added directly to their final monthly payout.


# The primary objective of this programming logic is to track how conditional loop control statements (continue) and mutating 
# state flags alter individual payouts depending strictly on their chronological order inside the data collection array.



employees = [
    {"name": "Rohan", "base": 50000, "overtime": 10, "attendance": "Excellent"},
    {"name": "Sita", "base": 40000, "overtime": 5, "attendance": "Low"},
    {"name": "John", "base": 60000, "overtime": 4, "attendance": "Good"}
]

total_company_expense = 0
print("--- Initialising Payroll Processor ---")


for emp in employees:
    current_pay = emp["base"]
    print(f"\nProcessing payroll for: {emp['name']}")
    print(f"  Initial base salary entry: INR {current_pay}")
    

    if emp["attendance"] == "Low":
        penalty = emp["base"] * 0.10
        current_pay -= penalty 
        total_company_expense += current_pay
        print(f"  [ATTENTION] Low Attendance! Applied 10% fine (INR {penalty}).")
        print(f"  [STATUS] Final Payout computed: INR {current_pay}. Overtime processing skipped.")
        continue  
        
   
    if total_company_expense > 50000:
        total_company_expense += current_pay 
        print(f"  [RESTRICTION] Corporate expense budget threshold breached (> INR 50,000).")
        print(f"  [STATUS] Final Payout computed: INR {current_pay}. Overtime allowance denied.")
        continue
        
  
    overtime_bonus = emp["overtime"] * 500
    current_pay += overtime_bonus
    total_company_expense += current_pay
    print(f"  [BONUS] Standard Attendance verified. Overtime allowance added: INR {overtime_bonus}.")
    print(f"  [STATUS] Final Payout computed: INR {current_pay}.")

print("\n--- Payroll Compilation Finalised ---")
print(f"Total Combined Budget Disbursed by Corporate: INR {total_company_expense}")
