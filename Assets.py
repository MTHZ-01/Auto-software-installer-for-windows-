
import pickle
# Universally Consistent
def is_portable(link: str) -> bool:
    return "portable" in link.replace(" ", "").lower()


# Universally Consistent
def is_for_windows(link: str) -> bool:
    link = link.split('?')[0]
    return link.endswith('.exe') or link.endswith('.zip') or link.endswith('rar')


# Universally Consistent
def Bits(link: str) -> str:
    link = link.lower().replace(' ', '')
    if 'x64' in link or '64bit' in link or '64bits' in link:
        return 'X64'
    elif 'x32' in link or '32bit' in link or '32bits' in link:
        return 'X32'
    elif 'x86' in link or '86bit' in link or '86bits' in link:
        return 'X32'
    else:
        return ''


# Universally Consistent
def Version(link: str) -> str:
    return app_name(link) + ' + '+Bits(link) + ' ' + app_version(link)


def common_procedure(Context, query, anchor_tags: list):
    anchor_tags = list(filter(lambda x: x.get_attribute('href') != '', anchor_tags))
    anchor_tags = list(filter(lambda x: x.get_attribute('href') is not None, anchor_tags))
    anchor_tags = list(filter(lambda x: is_for_windows(x.get_attribute('href')), anchor_tags))
    anchor_tags = list(filter(lambda x: not (is_portable(x.get_attribute('href'))), anchor_tags))

    download_link_hrefs = list(map(lambda x: [x.get_attribute('href'),query,Context+".com"], anchor_tags))
    download_link_texts = list(map(lambda x: Version(x.get_attribute('href')), anchor_tags))
    download_link_dict = dict(zip(download_link_texts, download_link_hrefs))
    if len(download_link_dict.keys()) > 0:
        try:
            old_records = pickle.load(open(Context + '.bin', 'br'))
            old_records.update(download_link_dict)
            pickle.dump(old_records,open(Context + '.bin', 'bw'))
        except:
            pickle.dump(download_link_dict,open(Context + '.bin', 'bw'))

    return download_link_dict


# Universally Consistent
def app_name(link: str) -> str:
    link = link.split('/')[-1]
    name = ''
    for char in link:
        if 48 <= ord(char) <= 57:
            break
        name += char
    return name.strip('.').replace('.', '').replace('-', '').replace('_', '')


# Universally Consistent
def app_version(link: str) -> str:
    link = link.split('/')[-1]
    version = ''
    number_met = False
    for char in link:
        if 48 <= ord(char) <= 57 or (char == '.' and number_met):
            version += char
            number_met = True
        elif number_met and not char == '.':
            break

    return version.strip('.')

def add_to_dict(Context:str, newDict:dict):
    file = open(Context+'.bin', 'br')
    oldDict = pickle.load(file)
    oldDict.update(newDict)
    file.close()
    file = open(Context+'.bin', 'bw')
    pickle.dump(oldDict)
    file.close()

def record_search(records:dict, query:str) -> dict:
    corresponding_dictionary = dict()
    for record in records.keys():
        if query.replace(' ', '').upper() in record.replace(' ', '').upper():
            corresponding_dictionary[record] = records[record]
    return corresponding_dictionary




