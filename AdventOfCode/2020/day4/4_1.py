import re


def is_exact_digit(num_str:str, digit:int) -> bool :
    return True if len(num_str) == digit else False

def is_matched_range(num_str:str, start:int, end:int) -> bool:
    return True if start <= int(num_str) <= end else False


#### validation ####
def is_byr_valid(byr:str) -> bool :
    return True if is_matched_range(byr,1920,2002) else False

def is_iyr_valid(iyr:str) -> bool :
    return True if is_matched_range(iyr,2010,2020) else False

def is_eyr_valid(eyr:str) -> bool:
    return True if is_matched_range(eyr,2020,2030) else False

def is_hgt_valid(hgt:str) -> bool:
    if hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193 :
        return True
    elif hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76:
        return True
    return False

def is_hcl_valid(hcl:str) -> bool:
    return True if re.fullmatch('^#[0-9a-f]{6}$', hcl) else False

def is_ecl_valid(ecl:str) -> bool:
    sample = ('amb','blu','brn','gry','grn','hzl','oth')
    return True if ecl in sample else False

def is_pid_valid(pid:str) -> bool:
    if pid.isdigit() and is_exact_digit(pid,9) and f"{int(pid):09d}" != pid:
        return True
    return False

def is_all_valid(d:dict) -> bool:
    if not(is_byr_valid(d['byr'])):
        # print('byr')
        return False
    if not(is_iyr_valid(d['iyr'])):
        # print('iyr')
        return False
    if not(is_eyr_valid(d['eyr'])):
        # print('eyr')
        return False
    if not(is_hgt_valid(d['hgt'])):
        # print('hgt')
        return False
    if not(is_hcl_valid(d['hcl'])):
        # print('hcl')
        return False
    if not(is_ecl_valid(d['ecl'])):
        # print('ecl')
        return False
    if not(is_pid_valid(d['pid'])):
        # print('pid')
        return False
    return True
########

with open('inputs.txt') as f:
    passports = f.read().strip().split('\n\n')

example = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

count = 0

datum = []

for passport in passports:

    p = passport.replace('\n', ' ')
    personal_data = dict()

    fields = p.split(' ')
    for field in fields:
        key, value = field.split(':')
        personal_data[key] = value

    datum.append(personal_data)

    if not(set(personal_data.keys()).issuperset(example)):
        continue

    if is_all_valid(personal_data):
        count+=1

print(count)



