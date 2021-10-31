start_code = input("Starting station code : ")
start_no = int(input("Starting station no : "))

exit_code = input("Exit station code : ")
exit_no = int(input("Exit station no : "))

if start_code == exit_code:
    travel = abs(start_no - exit_no)
else:
    travel = start_no + exit_no

print(f"You travelled  {travel} station(s).")