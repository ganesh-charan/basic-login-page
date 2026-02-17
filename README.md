# Smart Transport Load Balancing System

---
 
### 💻PROJECT DESCRIPTION:
This project deals  with filtering of weights given by client and divide them into categories.

### THE CATEGORIES ARE:
- < 0 → Invalid Entry
- 0–5 → Very Light
- 6–25 → Normal Load
- 26–60 → Heavy Load
- 60 → Overload

They got classified into their own lists 
#### 📃Lists:
- very_light
- normal_load
- heavy_load
- overload
- invalid_entries
as per above criterion

---

## ⁉️Logic Implemented :
- To categorize weights in List given by client I used for loop to cheek every value and sort them as per criterion above
- used logic length of initial client given list - invalid entries list to get valid entries
- also calculated affected entries due to "PLI" by counting when RULE A is applied

---

### MY NAME IS "paturu v n s ganesh charan"
#### L=26-5=21
#### PLI=21%3=0
So I implemented RULE A 

---

## 🧠RULE A(PLI=0):
After categorizing lists move overload list to invalid lists

---

## 🧠RULE B(PLI=1):
Remove all very light items 

---

## 🧠RULE C(PLI=3):
Keep only normal and heavy loads  

---

### implementation(RULE A):
- I used a for loop to go through each value of OVERLOAD list
- Appended each value into invalid entries
- Displayed all lists at the end along with counts

---

## Technologies Used

- Python
- Lists
- For loops
- Conditional statements

---

## Output Includes

- Categorized weight lists
- Total valid entries
- Number of affected items due to PLI
- Final loading plan

---

## Author

Ganesh Charan




