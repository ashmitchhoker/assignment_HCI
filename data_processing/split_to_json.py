import json
import re

def split_careers_to_json(careers, text_file_path, output_path="careers.json"):
    # Sort headings by length to avoid substring conflicts
    careers_sorted = sorted(careers, key=len, reverse=True)

    pattern = r"(" + "|".join(re.escape(c) for c in careers_sorted) + r")"

    with open(text_file_path, "r", encoding="utf-8") as f:
        text = f.read()

    parts = re.split(pattern, text)

    result = []
    current_title = None
    buffer = []

    id_counter = 1

    for part in parts:
        stripped = part.strip()
        if stripped in careers:
            if current_title:
                content = " ".join(buffer)
                result.append({
                    "id": id_counter,
                    "title": current_title,
                    "content": content
                })
                id_counter += 1

            current_title = stripped
            buffer = []
        else:
            if current_title:
                buffer.append(part)

    # Last career block
    if current_title:
        content = " ".join(buffer)
        result.append({
            "id": id_counter,
            "title": current_title,
            "content": content
        })

    # Write JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    return result


with open("career_names.json", "r", encoding="utf-8") as f:
    career_names = json.load(f)

split_careers_to_json(career_names, "cleaned_text.txt", output_path="careers_cleaned.json")

