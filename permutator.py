import argparse

def generate_usernames(first, last):
    first, last = first.lower(), last.lower()
    return [
        f"{first}{last}", f"{first}.{last}", f"{first}_{last}",
        f"{first}{last[0]}", f"{first[0]}{last}", f"{last}{first}"
    ]

def add_keyword_variants(usernames, keywords):
    new_usernames = set()
    for username in usernames:
        for kw in keywords:
            new_usernames.update({
                f"{username}_{kw}",
                f"{kw}_{username}",
                f"{username}.{kw}",
                f"{kw}.{username}",
                f"{username}{kw}",
                f"{kw}{username}",
            })
    return new_usernames

def attach_domain(usernames, domain):
    return {f"{u}@{domain}" for u in usernames}

def main():
    parser = argparse.ArgumentParser(
        description="Username/email permutation generator.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '-f', metavar='FILE',
        help="File with full names (one per line)."
    )
    parser.add_argument(
        '-u', metavar='USER',
        help="Specific full name in quotes, e.g., 'John Doe'."
    )
    parser.add_argument(
        '-k', metavar='KEYWORDS',
        help="Comma-separated related keywords (optional).\nExample: -k admin,it,hr"
    )
    parser.add_argument(
        '-d', metavar='DOMAIN',
        help="Domain name (optional).\nIf set, generates emails instead of usernames."
    )
    parser.add_argument(
        '-o', metavar='OUTPUT',
        help="Output file (optional).\nIf not set, results are only printed."
    )

    args = parser.parse_args()

    if args.f and args.u:
        print("Error: You can't use -f and -u at the same time.")
        return

    if not args.f and not args.u:
        print("Error: You must use either the -f or -u flag.")
        return

    keywords = []
    if args.k:
        keywords = [kw.strip().lower() for kw in args.k.split(",") if kw.strip()]
        print(f"Using related keywords: {', '.join(keywords)}")

    usernames = set()

    if args.f:
        try:
            with open(args.f, "r", encoding="utf-8") as file:
                for line in file:
                    name = line.strip()
                    if name:
                        parts = name.split()
                        if len(parts) >= 2:
                            first, last = parts[0], parts[-1]
                            usernames.update(generate_usernames(first, last))
        except FileNotFoundError:
            print(f"File '{args.f}' not found.")
            return

    elif args.u:
        parts = args.u.strip().split()
        if len(parts) >= 2:
            first, last = parts[0], parts[-1]
            usernames.update(generate_usernames(first, last))
        else:
            print("You must provide at least a first and last name.")
            return

    if keywords:
        usernames.update(add_keyword_variants(usernames, keywords))

    if args.d:
        print(f"Generating emails for domain: {args.d}")
        usernames = attach_domain(usernames, args.d)

    sorted_usernames = sorted(usernames)

    if args.o:
        with open(args.o, "w", encoding="utf-8") as output_file:
            output_file.write("\n".join(sorted_usernames))
        print(f"Saved {len(usernames)} {'emails' if args.d else 'usernames'} to '{args.o}'")
    else:
        print("\n".join(sorted_usernames))
        print(f"\nGenerated {len(usernames)} {'emails' if args.d else 'usernames'} (not saved).")

if __name__ == "__main__":
    main()
