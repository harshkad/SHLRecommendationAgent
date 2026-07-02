import json
import re

INPUT_FILE = "data/assessments.json"
OUTPUT_FILE = "data/clean_assessments.json"


def clean_text(text):

    if not text:
        return ""

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_test_type(full_text):
    # Matches uppercase characters separated by spaces, stopping before lowercase words
    match = re.search(r"Test Type:\s*([A-Z](?:\s+[A-Z])*)", full_text)
    if match:
        return match.group(1).strip()
    return "General"


def main():

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    cleaned = []
    seen_urls = set()

    for item in data:

        url = item.get("url", "").strip()

        if not url:
            continue

        # remove duplicates
        if url in seen_urls:
            continue

        seen_urls.add(url)

        name = clean_text(item.get("name", ""))
        description = clean_text(item.get("description", ""))
        full_text = clean_text(item.get("full_text", ""))

        combined_text = f"{name}. {description}. {full_text}"

        assessment = {
            "name": name,
            "url": url,
            "description": description,
            "test_type": extract_test_type(full_text), # <-- Pass full_text here
            "search_text": combined_text[:5000]
        }

        cleaned.append(assessment)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(cleaned)} clean assessments")


if __name__ == "__main__":
    main()
    