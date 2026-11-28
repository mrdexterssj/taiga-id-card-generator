import re

testing_str = "TG-12-123456-1234"
test = re.findall(r'\d+', testing_str)

print(test)
final_str = ""

for i in test:
    print(i)
    final_str += i

print (final_str)
