from rapidfuzz import fuzz


def groupbyScore(all_data, key):
    page_list = []
    used_list = []
    # FIRST LOOP
    for i, data in enumerate(all_data):
        if not i in used_list:
            lis = []
            # SECOND LOOP
            for j, sec_data in enumerate(all_data):
                isTrue = []
                # LIST OF KEY LEN
                for k in range(len(key(all_data[0]))):
                    first_text = key(data)[k]
                    sec_text = key(sec_data)[k]
                    # CHECK KEY TYPE STR
                    if str(type(first_text)) == "<class 'str'>" and str(type(sec_text)) == "<class 'str'>":
                        isTrue.append(fuzz.partial_ratio(str(first_text).lower(), str(sec_text).lower()) > 80)
                    # CHECK KEY TYPE INT
                    elif str(type(first_text)) == "<class 'int'>" and str(type(sec_text)) == "<class 'int'>":
                        isTrue.append(first_text == sec_text)
                # CHECK PAGE LIST
                if not False in isTrue and not i in page_list and not j in page_list:
                    lis.append(j)
                    used_list.append(j)
            # CHECK LIST AND SORTED
            non_page_list = list(set(lis))
            non_page_list = sorted(non_page_list, key=lambda x: x)
            if len(non_page_list) > 1:
                page_list.extend(non_page_list)
                all_page_list = []
                # YIELD DUP DATA
                for pg in non_page_list:
                    all_page_list.append(all_data[pg])
                yield key(data), all_page_list
            else:
                # YIELD NON DUP DATA
                yield key(data), [data]
