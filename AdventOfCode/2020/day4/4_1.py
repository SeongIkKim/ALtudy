with open('inputs.txt') as f:
    passports = f.read().strip().split('\n\n')

example = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

passport_datum = []
count = 0

for passport in passports:
    passport = passport.replace('\n', ' ')

    personal_data = dict()
    fields = passport.split(' ')
    for field in fields:
        key, value = field.split(':')
        personal_data[key] = value

    if example.issubset(set(personal_data.keys())):
        count+=1

    passport_datum.append(personal_data)

print(count)
