import streamlit as st

GRADE_MAP = {
    'O': 10,
    'A+': 9,
    'A': 8,
    'B+': 7,
    'B': 6,
    'C': 5,
    'Others': 0
}

def calculate_cgpa(subjects):
    total_credits = 0
    total_points = 0

    for subject, credit, grade in subjects:
        total_credits += credit
        total_points += credit * grade

    if total_credits == 0:
        return 0.0
    
    cgpa = total_points / total_credits
    return cgpa

def main():
    st.title("CGPA Calculator App")

    st.sidebar.header("User Input")
    
    default_subjects = [
        ("ETHICAL HACKING", 3, 'O'),
        ("SERVERLESS COMPUTING", 3, 'O'),
        ("PRINCIPLES OF COMPILER DESIGN", 3, 'O'),
        ("CRYPTOGRAPHY AND NETWORK SECURITY", 3, 'O'),
        ("ARTIFICIAL INTELLIGENCE", 3, 'O'),
        ("COMPILER DESIGN LABORATORY", 1.5, 'O'),
        ("ARTIFICIAL INTELLIGENCE LABORATORY", 1, 'O'),
        ("ADVANCED APPLICATION DEVELOPMENT", 3, 'O')
    ]

    subjects = []

    for i, (subject, credit, default_grade) in enumerate(default_subjects):
        grade = st.sidebar.selectbox(f"Grade for {subject}", list(GRADE_MAP.keys()), list(GRADE_MAP.keys()).index(default_grade))
        subjects.append((subject, credit, GRADE_MAP[grade]))

    additional_subjects = st.sidebar.number_input("Number of Additional Subjects", min_value=0, value=0)

    for i in range(additional_subjects):
        subject_name = st.sidebar.text_input(f"Name of Additional Subject {i + 1}")
        credit = st.sidebar.number_input(f"Credits for {subject_name}", min_value=1, value=3)
        grade_input = st.sidebar.text_input(f"Grade for {subject_name} (Enter 'O', 'A+', 'A-', 'B+', 'B-', 'C', or 'Others')", 'O')
        grade = GRADE_MAP.get(grade_input.upper(), 0)
        subjects.append((subject_name, credit, grade))

    if st.sidebar.button("Calculate CGPA"):
        cgpa = calculate_cgpa(subjects)
        st.success(f"Your CGPA is: {cgpa:.2f}")

    st.text("Made with 🧡 by DHARANI2D")

if __name__ == "__main__":
    main()
