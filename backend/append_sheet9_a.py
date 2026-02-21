
import os

filepath = r"d:\Drive E\TNECL\backend\create_full_json.py"

sheet9_data = """
# Sheet 9
add_sheet("Sheet9", [
    { "Sno": 1, "Code": 9101, "CollegeName": "A.R.J. College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 2, "Code": 9102, "CollegeName": "Akshaya College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 3, "Code": 9103, "CollegeName": "Angapa College of Engineering", "Website": "", "Location": "" },
    { "Sno": 4, "Code": 9104, "CollegeName": "Angel College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 5, "Code": 9105, "CollegeName": "Arjun College of Technology", "Website": "", "Location": "" },
    { "Sno": 6, "Code": 9106, "CollegeName": "Asian College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 7, "Code": 9107, "CollegeName": "C M S College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 8, "Code": 9108, "CollegeName": "Cheran College of Engineering", "Website": "", "Location": "" },
    { "Sno": 9, "Code": 9109, "CollegeName": "Dhanalakshmi Srinivasan College of Engineering", "Website": "", "Location": "" },
    { "Sno": 10, "Code": 9110, "CollegeName": "Dhanalakshmi Srinivasan Institute of Research and Technology", "Website": "", "Location": "" },
    { "Sno": 11, "Code": 9111, "CollegeName": "Dhirajlal Gandhi College of Technology", "Website": "", "Location": "" },
    { "Sno": 12, "Code": 9112, "CollegeName": "Dr. Nagarathinam's College of Engineering", "Website": "", "Location": "" },
    { "Sno": 13, "Code": 9113, "CollegeName": "Government College of Engineering - Bargur", "Website": "", "Location": "" },
    { "Sno": 14, "Code": 9114, "CollegeName": "Er.Perumal Manimekalai College of Engineering", "Website": "", "Location": "" },
    { "Sno": 15, "Code": 9115, "CollegeName": "Jayalakshmi Institute of Technology", "Website": "", "Location": "" },
    { "Sno": 16, "Code": 9116, "CollegeName": "Jayam College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 17, "Code": 9117, "CollegeName": "Knowledge Business School, KIOT Campus", "Website": "", "Location": "" },
    { "Sno": 18, "Code": 9118, "CollegeName": "Knowledge Institute of Technology, KIOT Campus", "Website": "", "Location": "" },
    { "Sno": 19, "Code": 9120, "CollegeName": "Mahendra Engineering College", "Website": "", "Location": "" },
    { "Sno": 20, "Code": 9121, "CollegeName": "Mahendra Engineering College For Women", "Website": "", "Location": "" },
    { "Sno": 21, "Code": 9122, "CollegeName": "Mahendra Institute of Engineering &Technology", "Website": "", "Location": "" },
    { "Sno": 22, "Code": 9123, "CollegeName": "Mahendra Institute of Technology", "Website": "", "Location": "" },
    { "Sno": 23, "Code": 9124, "CollegeName": "Narasu's Sarathy Institute of Technology", "Website": "", "Location": "" },
    { "Sno": 24, "Code": 9125, "CollegeName": "P.S.V. College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 25, "Code": 9126, "CollegeName": "Sapthagiri College of Engineering", "Website": "", "Location": "" },
    { "Sno": 26, "Code": 9127, "CollegeName": "Sengunthar College of Engineering", "Website": "", "Location": "" },
    { "Sno": 27, "Code": 9128, "CollegeName": "Sengunthar Engineering College", "Website": "", "Location": "" },
    { "Sno": 28, "Code": 9129, "CollegeName": "Shree Sathyam College Of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 29, "Code": 9130, "CollegeName": "Sri Venkateswara Institute of Engineering", "Website": "", "Location": "" },
    { "Sno": 30, "Code": 9131, "CollegeName": "The Kavery College of Engineering", "Website": "", "Location": "" },
    { "Sno": 31, "Code": 9132, "CollegeName": "The Kavery Engineering College", "Website": "", "Location": "" },
    { "Sno": 32, "Code": 9133, "CollegeName": "Varuvan Vadivelan Institute of Technology", "Website": "", "Location": "" },
    { "Sno": 33, "Code": 9134, "CollegeName": "Vivekanandha College of Engineering For Women", "Website": "", "Location": "" },
    { "Sno": 34, "Code": 9135, "CollegeName": "Vivekanandha College of Technology For Women", "Website": "", "Location": "" },
    { "Sno": 35, "Code": 9136, "CollegeName": "Vivekandha Institute of Information & Management Studies", "Website": "", "Location": "" },
    { "Sno": 36, "Code": 9137, "CollegeName": "Adhiyamaan College of Engineering", "Website": "", "Location": "" },
    { "Sno": 37, "Code": 9138, "CollegeName": "A V S Engineering College", "Website": "", "Location": "" },
    { "Sno": 38, "Code": 9139, "CollegeName": "Annai Mathammal Sheela Engineering College", "Website": "", "Location": "" },
    { "Sno": 39, "Code": 9140, "CollegeName": "Bharathiyar Institute of Engineering For Women", "Website": "", "Location": "" },
    { "Sno": 40, "Code": 9141, "CollegeName": "Brahma School of Business", "Website": "", "Location": "" },
    { "Sno": 41, "Code": 9142, "CollegeName": "CMS College of Engineering", "Website": "", "Location": "" },
    { "Sno": 42, "Code": 9143, "CollegeName": "Ganesh College of Engineering", "Website": "", "Location": "" },
    { "Sno": 43, "Code": 9144, "CollegeName": "Gnanamani College of Engineering", "Website": "", "Location": "" },
    { "Sno": 44, "Code": 9145, "CollegeName": "Gnanamani College of Technology", "Website": "", "Location": "" },
    { "Sno": 45, "Code": 9146, "CollegeName": "Gnanamani Institute of Management Studies", "Website": "", "Location": "" },
    { "Sno": 46, "Code": 9147, "CollegeName": "Greentech College of Engineering For Women", "Website": "", "Location": "" },
    { "Sno": 47, "Code": 9148, "CollegeName": "Idaya Engineering College For Women", "Website": "", "Location": "" },
    { "Sno": 48, "Code": 9149, "CollegeName": "King College of Technology", "Website": "", "Location": "" },
    { "Sno": 49, "Code": 9150, "CollegeName": "Kongunadu College of Engineering &Technology", "Website": "", "Location": "" },
    { "Sno": 50, "Code": 9151, "CollegeName": "Maha Barathi Engineering College", "Website": "", "Location": "" }
"""

with open(filepath, 'r') as f:
    content = f.read()

# Replace the last ]) with the new data (incomplete Sheet 9 list)
if "])" in content:
    parts = content.rsplit("])", 1)
    new_content = parts[0] + "])\n" + sheet9_data + parts[1]
    with open(filepath, 'w') as f:
        f.write(new_content)
    print("Appended Sheet 9 (Part 1) successfully")
else:
    print("Could not find ]) in file")
