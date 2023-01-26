def css_safety(css):
    removed_lines = css.replace("\n", "")
    if "{" in removed_lines and "}" in removed_lines:
        mod_braces = removed_lines.replace(" ", "").replace("\t", "").replace("{", " { ").replace("}", " } ").split()
        list_index_open = [e for e, x in enumerate(mod_braces) if x == "{"]
        list_index_close = [e for e, x in enumerate(mod_braces) if x == "}"]
        #if there is { and } in the file
        if removed_lines.count("{") == removed_lines.count("}"):
            #if the number of { is equal to }
            for i in range(0, len(list_index_open)):
                if len(mod_braces[list_index_open[i] + 1:list_index_close[i]]) == 0:
                    mod_braces.insert(list_index_open[i] + 1, "X:Y;")
            new_css = ""
            for el in mod_braces:
                if el[0] in ["#", ".", "@"]:
                    new_css = new_css + el + " "
                elif el in ["{", "}"]:
                    new_css = new_css + el.replace("\t", "") + "\n"
                else:
                    for p in el.replace(";", " ").split():
                        new_css = new_css + "\t" + p + ";\n"
            return new_css

        else:
            new_css = ""
            if len(list_index_open) > len(list_index_close):
                # there id no equal number of { and }
                css_check = css.split("{")
                for el in css_check:
                    if "}" in el: new_css = new_css + el
                return new_css

            else:
                css_check = css.split("}")
                for el in css_check:
                    if "{" in el: new_css = new_css + el
                return new_css

    else:
        css_list = css.replace("\t", "").replace(" ", "").strip().split("\n")
        css_list = [el for el in css_list if len(el) > 0]
        print(css_list)
        head_index = []
        for i in range(0, len(css_list)):
            if css_list[i][0] == "." or css_list[i][0] == "#":
                head_index.append(i)
        if len(head_index) > 0:
            new_css = ""
            for i in range(0, len(head_index)):
                new_content = ""
                if head_index[i] != head_index[-1]:
                    for el in css_list[head_index[i] + 1:head_index[i + 1]]:
                        new_content = new_content + "\t" + el + "\n"
                else:
                    for el in css_list[head_index[i] + 1:]:
                        new_content = new_content + "\t" + el + "\n"
                new_css = new_css + css_list[head_index[i]] + " {\n" + new_content + "}\n"
            return new_css
        else:
            # if there is no { or } or . or #
            return "{X:Y;}"