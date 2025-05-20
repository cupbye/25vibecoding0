'''
import streamlit as st
st.title('나의 첫 streamlit app')
st.write('hello streamlit!!!')
'''

import streamlit as st

# MBTI 질문 및 선택지
# 각 질문은 (질문 내용, 선택지1에 해당하는 유형, 선택지2에 해당하는 유형) 형태로 구성
questions_data = {
    "EI": [
        ("혼자 있을 때 에너지를 얻는다.", "I", "E"),
        ("여러 사람과 함께 있을 때 에너지를 얻는다.", "E", "I"),
        ("글쓰기를 통해 자신을 표현하는 것이 더 편하다.", "I", "E"),
        ("말로 직접 소통하는 것을 선호한다.", "E", "I"),
    ],
    "SN": [
        ("실제 경험과 구체적인 사실에 더 집중한다.", "S", "N"),
        ("미래의 가능성과 아이디어를 더 중요하게 생각한다.", "N", "S"),
        ("현재에 충실하며, 실용적인 것을 선호한다.", "S", "N"),
        ("상상력이 풍부하며, 비유적인 표현을 즐겨 사용한다.", "N", "S"),
    ],
    "TF": [
        ("결정을 내릴 때 논리와 분석을 중요하게 생각한다.", "T", "F"),
        ("결정을 내릴 때 사람들과의 관계와 감정을 고려한다.", "F", "T"),
        ("객관적인 사실과 원칙을 바탕으로 판단한다.", "T", "F"),
        ("타인의 감정에 공감하고 조화를 중요하게 생각한다.", "F", "T"),
    ],
    "JP": [
        ("계획을 세우고 체계적으로 일을 진행하는 것을 선호한다.", "J", "P"),
        ("상황에 따라 유연하게 대처하고 즉흥적인 것을 즐긴다.", "P", "J"),
        ("마감 기한을 중요하게 생각하고 미리 준비한다.", "J", "P"),
        ("자유로운 환경에서 일하는 것을 선호하며, 변화에 잘 적응한다.", "P", "J"),
    ]
}

# MBTI 유형별 설명 (간단하게 예시로 작성)
mbti_descriptions = {
    "ISTJ": "책임감이 강하고 현실적인 유형입니다. 신중하고 질서정연하며, 맡은 일에 최선을 다합니다.",
    "ISFJ": "헌신적이고 성실하며, 타인에 대한 배려심이 깊습니다. 안정감을 중요하게 생각합니다.",
    "INFJ": "통찰력이 뛰어나고 이상주의적인 성향을 가집니다. 타인의 성장을 돕는 데 관심이 많습니다.",
    "INTJ": "독립적이고 분석적이며, 비전을 가지고 있습니다. 전략적인 사고를 하며 목표를 추구합니다.",
    "ISTP": "논리적이고 실용적이며, 문제 해결 능력이 뛰어납니다. 현재를 즐기는 경향이 있습니다.",
    "ISFP": "온화하고 겸손하며, 현재의 삶을 즐깁니다. 예술적인 감각이 뛰어나고 관용적입니다.",
    "INFP": "이상주의적이고 창의적이며, 자신의 가치관을 중요하게 생각합니다. 타인에게 공감하는 능력이 뛰어납니다.",
    "INTP": "지적 호기심이 많고 논리적이며, 분석적인 사고를 합니다. 독립적이고 독창적인 아이디어를 추구합니다.",
    "ESTP": "활동적이고 현실적이며, 문제 해결에 능숙합니다. 새로운 경험을 즐기고 적응력이 뛰어납니다.",
    "ESFP": "사교적이고 활동적이며, 현재를 즐기는 낙천적인 유형입니다. 타인과의 관계를 중요하게 생각합니다.",
    "ENFP": "열정적이고 상상력이 풍부하며, 새로운 가능성을 추구합니다. 사람들과 잘 어울리고 변화를 즐깁니다.",
    "ENTP": "독창적이고 논리적이며, 새로운 아이디어를 탐구하는 것을 좋아합니다. 토론을 즐기고 도전을 두려워하지 않습니다.",
    "ESTJ": "체계적이고 현실적이며, 리더십이 뛰어납니다. 목표 지향적이며 결단력이 있습니다.",
    "ESFJ": "사교적이고 친절하며, 타인을 돕는 것을 좋아합니다. 조화로운 관계를 중요하게 생각합니다.",
    "ENFJ": "열정적이고 책임감이 강하며, 타인의 성장을 돕는 데 능숙합니다. 사람들에게 영감을 주는 리더입니다.",
    "ENTJ": "통솔력이 있고 결단력이 있으며, 장기적인 비전을 가지고 있습니다. 목표 달성을 위해 노력합니다."
}

