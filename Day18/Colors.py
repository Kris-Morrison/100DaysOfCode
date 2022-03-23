import colorgram

def color_choice():
    rgb_list = []
    color_list = colorgram.extract("hirst.jpeg", 36)
    # print(len(color_list))
    for number in range(36):
        color = color_list[number]
        rgb_list.append(color.rgb)
        #print(rgb_list)
    return rgb_list


