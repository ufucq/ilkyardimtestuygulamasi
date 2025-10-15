import streamlit as st
from quiz_data import tests

# Set page config
st.set_page_config(page_title="Test Uygulaması", layout="wide")

# --- STYLING ---
def local_css(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # Fail silently if CSS isn't present (helps when running quickly)
        pass

# --- SESSION STATE INITIALIZATION ---
def init_session_state():
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = []  # will be initialized when quiz starts
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
    if "test_selection" not in st.session_state:
        st.session_state.test_selection = list(tests.keys())[0]
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    # optional: store new selection when navigating between tests
    if "new_test_selection" not in st.session_state:
        st.session_state.new_test_selection = None

# --- FUNCTIONS ---
def show_question(questions):
    idx = st.session_state.current_question
    q = questions[idx]
    st.subheader(f"Soru {idx + 1}/{len(questions)}")
    st.write(q["question"])

    # determine pre-selected index if user already answered
    existing = None
    if idx < len(st.session_state.user_answers):
        existing = st.session_state.user_answers[idx]
    try:
        selected_index = q["options"].index(existing) if existing in q["options"] else 0
    except Exception:
        selected_index = 0

    user_answer = st.radio("Cevabınızı seçin:", q["options"], index=selected_index, key=f"q{idx}")
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
            # reset only the quiz-specific session items
            st.session_state.current_question = 0
            st.session_state.user_answers = [None] * len(questions)
            st.session_state.quiz_started = True
            st.session_state.quiz_submitted = False
            st.rerun()
    with col2:
        st.subheader("Başka bir test seçin")
        new_test = st.selectbox("Bir Test Seçin", list(tests.keys()), index=list(tests.keys()).index(st.session_state.test_selection))
        if st.button("Teste Git"):
            st.session_state.test_selection = new_test
            st.session_state.current_question = 0
            st.session_state.user_answers = [None] * len(tests[new_test]["questions"])
            st.session_state.quiz_started = True
            st.session_state.quiz_submitted = False
            st.rerun()

# --- MAIN APP ---
def main():
    init_session_state()

    if not st.session_state.authenticated:
        passphrase = st.text_input("Enter the passphrase:", type="password")
        if passphrase == "Ufuk Adamdır":
            st.session_state.authenticated = True
            st.rerun()
        elif passphrase != "":
            st.error("anahtar kelimeyi bilemediniz")
        return

    # authenticated
    local_css("style.css")

    if not st.session_state.quiz_started:
        # ensure selection exists
        st.title("İlk Yardım Eğitimi Test Uygulaması")
        st.session_state.test_selection = st.selectbox("Bir Test Seçin", list(tests.keys()), index=list(tests.keys()).index(st.session_state.test_selection))
        if st.button("Testi Başlat"):
            questions = tests[st.session_state.test_selection]["questions"]
            st.session_state.user_answers = [None] * len(questions)
            st.session_state.current_question = 0
            st.session_state.quiz_started = True
            st.session_state.quiz_submitted = False
            st.rerun()
        return

    # quiz started
    st.title("İlk Yar Test Uygulaması")
    st.header(st.session_state.test_selection)
    questions = tests[st.session_state.test_selection]["questions"]

    # show question or results
    if st.session_state.quiz_started and not st.session_state.quiz_submitted:
        user_answer = show_question(questions)

        col1, col2 = st.columns([1,1])
        with col1:
            if st.session_state.current_question > 0:
                if st.button("Önceki"):
                    # save current answer then move back
                    st.session_state.user_answers[st.session_state.current_question] = user_answer
                    st.session_state.current_question -= 1
                    st.rerun()
        with col2:
            if st.session_state.current_question < len(questions) - 1:
                if st.button("Sonraki"):
                    st.session_state.user_answers[st.session_state.current_question] = user_answer
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("Sonuçları Göster"):
                    st.session_state.user_answers[st.session_state.current_question] = user_answer
                    st.session_state.quiz_submitted = True
                    st.rerun()

        # progress bar
        progress_pct = (st.session_state.current_question + 1) / len(questions)
        st.progress(progress_pct)

        # Add "Testi Bitir" button below the progress bar
        if st.button("Testi Bitir"):
            st.session_state.quiz_started = False
            st.session_state.quiz_submitted = False
            st.session_state.current_question = 0
            st.session_state.user_answers = []
            st.rerun()

    if st.session_state.quiz_submitted:
        show_results(questions)

if __name__ == "__main__":
    main()