def calculate_mbti(answers):
    """
    사용자의 답변을 바탕으로 MBTI 유형을 계산합니다.
    """
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for dimension_answers in answers.values():
        for answer in dimension_answers:
            scores[answer] += 1

    result = ""
    result += "E" if scores["E"] >= scores["I"] else "I"
    result += "S" if scores["S"] >= scores["N"] else "N"
    result += "T" if scores["T"] >= scores["F"] else "F"
    result += "J" if scores["J"] >= scores["P"] else "P"
    return result

def main():
    st.set_page_config(page_title="MBTI 성격 유형 검사", layout="wide")
    st.title("간단 MBTI 성격 유형 검사")
    st.write("각 질문에 대해 자신에게 더 가깝다고 생각되는 답변을 선택해주세요.")

    user_answers = {}
    all_questions_answered = True

    for dimension, qs in questions_data.items():
        st.subheader(f"--- {dimension[0]}/{dimension[1]} 지표 ---")
        dimension_answers = []
        for i, (q_text, type1, type2) in enumerate(qs):
            # 고유한 키 생성을 위해 dimension과 질문 인덱스 사용
            key = f"{dimension}_{i}"
            # st.radio의 옵션은 (표시될 텍스트, 반환될 값)의 튜플 형태를 가질 수 없으므로,
            # 선택 시 반환될 값을 type1 또는 type2로 직접 지정
            options = [f"A. {q_text.split(' ')[0]} ...", f"B. {q_text.split(' ')[0]} ..."] # 간략한 옵션 표시
            
            # 라디오 버튼의 선택지를 텍스트로 하고, 선택된 텍스트를 기반으로 유형을 결정
            # 사용자에게는 질문의 핵심 내용과 선택지 A/B만 보여주도록 수정
            question_prompt = f"**{i+1}. {q_text}**"
            
            # 선택지 구성 방식 변경: 사용자가 직접 선택지를 읽고 A/B를 고르도록 안내
            # 실제 질문은 위에 표시하고, 선택은 A/B로만 받도록 간소화
            # 이 방식 대신, 각 선택지를 명확히 표시하는 것이 사용자 경험에 더 좋습니다.
            # 아래는 각 선택지를 버튼의 레이블로 사용하는 방식입니다.

            option_a_text = f"선택 1 ({type1})"
            option_b_text = f"선택 2 ({type2})"

            # 질문마다 고유한 키를 부여해야 함
            answer_choice = st.radio(
                question_prompt,
                (option_a_text, option_b_text),
                key=key,
                horizontal=True, # 가로 정렬
                index=None # 기본 선택 없음
            )

            if answer_choice == option_a_text:
                dimension_answers.append(type1)
            elif answer_choice == option_b_text:
                dimension_answers.append(type2)
            else:
                all_questions_answered = False # 하나라도 답변 안하면 False

        user_answers[dimension] = dimension_answers

    st.markdown("---")

    if st.button("결과 보기", disabled=not all_questions_answered):
        if not all_questions_answered:
            st.warning("모든 질문에 답변해주세요.")
        else:
            # 답변 통합 (각 지표별로 E,I,S,N,T,F,J,P 중 어떤 것을 선택했는지 리스트로 만듦)
            flat_answers = {"EI": [], "SN": [], "TF": [], "JP": []}
            for dim_key, dim_ans_list in user_answers.items():
                for ans_val in dim_ans_list:
                    flat_answers[dim_key].append(ans_val)


            final_mbti_type = calculate_mbti(flat_answers)
            st.subheader(f"🎉 당신의 MBTI 유형은: {final_mbti_type} 🎉")
            st.markdown(f"**{final_mbti_type} 유형 설명:**")
            st.info(mbti_descriptions.get(final_mbti_type, "결과 설명을 찾을 수 없습니다."))
            st.balloons()
    elif not all_questions_answered:
        st.info("모든 질문에 답변 후 '결과 보기' 버튼을 눌러주세요.")


if __name__ == "__main__":
    main()
