from checker import LinkChecker

def clean_links(file: str) -> list[str]:
    links = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            links.append(line)
    return links

def check_links(filename: str) -> list[LinkChecker]:
    urls = clean_links(filename)
    results = []
    for url in urls:
        link = LinkChecker(url)
        link.check()
        results.append(link)
        print(link.summary())
    return results

def write_report(results: list[LinkChecker], path: str = "report.md") -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Link Report\n\n")
        f.write(f"Checked {len(results)} link(s).\n\n")
        for result in results:
            f.write(f"- {result.summary()}\n")
    
def print_summary(results: list[LinkChecker]) -> None:
    alive = sum(1 for result in results if result.is_alive)
    dead = len(results) - alive
    print("\n--- Summary ---")
    print(f"Alive links: {alive}")
    print(f"Dead links: {dead}") 

def main() -> None:
    filename = "links.txt"
    results = check_links(filename)
    write_report(results)
    print_summary(results)
 

if __name__ == "__main__":
    main()
