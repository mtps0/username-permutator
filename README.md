# 🧩 Username & Email Permutator

A flexible tool for generating username or email permutations based on full names, with optional keywords and custom domain support.

---

## 🔍 What is this?

This script is built for:

- Username enumeration during internal/external assessments
- Generating email wordlists for password spraying
- Creating realistic user/email lists for OSINT

---

## 🚀 Features

- Accepts a single name or a file of names
- Generates multiple permutations (dots, underscores, initials, reversed)
- Adds optional keyword variants (e.g., admin, hr, it)
- Generates full email addresses with a custom domain
- Outputs to a file **only if requested** with `-o`

---

## ⚙️ Usage

```bash
# From a single name
python permutator.py -u "John Doe"

# From a file
python permutator.py -f names.txt

# With keywords
python permutator.py -f names.txt -k "admin,hr"

# Generate emails with a domain
python permutator.py -f names.txt -d company.com

# Save to a file
python permutator.py -f names.txt -k "it" -d company.com -o emails.txt
```
---

## 📥 Flags

| Flag         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `-f FILE`    | File with full names (one per line).                                        |
| `-u USER`    | A specific full name in quotes, e.g., `"John Doe"`.                         |
| `-k KEYWORDS`| Comma-separated keywords like `"admin,hr,it"` (optional).                   |
| `-d DOMAIN`  | Adds a domain to generate emails instead of usernames (optional).           |
| `-o OUTPUT`  | Output file name (optional). If not used, results are printed only.         |


## ⚠️ You must use either -f or -u, but not both.

---
## 🔄 Example Output

```bash
python permutator.py -u "john doe" -d example.com -o emails.txt
```

```text
johndoe@example.com
john.doe@example.com
adminjohndoe@example.com
johndoeadmin@example.com
j.doe@example.com
doejohn@example.com
```

## 📦 Installation

No dependencies required.

```bash
git clone https://github.com/mtps0/username-permutator
cd username-permutator
python permutator.py -h
```
