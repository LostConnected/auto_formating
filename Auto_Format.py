###########################################
#   修改以下内容以更改输出内容。
companies = ["A", "B", "C", "D", "E"]
states = [None, "OH", None, "oh", None]  
cities = [None, 1, None, 2, None]  
years = [2000, 2001, 2002, 2003, 2004]
num_employees = [100, 101, 102, 103, 104]
###########################################

def auto_format(companies, states, cities, years, num_employees, output_file=None):
    lines = []  # Store lines for file output

    for i in range(len(companies)):
        company_name = companies[i][:20]  
        state = states[i]                 
        city = str(cities[i]) if cities[i] is not None else "N/A"  
        year = str(years[i])              
        employees = str(num_employees[i]) 

        if state is None:
            output_line = f"{company_name:<20}          {year:<4}" 
        else:
            output_line = f"{company_name:<20}    {state:<2}   {city:<6} {year:<4}"
        
        employees_line = f"Employees: {employees}"
        
        print(output_line)  # Print to console
        print(employees_line)
        print()

        lines.append(output_line)
        lines.append(employees_line)
        lines.append("")  

    if output_file:
        with open(output_file, 'w') as file:
            for line in lines:
                file.write(line + '\n')  

auto_format(companies, states, cities, years, num_employees, "data-inc.txt")
