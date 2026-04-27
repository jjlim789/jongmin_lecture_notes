import os
import datetime as dt

def generate_readme(base_dir="olympiad"):
    sections = []

    # Get all subfolders (subjects) directly under the base_dir
    if not os.path.isdir(base_dir):
        print(f"Error: Directory '{base_dir}' not found.")
        return ""

    subjects = [
        name for name in sorted(os.listdir(base_dir))
        if os.path.isdir(os.path.join(base_dir, name))
    ]

    for subject in subjects:
        subject_path = os.path.join(base_dir, subject)
        
        # List PDFs inside each subject folder
        pdf_files = [
            f for f in sorted(os.listdir(subject_path))
            if f.endswith(".pdf")
        ]

        if not pdf_files:
            continue

        # Format the title (e.g., "geometry_notes" -> "Geometry Notes")
        subject_title = subject.replace("_", " ").title()
        
        section_lines = [f"## 📂 {subject_title}", ""]

        for f in pdf_files:
            # Create the Markdown link
            link = f"{base_dir}/{subject}/{f}".replace("\\", "/")
            section_lines.append(f"- [{f}]({link})")
        
        section_lines.append("")
        sections.append("\n".join(section_lines))

    # Construct the final README string
    date_str = dt.datetime.now().strftime("%Y-%m-%d")

    readme = (
        f"# Math Olympiad Lecture Notes\n\n"
        f"Last updated: {date_str}\n\n"
        f"💬 [Give Feedback](https://forms.gle/WeTzzrRcHzLPqM8RA)\n\n"
        "---\n\n"
        + "\n---\n\n".join(sections)
    )

    return readme


if __name__ == "__main__":
    # Ensure this script is run from the parent directory of 'olympiad'
    readme_content = generate_readme("olympiad")
    
    if readme_content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("README.md has been updated successfully.")