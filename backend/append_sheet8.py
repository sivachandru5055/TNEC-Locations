
import os

filepath = r"d:\Drive E\TNECL\backend\create_full_json.py"

sheet8_data = """
# Sheet 8
add_sheet("Sheet8", [
    { "Sno": 1, "Code": 8101, "CollegeName": "A.V.C. College of Engineering", "Website": "", "Location": "" },
    { "Sno": 2, "Code": 8102, "CollegeName": "Anjalai Ammal Mahalingam Engineering College", "Website": "", "Location": "" },
    { "Sno": 3, "Code": 8103, "CollegeName": "Annai College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 4, "Code": 8104, "CollegeName": "Arasu Engineering College", "Website": "", "Location": "" },
    { "Sno": 5, "Code": 8105, "CollegeName": "As-Salam College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 6, "Code": 8106, "CollegeName": "CARE College of Engineering", "Website": "", "Location": "" },
    { "Sno": 7, "Code": 8107, "CollegeName": "Chendhuran College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 8, "Code": 8108, "CollegeName": "Dhanalakshmi Srinivasan Institute of Research and Technology", "Website": "", "Location": "" },
    { "Sno": 9, "Code": 8110, "CollegeName": "Government College of Engineering - Thanjavur", "Website": "", "Location": "" },
    { "Sno": 10, "Code": 8111, "CollegeName": "Government College of Engineering -- Srirangam", "Website": "", "Location": "" },
    { "Sno": 11, "Code": 8112, "CollegeName": "Hajee Karutha Rowther Howdia College", "Website": "", "Location": "" },
    { "Sno": 12, "Code": 8113, "CollegeName": "Indra Ganesan College of Engineering", "Website": "", "Location": "" },
    { "Sno": 13, "Code": 8114, "CollegeName": "J.J. College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 14, "Code": 8115, "CollegeName": "K.Ramakrishnan College of Engineering", "Website": "", "Location": "" },
    { "Sno": 15, "Code": 8116, "CollegeName": "K.Ramakrishnan College of Technology", "Website": "", "Location": "" },
    { "Sno": 16, "Code": 8117, "CollegeName": "Kings College of Engineering", "Website": "", "Location": "" },
    { "Sno": 17, "Code": 8118, "CollegeName": "M.A.M. College of Engineering", "Website": "", "Location": "" },
    { "Sno": 18, "Code": 8120, "CollegeName": "M.A.M. College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 19, "Code": 8121, "CollegeName": "M.A.M. School of Engineering", "Website": "", "Location": "" },
    { "Sno": 20, "Code": 8122, "CollegeName": "M.I.E.T. Engineering College", "Website": "", "Location": "" },
    { "Sno": 21, "Code": 8123, "CollegeName": "Mahalakshmi Engineering College", "Website": "", "Location": "" },
    { "Sno": 22, "Code": 8124, "CollegeName": "Mookambigai College of Engineering", "Website": "", "Location": "" },
    { "Sno": 23, "Code": 8125, "CollegeName": "Mount Zion College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 24, "Code": 8126, "CollegeName": "N.S.N. College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 25, "Code": 8127, "CollegeName": "OAS Institute of Technology and Management", "Website": "", "Location": "" },
    { "Sno": 26, "Code": 8128, "CollegeName": "Oxford Engineering College", "Website": "", "Location": "" },
    { "Sno": 27, "Code": 8129, "CollegeName": "P.R. Engineering College", "Website": "", "Location": "" },
    { "Sno": 28, "Code": 8130, "CollegeName": "Parisutham Institute of Technology and Science", "Website": "", "Location": "" },
    { "Sno": 29, "Code": 8131, "CollegeName": "Periyar Maniammai Institute of Science & Technology", "Website": "", "Location": "" },
    { "Sno": 30, "Code": 8132, "CollegeName": "R.V.S. College of Engineering", "Website": "", "Location": "" },
    { "Sno": 31, "Code": 8133, "CollegeName": "Roever College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 32, "Code": 8134, "CollegeName": "Roever Institute of Technology", "Website": "", "Location": "" },
    { "Sno": 33, "Code": 8135, "CollegeName": "S.A.S.T.R.A. University", "Website": "", "Location": "" },
    { "Sno": 34, "Code": 8136, "CollegeName": "Saranathan College of Engineering", "Website": "", "Location": "" },
    { "Sno": 35, "Code": 8137, "CollegeName": "Sastra University", "Website": "", "Location": "" },
    { "Sno": 36, "Code": 8138, "CollegeName": "Sengunthar Engineering College", "Website": "", "Location": "" },
    { "Sno": 37, "Code": 8139, "CollegeName": "Shivani Engineering College", "Website": "", "Location": "" },
    { "Sno": 38, "Code": 8140, "CollegeName": "Sir Issac Newton College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 39, "Code": 8141, "CollegeName": "SMR East Coast College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 40, "Code": 8142, "CollegeName": "Sri Bharathi Engineering College for Women", "Website": "", "Location": "" },
    { "Sno": 41, "Code": 8143, "CollegeName": "Star Lion College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 42, "Code": 8144, "CollegeName": "Sudharsan Engineering College", "Website": "", "Location": "" },
    { "Sno": 43, "Code": 8145, "CollegeName": "Thanjavur Nayakkar College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 44, "Code": 8146, "CollegeName": "Trichy Engineering College", "Website": "", "Location": "" },
    { "Sno": 45, "Code": 8147, "CollegeName": "Udayam Poly College", "Website": "", "Location": "" },
    { "Sno": 46, "Code": 8148, "CollegeName": "University College of Engineering, Ariyalur", "Website": "", "Location": "" },
    { "Sno": 47, "Code": 8149, "CollegeName": "University College of Engineering, Pattukkottai", "Website": "", "Location": "" },
    { "Sno": 48, "Code": 8150, "CollegeName": "University College of Engineering, Thirukkuvalai", "Website": "", "Location": "" },
    { "Sno": 49, "Code": 8151, "CollegeName": "Valivalam Desikar Poly College", "Website": "", "Location": "" },
    { "Sno": 50, "Code": 8152, "CollegeName": "Vandayar Engineering College", "Website": "", "Location": "" },
    { "Sno": 51, "Code": 8201, "CollegeName": "A.R.J. College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 52, "Code": 8202, "CollegeName": "Bharathidasan University", "Website": "", "Location": "" }
])
"""

with open(filepath, 'r') as f:
    content = f.read()

# Replace the last ]) with the new data
if "])" in content:
    parts = content.rsplit("])", 1)
    new_content = parts[0] + "])\n" + sheet8_data + parts[1]
    with open(filepath, 'w') as f:
        f.write(new_content)
    print("Appended Sheet 8 successfully")
else:
    print("Could not find ]) in file")
