import yaml


# 解析data目录下的数据
def base_yml_with_file(file_name, key):
    with open("./data/" + file_name + ".yml", "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[key]
        case_data_list = []
        for case_data in data.values():
            case_data_list.append(case_data)
        return case_data_list


