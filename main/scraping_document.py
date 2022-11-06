import csv
import re

from thefuzz  import process
import xml.etree.ElementTree as ET



def read_csv(csv_file_name):
    
    with open(csv_file_name, 'r') as file:
        csv_dict_reader = csv.DictReader(file, delimiter=',')
        users_csv_list_dict = list(csv_dict_reader)
    return users_csv_list_dict


def read_xml(xml_file_name):

    with open(xml_file_name, 'r') as file:
        tree = ET.parse(file)
    root = tree.getroot()

    users_xml_list = []
    for user in root.findall('./user/users/user'):
        user_data = user.attrib.copy()
        for field in user:
            user_data[field.tag] = field.text
        users_xml_list.append(user_data)

    return users_xml_list


def remove_empty(data, fields):
    data_without_empty = list(filter(lambda item: not all((not item[field]) for field in fields),data))
    return data_without_empty


def clean_data(data, fields):
    data = remove_empty(data, fields)

    for item in data:
        for field in fields:
            if not item[field]:
                data.remove(item)
                break
            else:
                item[field] = re.sub('\(.*\)', "", item[field])
                item[field] = re.sub('\[.*\]', "", item[field])
    return data

def connect_names(csv_users, xml_users):
 
    names = []
    for xml_user in xml_users:
        name = str(xml_user['first_name'] or '') + str(xml_user['last_name'] or '')
        names.append(name)

    list_name = []
    for csv_user in csv_users:
        username = csv_user['username'].replace('.', ' ')

        highest = process.extractOne(username, names)

        if highest[1] > 70:
            xml_record = xml_users[names.index(highest[0])]
            names[names.index(highest[0])] = ''
            list_name.append({**csv_user, **xml_record})
    return list_name


def tru_users_data(csv_file_name, xml_file_name):
    users_from_csv = read_csv(csv_file_name)
    users_from_xml = read_xml(xml_file_name)

    users_from_csv_clean = clean_data(users_from_csv, ['username'])
    users_from_xml_clean = clean_data(users_from_xml, ['first_name', 'last_name'])

    connect_name = connect_names(users_from_csv_clean, users_from_xml_clean)
    return connect_name
print(tru_users_data('test_file/test_task.csv', 'test_file/test_task.xml'))
