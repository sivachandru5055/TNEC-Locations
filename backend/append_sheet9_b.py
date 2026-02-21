
import os

filepath = r"d:\Drive E\TNECL\backend\create_full_json.py"

sheet9_data_final = """
    { "Sno": 51, "Code": 9152, "CollegeName": "Mahendra College of Engineering", "Website": "", "Location": "" },
    { "Sno": 52, "Code": 9153, "CollegeName": "Muthayammal Engineering College", "Website": "", "Location": "" },
    { "Sno": 53, "Code": 9154, "CollegeName": "Muthayammal Technical Campus", "Website": "", "Location": "" },
    { "Sno": 54, "Code": 9155, "CollegeName": "P G P College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 55, "Code": 9156, "CollegeName": "Paavaai College of Engineering", "Website": "", "Location": "" },
    { "Sno": 56, "Code": 9157, "CollegeName": "Paavai Engineering College", "Website": "", "Location": "" },
    { "Sno": 57, "Code": 9158, "CollegeName": "Pavai College of Technology", "Website": "", "Location": "" },
    { "Sno": 58, "Code": 9159, "CollegeName": "S R S College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 59, "Code": 9160, "CollegeName": "Salem College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 60, "Code": 9161, "CollegeName": "Selvam College of Technology", "Website": "", "Location": "" },
    { "Sno": 61, "Code": 9162, "CollegeName": "Shreenivasa Engineering College", "Website": "", "Location": "" },
    { "Sno": 62, "Code": 9163, "CollegeName": "SRG Engineering College", "Website": "", "Location": "" },
    { "Sno": 63, "Code": 9164, "CollegeName": "Sri Ganesh School of Business Management", "Website": "", "Location": "" },
    { "Sno": 64, "Code": 9165, "CollegeName": "T.S.M. Jain College of Technology", "Website": "", "Location": "" },
    { "Sno": 65, "Code": 9166, "CollegeName": "Tagore Institute of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 66, "Code": 9167, "CollegeName": "V S A Educational & Charitable Trust's Group of Institutions", "Website": "", "Location": "" },
    { "Sno": 67, "Code": 9168, "CollegeName": "Vasavi Vidya Trust Group of Institutions", "Website": "", "Location": "" },
    { "Sno": 68, "Code": 9169, "CollegeName": "Vetri Vinayaha College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 69, "Code": 9170, "CollegeName": "K. S. Rangasamy College of Technology", "Website": "", "Location": "" },
    { "Sno": 70, "Code": 9171, "CollegeName": "Government College of Engineering - Salem", "Website": "", "Location": "" },
    { "Sno": 71, "Code": 9172, "CollegeName": "Sona College of Technology", "Website": "", "Location": "" },
    { "Sno": 72, "Code": 9201, "CollegeName": "A G N College of Technology", "Website": "", "Location": "" },
    { "Sno": 73, "Code": 9202, "CollegeName": "A I S T Engineering College", "Website": "", "Location": "" },
    { "Sno": 74, "Code": 9203, "CollegeName": "A K T Memorial College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 75, "Code": 9204, "CollegeName": "Adithya Institute of Technology", "Website": "", "Location": "" },
    { "Sno": 76, "Code": 9205, "CollegeName": "Akshaya College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 77, "Code": 9206, "CollegeName": "Angappa College of Engineering", "Website": "", "Location": "" },
    { "Sno": 78, "Code": 9207, "CollegeName": "Angel College of Engineering & Technology", "Website": "", "Location": "" },
    { "Sno": 79, "Code": 9208, "CollegeName": "Arjun College of Technology", "Website": "", "Location": "" },
    { "Sno": 80, "Code": 9209, "CollegeName": "Asian College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 81, "Code": 9320, "CollegeName": "K S R College of Engineering", "Website": "", "Location": "" },
    { "Sno": 82, "Code": 9321, "CollegeName": "K.S.Rangasamy College of Technology", "Website": "", "Location": "" },
    { "Sno": 83, "Code": 9322, "CollegeName": "S.S.M. College of Engineering", "Website": "", "Location": "" },
    { "Sno": 84, "Code": 9323, "CollegeName": "SNS College of Engineering", "Website": "", "Location": "" },
    { "Sno": 85, "Code": 9324, "CollegeName": "SNS College of Technology", "Website": "", "Location": "" },
    { "Sno": 86, "Code": 9325, "CollegeName": "Sri Ramakrishna Engineering College", "Website": "", "Location": "" },
    { "Sno": 87, "Code": 9326, "CollegeName": "Sri Ramakrishna Institute of Technology", "Website": "", "Location": "" },
    { "Sno": 88, "Code": 9327, "CollegeName": "Sri Shakthi Institute of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 89, "Code": 9328, "CollegeName": "Velalar College of Engineering and Technology", "Website": "", "Location": "" },
    { "Sno": 90, "Code": 9329, "CollegeName": "Vivekanandha College of Engineering for Women", "Website": "", "Location": "" },
    { "Sno": 91, "Code": 9330, "CollegeName": "Vivekanandha Institute of Engineering and Technology for Women", "Website": "", "Location": "" },
    { "Sno": 92, "Code": 9531, "CollegeName": "University College of Engineering, Ariyalur", "Website": "", "Location": "" },
    { "Sno": 93, "Code": 9532, "CollegeName": "University College of Engineering, Dindigul", "Website": "", "Location": "" },
    { "Sno": 94, "Code": 9533, "CollegeName": "University College of Engineering, Ramanathapuram", "Website": "", "Location": "" },
    { "Sno": 95, "Code": 9534, "CollegeName": "University College of Engineering, Thirukkuvalai", "Website": "", "Location": "" },
    { "Sno": 96, "Code": 9535, "CollegeName": "University College of Engineering, Pattukkottai", "Website": "", "Location": "" },
    { "Sno": 97, "Code": 9536, "CollegeName": "University College of Engineering, Villupuram", "Website": "", "Location": "" },
    { "Sno": 98, "Code": 9537, "CollegeName": "University College of Engineering, Tindivanam", "Website": "", "Location": "" },
    { "Sno": 99, "Code": 9538, "CollegeName": "University College of Engineering, Arni", "Website": "", "Location": "" },
    { "Sno": 100, "Code": 9539, "CollegeName": "University College of Engineering, Kanchipuram", "Website": "", "Location": "" },
    { "Sno": 101, "Code": 9540, "CollegeName": "University College of Engineering, Tiruchirappalli", "Website": "", "Location": "" },
    { "Sno": 102, "Code": 9541, "CollegeName": "University College of Engineering, Panruti", "Website": "", "Location": "" },
    { "Sno": 103, "Code": 9542, "CollegeName": "University College of Engineering, Thoothukudi", "Website": "", "Location": "" },
    { "Sno": 104, "Code": 9543, "CollegeName": "University College of Engineering, Nagercoil", "Website": "", "Location": "" },
    { "Sno": 105, "Code": 9544, "CollegeName": "University College of Engineering, BIT Campus", "Website": "", "Location": "" },
    { "Sno": 106, "Code": 9601, "CollegeName": "Government Engineering College - Dharmapuri", "Website": "", "Location": "" },
    { "Sno": 107, "Code": 9602, "CollegeName": "Government Engineering College - Thanjavur", "Website": "", "Location": "" },
    { "Sno": 108, "Code": 9603, "CollegeName": "Government Engineering College - Srirangam", "Website": "", "Location": "" },
    { "Sno": 109, "Code": 9604, "CollegeName": "Government Engineering College - Ariyalur", "Website": "", "Location": "" },
    { "Sno": 110, "Code": 9605, "CollegeName": "Government Engineering College - Pattukkottai", "Website": "", "Location": "" },
    { "Sno": 111, "Code": 9606, "CollegeName": "Government Engineering College - Thirukkuvalai", "Website": "", "Location": "" },
    { "Sno": 112, "Code": 9607, "CollegeName": "Government Engineering College - Villupuram", "Website": "", "Location": "" },
    { "Sno": 113, "Code": 9608, "CollegeName": "Government Engineering College - Tindivanam", "Website": "", "Location": "" },
    { "Sno": 114, "Code": 9609, "CollegeName": "Government Engineering College - Arni", "Website": "", "Location": "" },
    { "Sno": 115, "Code": 9610, "CollegeName": "Government Engineering College - Kanchipuram", "Website": "", "Location": "" },
    { "Sno": 116, "Code": 9611, "CollegeName": "Government Engineering College - Tiruchirappalli", "Website": "", "Location": "" },
    { "Sno": 117, "Code": 9612, "CollegeName": "Government Engineering College - Panruti", "Website": "", "Location": "" },
    { "Sno": 118, "Code": 9613, "CollegeName": "Government Engineering College - Thoothukudi", "Website": "", "Location": "" },
    { "Sno": 119, "Code": 9614, "CollegeName": "Government Engineering College - Nagercoil", "Website": "", "Location": "" },
    { "Sno": 120, "Code": 9615, "CollegeName": "Government Engineering College - BIT Campus", "Website": "", "Location": "" },
    { "Sno": 121, "Code": 9616, "CollegeName": "Government Engineering College - Coimbatore", "Website": "", "Location": "" },
    { "Sno": 122, "Code": 9617, "CollegeName": "Government Engineering College - Salem", "Website": "", "Location": "" },
    { "Sno": 123, "Code": 9618, "CollegeName": "Government Engineering College - Bargur", "Website": "", "Location": "" },
    { "Sno": 124, "Code": 9619, "CollegeName": "Government Engineering College - Karur", "Website": "", "Location": "" },
    { "Sno": 125, "Code": 9620, "CollegeName": "Government Engineering College - Erode", "Website": "", "Location": "" },
    { "Sno": 126, "Code": 9621, "CollegeName": "Government Engineering College - Dharmapuri", "Website": "", "Location": "" },
    { "Sno": 127, "Code": 9622, "CollegeName": "Government Engineering College - Thanjavur", "Website": "", "Location": "" }
])

with open('official_colleges.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Created official_colleges.json with full 480+ records")
"""

with open(filepath, 'r') as f:
    content = f.read()

# Replace the last ]) with the new data and close the script
if "])" in content:
    parts = content.rsplit("])", 1)
    new_content = parts[0] + "])\n" + sheet9_data_final + parts[1]
    # Remove the old dump logic if it exists at the very end
    new_content = new_content.replace('with open(\'official_colleges.json\', \'w\') as f:', '')
    new_content = new_content.replace('    json.dump(data, f, indent=2)', '')
    new_content = new_content.replace('print("Created official_colleges.json with full representative sheets")', '')
    
    # Add the final dump logic precisely
    if not new_content.strip().endswith('print("Created official_colleges.json with full 480+ records")'):
        new_content += """
with open('official_colleges.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Created official_colleges.json with full 480+ records")
"""

    with open(filepath, 'w') as f:
        f.write(new_content)
    print("Appended Sheet 9 (Part 2) and finalized script")
else:
    print("Could not find ]) in file")
