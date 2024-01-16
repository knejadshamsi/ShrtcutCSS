from bs4 import BeautifulSoup
import codecs

# option = BeautifulSoup(open("test.html"), "html5lib").option

# print(option.encode(formatter="html5"))

soup = BeautifulSoup(open("test.html"), "html5lib")
el = soup.find("div").encode(formatter="html5")
# print(el)


html_list_splited = str(open("test.html").read()).replace(">", "> \n").split('\n')
html_list_cleaned = [el.strip() for el in html_list_splited if len(el) > 0]
html_list_limited = html_list_cleaned[html_list_cleaned.index("<body>") + 1:html_list_cleaned.index("</body>")]
html_list = [el for el in html_list_limited if el[0:2] != "</"]

print(html_list)
for el in html_list:
    new_el = el.replace(" ", ' class="test" ', 1)
    print(new_el)

print(html_list)

# should be done for each item only

html_el = [el.replace("<", "").replace(">", "").split() for el in html_list]

if "scc" in html_el[0]: print("true")
else: print("false")
if "class" in html_el[0]: print("true")
else: print("false")

test_dict = {'#test': {'width': '100%', 'color': 'black'}, '#other': {'width': '90%', 'color': 'white'}}

if "#other2" in test_dict and len(test_dict["#other"]) > 0:
        test_dict["#other2"].update({"hey":"hi","wow": "nice"})
else:
        test_dict["#other2"] = {"hey": "hi", "wow": "nice"}

print(test_dict)


test_data = date.replace(" ","").replace("\n","").replace("\t","").replace("{", " x;"). replace("}", " ").split()
for i in range(1,len(test_data),2):
    test_data[i] = test_data[i].replace(";"," ").split()
    if len(test_data[i]) > 1:
        del test_data[i][0]
    else:
        test_data[i][0] = " "


test3 = "wefwef\n"
test3.remove("\n")
print("test3",test3)

