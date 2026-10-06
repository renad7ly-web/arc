# يقرأ مجلد files/<السنة>/<الملف> ويولّد archive.json تلقائيًا
import json, os, re
rows = []
for year in sorted(os.listdir("files")):
    p = os.path.join("files", year)
    if not (os.path.isdir(p) and re.fullmatch(r"\d{4}", year)):
        continue
    for name in sorted(os.listdir(p)):
        if name.startswith("."):
            continue
        title = re.sub(r"[_\-]+", " ", os.path.splitext(name)[0]).strip()
        rows.append({"year": int(year), "title": title, "file": f"files/{year}/{name}"})
with open("archive.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
print(len(rows), "files indexed")
