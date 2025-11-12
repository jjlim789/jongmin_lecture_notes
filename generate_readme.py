import os
import datetime as dt

def generate_readme(base_dir="olympiad"):
    sections = []

    # Go one folder deep inside olympiad
    for folder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        # Collect PDF files in this subfolder
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
        pdf_files.sort()

        if not pdf_files:
            continue

        # Section title
        section_title = f"## 📂 {folder.replace('_', ' ').title()} (`{base_dir}/{folder}`)"
        section_lines = [section_title, ""]

        # File entries
        for f in pdf_files:
            link = f"{base_dir}/{folder}/{f}"
            section_lines.append(f"- [{f}]({link})")

        sections.append("\n".join(section_lines))

    date_str = dt.datetime.now().strftime("%Y-%m-%d")
    # Assemble README
    readme = (
        f"# Olympiad Lecture Notes (last updated {date_str})\n\n"
        f"💬 [Give Feedback](https://forms.gle/WeTzzrRcHzLPqM8RA)\n\n"
        "---\n\n"
        + "\n\n---\n\n".join(sections)
    )
    return readme

if __name__ == "__main__":
    readme_content = generate_readme("olympiad")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("README.md has been updated.")
