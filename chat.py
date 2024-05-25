import streamlit as st
import ollama

# initialize session state 
if "question" not in st.session_state:
    st.session_state.question = ""
if "verification_result" not in st.session_state:
    st.session_state.verification_result = ""

# function to generate a random question 
def generate_question(topic):
    if topic == "Geography":
        prompt = "Generate a random geography-related question."
    elif topic == "Health":
        prompt = "Generate a random health-related question."
    elif topic == "Sports":
        prompt = "Generate a random sports-related question."
    else:
        return "Invalid topic"
    
    try:
        response = ollama.chat(model='llama2', stream=False, messages=[{"role": "user", "content": prompt}])
        print("Response:", response) 
        
        if response and isinstance(response, dict) and "message" in response and "content" in response["message"]:
            question = response["message"]["content"]
            return question.strip()  # return the generated question
        else:
            return "Unable to generate a question at the moment."
    except Exception as e:
        print("Error:", e)
        return "Error occurred while generating the question."

# function to verify user answer
def verify_answer(question, answer):
    prompt = f"Question: {question}\nUser's answer: {answer}\nIs the user's answer correct? Please answer with 'Correct' or 'Incorrect' and provide a brief explanation."
    
    try:
        response = ollama.chat(model='llama2', stream=False, messages=[{"role": "user", "content": prompt}])
        print("Response:", response)  
        
        if response and isinstance(response, dict) and "message" in response and "content" in response["message"]:
            verification_message = response["message"]["content"]
            print("Verification Message:", verification_message)  
            
            if "correct" in verification_message.lower() and "incorrect" not in verification_message.lower():
                return "Correct!"
            elif "incorrect" in verification_message.lower():
                return "Incorrect."
            else:
                return "Unable to determine correctness. Please try again."
        else:
            return "Unable to verify the answer at the moment. Please try again later."
    except Exception as e:
        print("Error:", e)
        return "Error occurred while verifying the answer."

# main streamlit app
def main():
    st.title("Question and Answer System")

    # dropdown menu 
    topic = st.selectbox("Select a topic for the question", ["Geography", "Health", "Sports"])

    # button to generate question
    if st.button("Generate Question"):
        st.session_state.question = generate_question(topic)
        st.session_state.verification_result = ""  # Reset verification result

    # display generated question
    if st.session_state.question:
        st.write("Generated Question: ", st.session_state.question)

        # input box for user answer
        user_answer = st.text_input("Your Answer")

        # button to verify answer
        if st.button("Verify Answer"):
            if user_answer:
                # verify the answer
                st.session_state.verification_result = verify_answer(st.session_state.question, user_answer)
                st.write("Verification Result:", st.session_state.verification_result)
            else:
                st.write("Please provide an answer.")
    else:
        st.write("No question generated yet. Please select a topic and generate a question.")

if __name__ == "__main__":
    main()
