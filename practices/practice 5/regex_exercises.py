# 1)
import re
s = input()
print(bool(re.fullmatch(r"ab*", s)))


# 2)
import re
s = input()
print(bool(re.fullmatch(r"ab{2,3}", s)))


# 3)
import re
s = input()
print(re.findall(r"\b[a-z]+_[a-z]+\b", s))


# 4)
import re
s = input()
print(re.findall(r"\b[A-Z][a-z]+\b", s))


# 5)
import re
s = input()
print(bool(re.fullmatch(r"a.*b", s)))


# 6)
import re
s = input()
print(re.sub(r"[ ,\.]", ":", s))


# 7)
s = input().strip()
parts = s.split("_")
print(parts[0] + "".join(p.capitalize() for p in parts[1:]))


# 8)
import re
s = input()
print(re.split(r"(?=[A-Z])", s))


# 9)
import re
s = input()
print(re.sub(r"(?<!^)(?=[A-Z])", " ", s))


# 10)
import re
s = input().strip()
s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
print(s.lower())