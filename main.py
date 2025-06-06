# -*- coding: utf-8 -*-

# MBTI 유형별 가상 데이터 정의 (딕셔너리 형태)
# 이 데이터는 실제 연구가 아닌, 재미를 위해 만들어진 가상의 정보입니다.
mbti_data = {
    'INTJ': {
        'emoji': '🐲',
        'score': 96,
        'strengths': '논리적 비판, 비문학 독해, 구조 분석에 강점을 보입니다.'
    },
    'INTP': {
        'emoji': '🦉',
        'score': 94,
        'strengths': '복잡한 이론을 이해하고 추론하며, 독창적인 해석을 잘합니다.'
    },
    'ENTJ': {
        'emoji': '🦅',
        'score': 95,
        'strengths': '토론과 발표에 능하며, 글의 핵심 주장을 빠르게 파악합니다.'
    },
    'ENTP': {
        'emoji': '🦄',
        'score': 93,
        'strengths': '다양한 관점을 제시하고, 창의적인 문제 해결 능력이 뛰어납니다.'
    },
    'INFJ': {
        'emoji': '🐋',
        'score': 95,
        'strengths': '문학 작품에 깊이 공감하며, 인물의 내면 심리 분석에 탁월합니다.'
    },
    'INFP': {
        'emoji': '🌸',
        'score': 93,
        'strengths': '시적 표현을 잘 이해하고, 감성적이고 깊이 있는 글쓰기를 잘합니다.'
    },
    'ENFJ': {
        'emoji': '☀️',
        'score': 92,
        'strengths': '화법과 작문에 능숙하며, 타인을 설득하고 공감을 이끌어내는 능력이 좋습니다.'
    },
    'ENFP': {
        'emoji': '🦋',
        'score': 91,
        'strengths': '풍부한 상상력을 바탕으로 자유로운 형식의 글쓰기를 즐깁니다.'
    },
    'ISTJ': {
        'emoji': '🧱',
        'score': 94,
        'strengths': '문법, 어문 규정을 꼼꼼하게 학습하고 체계적으로 내용을 정리합니다.'
    },
    'ISFJ': {
        'emoji': 'HS', # 이모지가 없어서 텍스트로 대체
        'score': 90,
        'strengths': '세부 내용을 잘 기억하고, 안정적이고 성실한 학습 태도를 가집니다.'
    },
    'ESTJ': {
        'emoji': '🏛️',
        'score': 92,
        'strengths': '명확한 근거를 바탕으로 실용적인 글을 쓰는 것을 선호합니다.'
    },
    'ESFJ': {
        'emoji': '🤝',
        'score': 89,
        'strengths': '자신의 경험을 바탕으로 한 작문에 능하고, 의사소통 능력이 좋습니다.'
    },
    'ISTP': {
        'emoji': '🔧',
        'score': 88,
        'strengths': '문제 해결 중심으로 독해하며, 언어의 기술적 측면을 분석하는 것을 즐깁니다.'
    },
    'ISFP': {
        'emoji': '🎨',
        'score': 87,
        'strengths': '작품의 예술성을 감상하고, 미적 감수성을 바탕으로 주관적 감상을 잘 표현합니다.'
    },
    'ESTP': {
        'emoji': '⚡️',
        'score': 86,
        'strengths': '실전 문제 풀이에 강하고, 토론 등에서 순발력과 임기응변이 뛰어납니다.'
    },
    'ESFP': {
        'emoji': '🎤',
        'score': 85,
        'strengths': '생생한 경험을 바탕으로 표현력이 좋으며, 대중적인 글쓰기에 재능이 있습니다.'
    }
}

def start_analyzer():
    """MBTI 분석기를 시작하는 메인 함수"""
    print("=" * 50)
    print("👑 MBTI 유형별 고3 국어 가상 성취도 분석기 👑")
    print("=" * 50)
    print("🚨 주의: 이 결과는 재미를 위한 가상 데이터입니다!")
    
    # 선택 가능한 MBTI 목록 보여주기
    print("\n[선택 가능한 MBTI 유형]")
    # 8개씩 두 줄로 나눠서 출력
    types = list(mbti_data.keys())
    print(" | ".join(types[:8]))
    print(" | ".join(types[8:]))
    print("\n(프로그램을 종료하려면 '종료' 또는 'q'를 입력하세요)")

    while True:
        # 사용자로부터 MBTI 유형 입력받기
        user_input = input("\n> 분석하고 싶은 MBTI 유형을 입력하세요: ").strip().upper()

        # 종료 조건 확인
        if user_input in ['종료', 'Q']:
            print("\n프로그램을 종료합니다. 이용해주셔서 감사합니다! 👋")
            break
        
        # 입력된 유형이 데이터에 있는지 확인
        if user_input in mbti_data:
            info = mbti_data[user_input]
            
            # 결과 출력
            print("\n" + "─" * 25)
            print(f"    {user_input} {info['emoji']} 유형 분석 결과")
            print("─" * 25)
            print(f"  [가상 평균 점수] : {info['score']}점")
            print(f"  [국어 영역 강점] : {info['strengths']}")
            print("─" * 25)
        else:
            # 잘못된 유형을 입력했을 때 안내 메시지
            print(f"\n[오류] '{user_input}'은(는) 유효한 MBTI 유형이 아닙니다. 다시 입력해주세요.")

# 프로그램 실행
if __name__ == "__main__":
    start_analyzer()
