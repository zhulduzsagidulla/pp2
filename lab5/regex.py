import re
# ex1
x1 = re.match("a*b", "abbb")
print(x1)
# ex2
x2 = re.match("ab{2}|b{3}", "abbb")
print(x2)
# ex3
print(re.findall(".+_+.+", "sagidulla_zhuldyz"))
# ex4
print(re.findall("[A-Z]{1}[a-z]+", "Zhuldyz"))
# ex5
print(re.match("^a.*b$", "afdsfb"))
# ex6
txt = "a r,.n"
txt = txt.replace(".", ":").replace(",", ":").replace(" ", ":")
print(txt)
# ex7
txt = "sagidulla zhuldyz"
txt = txt.title().replace("_", "")
print(txt)
# ex8
txt = "lolKeEeK"
print(re.split("[A-Z]", txt))
# ex9
txt = "zhUlUz"
print(re.sub(r"(\w)([A-Z])", r"\1 \2", txt))
# ex10
txt = "zhuldyzSagidulla"
string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt).lower()
print(string)