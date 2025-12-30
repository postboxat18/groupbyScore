# 🔍 `groupbyScore` – Group Similar Items Using Fuzzy Matching in Python

[![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/postboxat18/groupbyScore.git)

## Overview

`groupbyScore` is a Python function that groups similar records from a list of dictionaries using fuzzy matching. It utilizes the **`rapidfuzz`** package for high-performance string similarity scoring.

---

## 📦 Dependencies

* Python 3.6+
* [`rapidfuzz`](https://github.com/maxbachmann/RapidFuzz)

Install with:

```bash
pip install rapidfuzz
```

---

## 🚀 Function Signature

```python
groupbyScore(all_data, score, key)
```

### Parameters

* `all_data` (`List[dict]`): A list of dictionaries to be grouped.
* `key` (`Callable`): A function returning a tuple of values (e.g., `lambda x: (x["Notes"], x["page_num"])`) used to compare and group.

---

## ⚙️ How It Works

1. Iterates over all item pairs in the dataset.
2. Compares each field in the `key(...)` tuple:

   * **Strings**: `fuzz.partial_ratio` > 80
   * **Integers**: must match exactly
3. Groups items where **all** key fields match.
4. Yields:

   * the group key
   * the list of matching items

---

## ✅ Example Usage

```python
from groupbyScore.groupbyScore import groupbyScore

data = [
    {"Notes": "Chest Pain", "page_num": 1},
    {"Notes": "chest pain", "page_num": 1},
    {"Notes": "church", "page_num": 1},
    {"Notes": "Fever", "page_num": 2},
    {"Notes": "feverish", "page_num": 2}
]
# TUPLE
for key, group in groupbyScore(data, key=lambda x: (x["Notes"], x["page_num"]),score=90):
    print("Group Key:", key)
    print("Group Items:", group)
# STR
for key, group in groupbyScore(data, key=lambda x: x["Notes"],score=90):
    print("Group Key:", key)
    print("Group Items:", group)

```

---

## 📤 Example Output

```
#### OUTPUT 1
Group Key: ('Chest Pain', 1)
Group Items: [{'Notes': 'Chest Pain', 'page_num': 1}, {'Notes': 'chest pain', 'page_num': 1}]

Group Key: ('church', 1)
Group Items: [{'Notes': 'church', 'page_num': 1}]

Group Key: ('Fever', 2)
Group Items: [{'Notes': 'Fever', 'page_num': 2}, {'Notes': 'feverish', 'page_num': 2}]

#### OUTPUT 2
Group Key: Chest Pain
Group Items: [{'Notes': 'Chest Pain', 'page_num': 1}, {'Notes': 'chest pain', 'page_num': 1}]

Group Key: church
Group Items: [{'Notes': 'church', 'page_num': 1}]

Group Key: Fever
Group Items: [{'Notes': 'Fever', 'page_num': 2}, {'Notes': 'feverish', 'page_num': 2}]
```

---

## 📎 GitHub

🔗 [https://github.com/postboxat18/groupbyScore.git](https://github.com/postboxat18/groupbyScore.git)

