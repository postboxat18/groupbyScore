from rapidfuzz import fuzz

all_data = [{"Notes": "Chest Pain", "page_num": 1},
            {"Notes": "chest pain", "page_num": 1},
            {"Notes": "Fever", "page_num": 2},
            {"Notes": "feverish", "page_num": 2}]


def groupScore(all_data, key):
    print(key)
    page_list = []
    all_page = []
    for i, data in enumerate(all_data):
        if not i == len(all_data) - 1:
            if key(data)[0].lower() == key(all_data[i + 1])[0].lower() and str(key(data)[1]).lower() == str(
                    key(all_data[i + 1])[1]).lower():
                if not i in page_list:
                    all_page.append(data)
                if not i + 1 in page_list:
                    all_page.append(all_data[i + 1])
                page_list.append(i)
                page_list.append(i + 1)

    print(len(page_list))
    page_list = list(set(page_list))
    print(len(page_list))
    print("all_page-------------")
    print(len(all_page))
    all_page = [dict(lis) for lis in {tuple(data.items()) for data in all_page}]
    print(len(all_page))


def groupScore1(all_data, key):
    print(key)
    page_list = []
    all_page = []
    for i, data in enumerate(all_data):
        lis = []
        for j, sec_data in enumerate(all_data):
            if key(data)[0].lower() == key(sec_data)[0].lower() and str(key(data)[1]).lower() == str(
                    key(sec_data)[1]).lower() and not i in page_list and not j in page_list:
                lis.append(j)
        non_page_list = list(set(lis))
        if len(non_page_list) > 1:
            page_list.extend(non_page_list)
            all_page_list = []
            for pg in non_page_list:
                all_page_list.append(all_data[pg])
            print(key(data), len(all_page_list))
            all_page.append({"key": key(data), "data": all_page_list})

    print(len(page_list))
    page_list = list(set(page_list))
    print(len(page_list))
    print("all_page-------------")

    print(len(all_page))


def groupScore2(all_data, key):
    page_list = []
    all_page = []
    for i, data in enumerate(all_data):
        lis = []
        for j, sec_data in enumerate(all_data):
            isTrue = []
            for k in range(len(key(all_data[0]))):
                # isTrue.append(fuzz.partial_ratio(str(key(data)[k]).lower(), str(key(sec_data)[k]).lower()) > 80)
                isTrue.append(str(key(data)[k]).lower() == str(key(sec_data)[k]).lower())
            if not False in isTrue and not i in page_list and not j in page_list:
                lis.append(j)
        non_page_list = list(set(lis))
        non_page_list = sorted(non_page_list, key=lambda x: x)
        if len(non_page_list) > 1:
            # print(key(data), non_page_list)
            page_list.extend(non_page_list)
            all_page_list = []
            for pg in non_page_list:
                all_page_list.append(all_data[pg])
                # print(key(all_data[pg])[0], all_data[pg]["acc_page_num"])
            print(key(data), len(all_page_list))
            all_page.append({"key": key(data), "data": all_page_list})
    print(len(all_page))


def groupScore3(all_data, key):
    page_list = []
    all_page = []
    for i, data in enumerate(all_data):
        lis = []
        for j, sec_data in enumerate(all_data):
            isTrue = []
            for k in range(len(key(all_data[0]))):
                first_text = key(data)[k]
                sec_text = key(sec_data)[k]
                if str(type(first_text)) == "<class 'str'>" and str(type(sec_text)) == "<class 'str'>":
                    isTrue.append(fuzz.partial_ratio(str(first_text).lower(), str(sec_text).lower()) > 80)
                elif str(type(first_text)) == "<class 'int'>" and str(type(sec_text)) == "<class 'int'>":
                    isTrue.append(first_text == sec_text)
            if not False in isTrue and not i in page_list and not j in page_list:
                lis.append(j)
        non_page_list = list(set(lis))
        non_page_list = sorted(non_page_list, key=lambda x: x)
        if len(non_page_list) > 1:
            # print(key(data), non_page_list)
            page_list.extend(non_page_list)
            all_page_list = []
            for pg in non_page_list:
                all_page_list.append(all_data[pg])
                print(key(all_data[pg])[0], all_data[pg]["acc_page_num"])
            # print(key(data), len(all_page_list))
            all_page.append({"key": key(data), "data": all_page_list})
    print(len(all_page))


def groupScore4(all_data, key):
    page_list = []
    for i, data in enumerate(all_data):
        lis = []
        for j, sec_data in enumerate(all_data):
            isTrue = []
            for k in range(len(key(all_data[0]))):
                first_text = key(data)[k]
                sec_text = key(sec_data)[k]
                if str(type(first_text)) == "<class 'str'>" and str(type(sec_text)) == "<class 'str'>":
                    isTrue.append(fuzz.partial_ratio(str(first_text).lower(), str(sec_text).lower()) > 80)
                elif str(type(first_text)) == "<class 'int'>" and str(type(sec_text)) == "<class 'int'>":
                    isTrue.append(first_text == sec_text)
            if not False in isTrue and not i in page_list and not j in page_list:
                lis.append(j)
        non_page_list = list(set(lis))
        non_page_list = sorted(non_page_list, key=lambda x: x)
        if len(non_page_list) > 1:
            # print(key(data), non_page_list)
            page_list.extend(non_page_list)
            all_page_list = []
            for pg in non_page_list:
                all_page_list.append(all_data[pg])
                print(key(all_data[pg])[0], all_data[pg]["acc_page_num"])
            yield key(data), all_page_list
        else:
            yield key(data), [data]


all_data = sorted(all_data, key=lambda x: (x["Notes"], x["acc_page_num"]))
# groupScore4(all_data=all_data, key=lambda x: (x["Notes"], x["acc_page_num"]))
for key, gp in groupScore4(all_data=all_data, key=lambda x: (x["Notes"], x["acc_page_num"])):
    print(key, len(gp))
