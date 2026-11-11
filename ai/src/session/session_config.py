# 설거지 세션 (water + dishes, microwave 후처리 분기)
DISHWASHING_PARAMS = {
    "T2": 2,    # water -> dishes 최대 허용 gap (분)
    "T3": 5,    # 재감지 허용 gap / 세션 종료 timeout (분)
    "L": 60,    # microwave 선행 확인 lookback (분)
}

# 식사 세션 (cooking/microwave -> dishes, 설거지 트리거로 종료)
MEAL_PARAMS = {
    "T1": 10,   # 조리(microwave) 재감지 허용 gap (분)
    "T2": 20,   # CONFIRMED 이후 무감지 timeout (분) - 설거지 트리거보다 먼저 도달하면 이걸로 종료
}


# 세탁 세션
LAUNDRY_PARAMS = {
    "T1": 5,    # 세탁 재감지 gap / 종료 timeout
    "T2": 20,   # 세탁 최소 지속시간
}

# 청소 세션
CLEANING_PARAMS = {
    "T1": 5,    # 청소 재감지 gap / 종료 timeout (분)
    "T2": 5,    # 청소 최소 지속시간 (분)
}

# 소리 증거 판단 (세탁/청소처럼 단일 소리가 지속되는 세션에 적용)
# analyze_top2.py 시뮬레이션 근거: start 0.6 / keep 0.4 에서 세탁 TP 1.0, 오확정 0
EVIDENCE_PARAMS = {
    "window_sec": 60,   # 확률 평균을 낼 시간 창 (초)
    "tau_start": 0.6,   # 세션을 새로 열 때 필요한 평균 확률
    "tau_keep": 0.4,    # 열린 세션을 유지할 때 필요한 평균 확률
}
