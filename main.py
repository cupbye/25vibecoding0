'''
import streamlit as st
st.title('나의 첫 streamlit app')
st.write('hello streamlit!!!')
'''

import streamlit as st

st.title("MBTI 성격유형 검사")

st.write("아래 문항에 답하여 당신의 MBTI 유형을 알아보세요!")

questions = {
    "EI": [
        ("나는 사교적인 편이다.", "E"),
        ("나는 혼자 있는 것이 더 편하다.", "I"),
    ],
    "SN": [
        ("나는 실제적인 정보를 선호한다.", "S"),
        ("나는 직관적으로 이해하는 편이다.", "N"),
    ],
    "TF": [
        ("나는 결정을 내릴 때 논리와 이성을 중시한다.", "T"),
        ("나는 감정과 상황을 고려한다.", "F"),
    ],
    "JP": [
        ("나는 계획을 세우고 따르는 것을 좋아한다.", "J"),
        ("나는 즉흥적인 행동을 더 선호한다.", "P"),
    ],
}

mbti_scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

for category, q_list in questions.items():
    for question, trait in q_list:
        response = st.radio(question, ["그렇다", "아니다"], key=question)
        if response == "그렇다":
            mbti_scores[trait] += 1

# 유형 계산
def get_mbti(scores):
    result = ""
    result += "E" if scores["E"] >= scores["I"] else "I"
    result += "S" if scores["S"] >= scores["N"] else "N"
    result += "T" if scores["T"] >= scores["F"] else "F"
    result += "J" if scores["J"] >= scores["P"] else "P"
    return result

if st.button("결과 확인하기"):
    mbti_type = get_mbti(mbti_scores)
    st.subheader(f"당신의 MBTI 유형은 **{mbti_type}** 입니다!")
    st.write("간단한 설명을 추가할 수도 있어요 :)")


