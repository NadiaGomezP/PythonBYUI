import math 

###for average
sum_life_exp_list = [] 

### SELECTED YEAR
min_life_exp = math.inf
min_country = ""
min_code = ""

max_life_exp = 0
max_country = ""
max_code = ""

#FROM ALL THE LIST 
min_overrall_life = math.inf
min_overrall_country = ""
min_overrall_year = 0
min_overrall_code = ""


max_overrall_life = 0
max_overrall_country = ""
max_overrall_year = 0
max_overrall_code = ""



user_year = int(input("\nInsert your year of interest: "))

with open("life-expectancy.csv") as life_expentancy_list:
    life_expentancy_list.readline()
    for line in life_expentancy_list:
        parts = line.split(",")
        years = int(parts[2])
        country = parts[0]
        code = parts [1]
        life_expentancy = float(parts[3])
        if user_year == years:
            sum_life_exp_list.append(life_expentancy)
            total_sum = sum(sum_life_exp_list)
            average = total_sum / len(sum_life_exp_list)
            if life_expentancy < min_life_exp:
                min_life_exp = life_expentancy
                min_country = country
                min_code = code
            elif life_expentancy > max_life_exp:
                max_life_exp = life_expentancy
                max_code = code
                max_country = country
        elif life_expentancy < min_overrall_life:
            min_overrall_life = life_expentancy
            min_overrall_country = country
            min_overrall_year = years
            min_overrall_code = code
        elif life_expentancy > max_overrall_life:
            max_overrall_life = life_expentancy
            max_overrall_country = country
            max_overrall_year = years
            max_overrall_code = code
print(f"\nThe overall max life expectancy is: {max_overrall_life} from {max_overrall_country} ({max_overrall_code}) in {max_overrall_year}")
print(f"The overall min life expectancy is: {min_overrall_life} from {min_overrall_country} ({min_overrall_code}) in {min_overrall_year}")
print(f"\nFor the year {user_year}:\n")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {max_country} ({max_code}) with {max_life_exp:.2f}")
print(f"The min life expectancy was in {min_country} ({min_code}) with {min_life_exp:.2f}\n")



