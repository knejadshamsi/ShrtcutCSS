def size_inter(class_name, prop, class_dict):
    dimensions_split = {'width':[prop.split('-')[0], 'vw'], 'height': [prop.split('-')[1],'vh']}
    dimensions = {'width': '', 'height': ''}
    for dem_name, dem in dimensions_split.items():
        if dem[0].isdigit(): dem = int(dem)
        match dem[0]:
            case 'full':    dimensions[dem_name] = "100" + dem[1]
            case 'half':    dimensions[dem_name] = "50" + dem[1]
            case 'quarter': dimensions[dem_name] = "25" + dem[1]
            case 'fill':    dimensions[dem_name] = "100%"
            case 'half%':   dimensions[dem_name] = "50%"
            case 'quarter%':dimensions[dem_name] = "25%"
            case int(): dimensions[dem_name] = dem[0] + "rem"
            case _: dimensions[dem_name] = dem[0]

    if class_name in class_dict and len(class_dict[class_name]) > 0:
        class_dict[class_name].update(dimensions)
    else:
        class_dict[class_name] = dimensions

    return class_dict


def color_inter(class_name, prop, class_dict):
    colors = {'background': prop.split('-')[0], 'color': prop.split('-')[1]}
    color_palette = {}
    for colors_place,colors_prep in colors.items():
        color = colors_prep.split('.')
        #if type(color) == "list":



def position_inter(class_name, prop, class_dict):
    return "hi"
