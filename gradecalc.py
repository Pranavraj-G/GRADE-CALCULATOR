import streamlit as st

def main():
    st.title("Simple Grade Calculator")
    
    # Allow users to input their test score
    test_score = st.number_input("Enter your test score", min_value=0, max_value=100, step=1)

    # Calculate the final grade based on the grading scale
    final_grade = calculate_grade(test_score)

    # Display the final grade
    st.write(f"Your final grade is: {final_grade}")

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    main()
