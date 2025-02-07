T = 10

for test_case in range(1, 1 + T):
    dump_num = int(input())
    box_height_list = list(map(int, input().split()))
    max_height = 0
    min_height = 0

    while dump_num > 0:
        # 맥스값과 민값을 초기화한다.
        max_height = box_height_list[0]
        max_idx = 0
        min_height = box_height_list[0]
        min_idx = 0
        # 가장 높은 박스와 낮은 박스의 인덱스 값을 가져온다.
        for indx in range(len(box_height_list)):
            if max_height < box_height_list[indx]:
                max_height = box_height_list[indx]
                max_idx = indx
            if min_height > box_height_list[indx]:
                min_height = box_height_list[indx]
                min_idx = indx
        # 높은 박스 하나를 줄이고 낮은 박스 하나를 높인다.
        box_height_list[max_idx] -= 1
        box_height_list[min_idx] += 1

        # 마지막에 max_height 나 min_height 가 변경되었으면 바꾼다.
        if dump_num == 1:
            new_max_height = 0
            new_min_height = 101
            for indx in range(len(box_height_list)):
                if new_max_height < box_height_list[indx]:
                    new_max_height = box_height_list[indx]
                if new_min_height > box_height_list[indx]:
                    new_min_height = box_height_list[indx]
            max_height = new_max_height
            min_height = new_min_height

        dump_num -= 1
    # 덤프 횟수만큼 반복한다.

    print(f'#{test_case} {max_height-min_height}')
    # 높은 박스와 낮은 박스의 차를 구해서 출력한다.
