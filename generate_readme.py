import os
import datetime as dt

def generate_readme(base_dir="olympiad"):
    sections = []

    def process_category(title, folder_name):
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.isdir(folder_path):
            return

        section_lines = [f"## 📂 {title} (`{base_dir}/{folder_name}`)", ""]

        # Check if this folder contains subfolders
        subfolders = [
            name for name in sorted(os.listdir(folder_path))
            if os.path.isdir(os.path.join(folder_path, name))
        ]

        if subfolders:
            # --- Case 1: category has subfolders (camp_notes) ---
            for subject in subfolders:
                subject_path = os.path.join(folder_path, subject)

                # List PDFs inside subject folder
                pdf_files = [
                    f for f in os.listdir(subject_path)
                    if f.endswith(".pdf")
                ]
                pdf_files.sort()

                if not pdf_files:
                    continue

                subject_title = subject.replace("_", " ").title()
                section_lines.append(f"### {subject_title}\n")

                for f in pdf_files:
                    link = f"{base_dir}/{folder_name}/{subject}/{f}".replace("\\", "/")
                    section_lines.append(f"- [{f}]({link})")
                section_lines.append("")

        else:
            # --- Case 2: category has NO subfolders (geometry_lectures) ---
            pdf_files = [
                f for f in sorted(os.listdir(folder_path))
                if f.endswith(".pdf")
            ]

            for f in pdf_files:
                link = f"{base_dir}/{folder_name}/{f}".replace("\\", "/")
                section_lines.append(f"- [{f}]({link})")
            section_lines.append("")

        sections.append("\n".join(section_lines))

    # Process the two known categories
    process_category("Camp Notes", "camp_notes")
    process_category("Geometry Lectures", "geometry_lectures")

    date_str = dt.datetime.now().strftime("%Y-%m-%d")

    readme = (
        f"# Math Olympiad Lecture Notes\n\n"
        f"last updated {date_str}\n\n"
        f"💬 [Give Feedback](https://forms.gle/WeTzzrRcHzLPqM8RA)\n\n"
        "---\n\n"
        + "\n---\n\n".join(sections)
    )

    return readme


if __name__ == "__main__":
    readme_content = generate_readme("olympiad")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("README.md has been updated.")
