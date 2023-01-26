import random
from prop_inter import *
from safety import *


def random_class_name(eltype, genmode):
    if genmode == "123":
        return str(eltype + "-" + str(random.randint(1, 100000)))
    elif genmode == "xyz":
        random_class = eltype + "-"
        for _ in range(8):
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            random_class += (chr(random_integer))
        return random_class


def class_handler(file, el_name, element, genmode):
    with open(file, "r") as file:
        html_file = file.read()
        new_class = random_class_name(el_name, genmode)
        new_element = element.replace(" ", f' class="{new_class}" ', 1)
        html_file = html_file.replace(element, new_element, 1)

    with open(file.name, "w") as file:
        file.write(html_file)


def html_parser(file, genmode):
    html_list_splited = str(open(file).read()).replace(">", "> \n").split('\n')
    html_list_cleaned = [el.strip() for el in html_list_splited if len(el) > 0]
    html_list_limited = html_list_cleaned[html_list_cleaned.index("<body>") + 1:html_list_cleaned.index("</body>")]
    html_list = [el for el in html_list_limited if el[0:2] != "</"]
    for el in html_list:
        el_list = el.replace("<", "").replace(">", "").replace("=", " ").split()
        if ("scc" in el_list) and ("class" not in el_list):
            class_handler(file,el_list[0], el, genmode)


# returns a dict made from a css file
#BUG NOTE: If the properties are emptied , it will throw an error
def css_parser(file):
    with open(file) as file:
        css = file.read()
    css_txt = css_safety(css)
    parsed_list = str(css_txt).replace("\n", "").replace("\t", "").replace(" ", "").replace("{", " ").replace("}", " ").split()
    for i in range(1, len(parsed_list), 2):
        if len(parsed_list[i]) > 0: parsed_list[i] = parsed_list[i].replace(":", " ").replace(";", " ").split();
        else: parsed_list[i] = " "
        print("parsed list is ",parsed_list)
    css_dict = {
        parsed_list[y]: {parsed_list[y + 1][z]: parsed_list[y + 1][z + 1] for z in range(0, len(parsed_list[y + 1]), 2)} for y in range(0, len(parsed_list), 2)}
    if css_dict["X"]: del css_dict["X"]
    return css_dict


# ***** doing the scc stuff
def scc_interpreter(file, css_dict):
    html_list_splited = str(open(file).read()).replace(">", "> \n").split('\n')
    html_list_cleaned = [el.strip() for el in html_list_splited if len(el) > 0]
    html_list_limited = html_list_cleaned[html_list_cleaned.index("<body>") + 1:html_list_cleaned.index("</body>")]
    html_list = [el.replace("<", "").replace(">", "").replace("=", " ").split() for el in html_list_limited if el[0:2] != "</"]
    for scc_element in html_list:
        if "scc" in scc_element:
            el_list = scc_element[scc_element.index("class")+1:]
            el_class_name = el_list[0].replace('"', ".", 1).replace('"',"")
            el_props = el_list[el_list.index("scc")+1:]
            i = 0
            for order in el_props[0]:
                i = i + 1
                if i < len(el_props):
                    match order:
                        case "S": size_inter(el_class_name, el_props[i], css_dict)
                        case "C": color_inter(el_class_name, el_props[i], css_dict)
                        case "P": position_inter(el_class_name, el_props[i], css_dict)
                else:
                    break
    return css_dict


def dict_to_css(css_dict):
    style = ""
    for selector in css_dict:
        properties = str(css_dict.get(selector)).replace("'", "").replace(", ", ";\n \t").replace("{", "").replace("}", "")
        style = style + "\n" + selector + " { \n \t" + properties + ";\n }"

    return style