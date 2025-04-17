import streamlit as st

st.title("🧠 GPT용 프롬프트 자동 생성기")
st.write("아래 5가지 질문에 답하면, GPT에게 보낼 파이썬 코드 생성 프롬프트가 완성됩니다!")

# 사용자 입력
problem = st.text_area("문제 상황을 입력하세요", height=80)
decomposition = st.text_area("[문제분해] 문제를 어떻게 나눌 수 있을까요?", height=80)
pattern = st.text_area("[패턴인식] 반복되는 패턴이 있나요?", height=80)
abstraction = st.text_area("[추상화] 핵심 변수와 수식은 무엇인가요?", height=80)
algorithm = st.text_area("[알고리즘] 해결을 위한 알고리즘은 어떤 순서인가요?", height=80)

if st.button("🧩 프롬프트 생성하기"):
    prompt = f"""
문제: {problem}
문제 분해: {decomposition}
패턴 인식: {pattern}
추상화: {abstraction}
알고리즘: {algorithm}

위 내용을 바탕으로 초보자가 이해할 수 있는 파이썬 프로그램을 작성해줘.
입력 → 처리 → 출력의 구조를 따르고, 주석을 포함해서 작성해줘.
"""
    st.subheader("✅ 아래 문장을 복사해서 GPT에 붙여넣으세요!")
    st.code(prompt, language="markdown")
    st.success("✂️ Ctrl+C 또는 ⌘+C 로 복사해서 ChatGPT에 붙여넣어 보세요!")
