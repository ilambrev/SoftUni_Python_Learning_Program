title = input()
article = input()
comments = []
separator = "\n"

while True:
    comment = input()

    if comment == "end of comments":
        break
    else:
        comments.append(comment)

html = f"<h1>{separator}    {title}{separator}</h1>{separator}"
html += f"<article>{separator}    {article}{separator}</article>{separator}"
html += "\n".join(f"<div>{separator}    {c}{separator}</div>" for c in comments)

print(html)