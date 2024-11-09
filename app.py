import streamlit as st

st.title("Simple Calculator")
st.write("Enter two numbers and select an operation to perform a calculation.")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

operation = st.selectbox("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

if st.button("Calculate"):
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        st.success(f"Result: {result}")
    except Exception as e:
        st.error("An error occurred: " + str(e))