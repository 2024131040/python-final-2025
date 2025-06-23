def SmoothingMethod(l, k):
    """
    리스트에 슬라이딩 윈도우 방식의 평활화(smoothing)를 적용합니다.
    각 값은 자신과 양 옆의 이웃값 평균으로 대체되며,
    가장자리는 경계 값을 반복하여 확장합니다.

    매개변수:
        l: 실수로 구성된 1차원 리스트
        k: 홀수 크기의 윈도우 크기 (예: 3, 5, 7 등)

    반환값:
        소수 첫째 자리까지 반올림된 평활화된 값들의 리스트
    """
    smoothed_list = []
    radius = (k - 1) // 2
    for i in range(len(l)):
        window_sum = 0
        for j in range(i - radius, i + radius + 1):
            if j < 0:
                window_sum += l[0]
            elif j >= len(l):
                window_sum += l[-1]
            else:
                window_sum += l[j]
        average = round(window_sum / k, 1)
        smoothed_list.append(average)
    return smoothed_list
