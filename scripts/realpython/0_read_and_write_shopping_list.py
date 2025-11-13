from pathlib import Path


# Using open() method on Path object.
path = Path("shopping_list.md")
with path.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.read()
    groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))


# Using read_text() method on Path object.
content = Path("shopping_list.md").read_text(encoding="utf-8")
groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))


# Write plain text.
Path("plain_list.md").write_text("\n".join(groceries), encoding="utf-8")
