import streamlit as st
from quiz_data import tests

# Set page config
st.set_page_config(page_title="Test Uygulaması", layout="wide")


# --- STYLING ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
def init_session_state():
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = []
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

# --- FUNCTIONS ---
def show_question(questions):
    q = questions[st.session_state.current_question]
    st.subheader(f"Soru {st.session_state.current_question + 1}/{len(questions)}")
    st.write(q["question"])
    user_answer = st.radio("Cevabınızı seçin:", q["options"], key=f"q{st.session_state.current_question}")
    return user_answer

def show_results(questions):
    st.subheader("Sonuçlar")
    score = 0
    wrong_answers = []
    for i, q in enumerate(questions):
        user_answer = st.session_state.user_answers[i]
        correct_answer = q['answer']
        
        if user_answer == correct_answer:
            score += 1
        else:
            wrong_answers.append({
                "question_number": i + 1,
                "question": q["question"],
                "your_answer": user_answer,
                "correct_answer": correct_answer,
                "explanation": q.get("explanation"),
                "wrong_explanations": q.get("wrong_explanations", {})
            })

    st.subheader(f"Toplam puanınız {score}/{len(questions)}")

    if not wrong_answers:
        st.balloons()
        st.success("Tebrikler! Tüm soruları doğru cevapladınız.")

    if wrong_answers:
        st.subheader("Yanlış cevaplarınızı gözden geçirin:")
        for wrong in wrong_answers:
            with st.container():
                st.markdown("---")
                st.error(f"Soru {wrong['question_number']}: {wrong['question']}")
                st.write(f"Sizin cevabınız: {wrong['your_answer']}")
                st.write(f"Doğru cevap: {wrong['correct_answer']}")
                if wrong['explanation']:
                    st.info(f"Açıklama: {wrong['explanation']}")
                if wrong['your_answer'] in wrong['wrong_explanations']:
                    st.warning(f"Cevabınız neden yanlış: {wrong['wrong_explanations'][wrong['your_answer']]}")

    st.markdown("***")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Bu testi tekrarla")
        if st.button("Tekrarla"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.user_answers = []
            st.session_state.quiz_started = True
            st.session_state.quiz_submitted = False
            st.rerun()
    with col2:
        st.subheader("Başka bir test seçin")
        new_test = st.selectbox("Bir Test Seçin", list(tests.keys()))
        if st.button("Teste Git"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.user_answers = []
            st.session_state.quiz_started = True
            st.session_state.quiz_submitted = False
            st.session_state.new_test_selection = new_test
            st.rerun()

# --- MAIN APP ---
def main():
    local_css("style.css")
    init_session_state()

    if "new_test_selection" in st.session_state:
        st.session_state.test_selection = st.session_state.new_test_selection
        del st.session_state.new_test_selection

    st.title("İlk Yar Test Uygulaması")

    if "test_selection" not in st.session_state:
        st.session_state.test_selection = list(tests.keys())[0]

    if not st.session_state.quiz_started:
        test_selection = st.selectbox("Bir Test Seçin", list(tests.keys()), key="test_selection")
        if st.button("Testi Başlat"):
            st.session_state.quiz_started = True
            st.rerun()
    else:
        st.header(st.session_state.test_selection)

    if st.session_state.quiz_started:
        questions = tests[st.session_state.test_selection]["questions"]

        if st.session_state.quiz_started and not st.session_state.quiz_submitted:
            user_answer = show_question(questions)

            col1, col2 = st.columns([1,1])

            with col1:
                if st.session_state.current_question > 0:
                    if st.button("Önceki"):
                        st.session_state.user_answers.pop()
                        st.session_state.current_question -= 1
                        st.rerun()
            with col2:
                if st.session_state.current_question < len(questions) - 1:
                    if st.button("Sonraki"):
                        st.session_state.user_answers.append(user_answer)
                        st.session_state.current_question += 1
                        st.rerun()
                else:
                    if st.button("Sonuçları Göster"):
                        st.session_state.user_answers.append(user_answer)
                        st.session_state.quiz_submitted = True
                        st.rerun()
            st.progress((st.session_state.current_question + 1) / len(questions))

        if st.session_state.quiz_submitted:
            show_results(questions)

if __name__ == "__main__":
    main()