📁 Data Replication & Integrity Analysis (Python)
📌 Overview

This project demonstrates how different copying techniques in Python affect data integrity:

Assignment Copy
Shallow Copy
Deep Copy

It simulates a simple user data storage system and analyzes how modifications impact original data.

⚙️ Features
📂 Simulates user file storage and usage
🔁 Demonstrates assignment, shallow, and deep copying
✏️ Modifies copied data based on logic
🔍 Detects data corruption (leakage)
📊 Generates integrity report
🗂️ Data Structure

Each user contains:

id → User ID
data →
files → List of file names
usage → Storage usage

Example:

{
  "id": 1,
  "data": {
    "files": ["a.txt", "b.txt"],
    "usage": 500
  }
}
🔁 Copy Types Explained
1. Assignment Copy
assign_copy = users
No actual copy is created
Both variables point to the same object
⚠️ Changes affect original data
2. Shallow Copy
shallow = copy.copy(users)
Copies outer structure only
Inner objects (lists, dicts) are shared
⚠️ Partial data corruption possible
3. Deep Copy
deep = copy.deepcopy(users)
Fully independent copy
No shared references
✅ Safe from unintended changes
✏️ Modification Logic

Based on roll_no:

If even → Add "user646_file.txt"
If odd → Remove last file (if exists)
Increase usage by +100
🔍 Integrity Check

The system evaluates:

Leakage Count → Differences between original & deep copy
Safe Count → Unchanged data
Overlap Count → Common files between original & deep copy
📊 Output

The program displays:

Data before and after modification
Comparison of all copy types
Integrity report:
Leakage
Safe data
Overlap

Example:

Result Tuple: (leakage, safe, overlap)
🧪 Key Observation
Assignment & shallow copy modify original data ❌
Deep copy keeps original data intact ✅
🧑‍💻 Requirements

No external libraries required (uses built-in copy module)

▶️ How to Run
python your_script_name.py
⚠️ Data Corruption Definition

Data corruption occurs when:

Original data changes unintentionally due to improper copying methods or shared references.

📎 Notes
This project is useful for understanding memory handling in Python
Important for real-world applications like databases, caching, and backups
