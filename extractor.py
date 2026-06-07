import os
import re
import csv

Folder containing the HTML response files

folder = os.path.expanduser("~/info")

with open("business_data.csv", "w", newline="", encoding="utf-8") as csvfile:
writer = csv.writer(csvfile)

writer.writerow([
    "file",
    "reference_number",
    "business_name",
    "email",
    "phone",
    "nature_of_business",
    "applicant_name",
    "address"
])

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    if not os.path.isfile(filepath):
        continue

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        reference = re.search(
            r'Reference Number.*?</b>\s*([^<]+)',
            content,
            re.I | re.S
        )

        business = re.search(
            r'Name of Business or Person&nbsp;:&nbsp;</b>\s*([^<]+)',
            content,
            re.I
        )

        email = re.search(
            r'Email&nbsp;:&nbsp;</b>\s*([^<]+)',
            content,
            re.I
        )

        phone = re.search(
            r'Phone&nbsp;:&nbsp;</b>\s*([0-9]+)',
            content,
            re.I
        )

        nature = re.search(
            r'Nature of Business&nbsp;:&nbsp;</b>\s*([^<]+)',
            content,
            re.I
        )

        applicant = re.search(
            r'Name of Applicant&nbsp;:&nbsp;</b>\s*([^<]+)',
            content,
            re.I
        )

        address = re.search(
            r'Address.*?&nbsp;:&nbsp;</b>\s*([^<]+)',
            content,
            re.I | re.S
        )

        writer.writerow([
            filename,
            reference.group(1).strip() if reference else "",
            business.group(1).strip() if business else "",
            email.group(1).strip() if email else "",
            phone.group(1).strip() if phone else "",
            nature.group(1).strip() if nature else "",
            applicant.group(1).strip() if applicant else "",
            address.group(1).strip() if address else ""
        ])

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Done! Results saved to business_data.csv")
