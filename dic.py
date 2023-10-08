version_list = [[1, 21, 25],
                [2, 25, 47],
                [3, 29, 77],
                [4, 3, 114],
                [5, 37, 154],
                [6, 41, 195],
                [7, 45, 224],
                [8, 49, 279],
                [9, 53, 335],
                [10, 57, 395],
                [11, 61, 468],
                [12, 65, 535],
                [13, 69, 619],
                [14, 73, 667],
                [15, 77, 758],
                [16, 81, 854],
                [17, 85, 938],
                [18, 89, 1046],
                [19, 93, 1153],
                [20, 97, 1249],
                [21, 101, 1352],
                [22, 105, 1460],
                [23, 109, 1588],
                [24, 113, 1704],
                [25, 117, 1853],
                [26, 121, 1990],
                [27, 125, 2132],
                [28, 129, 2223],
                [29, 133, 2369],
                [30, 137, 2520],
                [31, 141, 2677],
                [32, 145, 2840],
                [33, 149, 3009],
                [34, 153, 3183],
                [35, 157, 3351],
                [36, 161, 3537],
                [37, 165, 3729],
                [38, 169, 3927],
                [39, 173, 4087],
                [40, 177, 4296]]

v_dict_list = []

for v in version_list:
    v_dict = {
        'version': v[0],
        'width': v[1],
        'maxChar': v[2],
    }
    v_dict_list.append(v_dict)

print(v_dict_list)

[{'version': 1, 'width': 21, 'maxChar': 25}, {'version': 2, 'width': 25, 'maxChar': 47}, {'version': 3, 'width': 29, 'maxChar': 77}, {'version': 4, 'width': 3, 'maxChar': 114}, {'version': 5, 'width': 37, 'maxChar': 154}, {'version': 6, 'width': 41, 'maxChar': 195}, {'version': 7, 'width': 45, 'maxChar': 224}, {'version': 8, 'width': 49, 'maxChar': 279}, {'version': 9, 'width': 53, 'maxChar': 335}, {'version': 10, 'width': 57, 'maxChar': 395}, {'version': 11, 'width': 61, 'maxChar': 468}, {'version': 12, 'width': 65, 'maxChar': 535}, {'version': 13, 'width': 69, 'maxChar': 619}, {'version': 14, 'width': 73, 'maxChar': 667}, {'version': 15, 'width': 77, 'maxChar': 758}, {'version': 16, 'width': 81, 'maxChar': 854}, {'version': 17, 'width': 85, 'maxChar': 938}, {'version': 18, 'width': 89, 'maxChar': 1046}, {'version': 19, 'width': 93, 'maxChar': 1153}, {'version': 20, 'width': 97, 'maxChar': 1249}, {'version': 21,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'width': 101, 'maxChar': 1352}, {'version': 22, 'width': 105, 'maxChar': 1460}, {'version': 23, 'width': 109, 'maxChar': 1588}, {'version': 24, 'width': 113, 'maxChar': 1704}, {'version': 25, 'width': 117, 'maxChar': 1853}, {'version': 26, 'width': 121, 'maxChar': 1990}, {'version': 27, 'width': 125, 'maxChar': 2132}, {'version': 28, 'width': 129, 'maxChar': 2223}, {'version': 29, 'width': 133, 'maxChar': 2369}, {'version': 30, 'width': 137, 'maxChar': 2520}, {'version': 31, 'width': 141, 'maxChar': 2677}, {'version': 32, 'width': 145, 'maxChar': 2840}, {'version': 33, 'width': 149, 'maxChar': 3009}, {'version': 34, 'width': 153, 'maxChar': 3183}, {'version': 35, 'width': 157, 'maxChar': 3351}, {'version': 36, 'width': 161, 'maxChar': 3537}, {'version': 37, 'width': 165, 'maxChar': 3729}, {'version': 38, 'width': 169, 'maxChar': 3927}, {'version': 39, 'width': 173, 'maxChar': 4087}, {'version': 40, 'width': 177, 'maxChar': 4296}]
