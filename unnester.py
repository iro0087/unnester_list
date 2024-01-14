class unnester():

    def nestfind(input_l, dim_search):

        rtn_lb = input_l

        for i in dim_search:

            rtn_lb = rtn_lb[i]

        return rtn_lb

    def end_(input_l, rtn_l, flag_l, dim_end):

        print("end_", rtn_l)

        print(flag_l)

        idx = -1

        adjust = 1

        for el in range(len(flag_l)):

            print(flag_l[el])

            if el == 0:

                print("zero", unnester.nestfind(input_l, flag_l[el]))

                idx += len(unnester.nestfind(input_l, flag_l[el])) + flag_l[el][-1]

            elif len(flag_l[el]) == len(flag_l[el - 1]):

                print("one", unnester.nestfind(input_l, flag_l[el]))

                idx += len(unnester.nestfind(input_l, flag_l[el])) + (flag_l[el][-1] - flag_l[el - 1][-1]) - 1

            elif len(flag_l[el]) > len(flag_l[el - 1]): 

                print("two")

                idx += len(unnester.nestfind(input_l, flag_l[el])) - (len(unnester.nestfind(input_l, flag_l[el - 1])) - flag_l[el][-1])

            else:

                print("three")

                len_flag_l_curr = len(flag_l[el])

                remain_idx = 0

                for i in range(1, len(flag_l[el - 1]) - len_flag_l_curr + 1):

                    remain_idx += len(unnester.nestfind(input_l, flag_l[el - 1][0:len(flag_l[el - 1]) - i])) - flag_l[el - 1][-i] - 1

                print("remain_idx: ", remain_idx)

                idx += len(unnester.nestfind(input_l, flag_l[el])) + (flag_l[el][-1] - flag_l[el - 1][len_flag_l_curr - 1]) - 1 + remain_idx 

            print("idx: ", idx, el)

            if len(flag_l[el]) == dim_end:

                cur = unnester.nestfind(input_l, flag_l[el])

                print("cur: ", cur, rtn_l[idx - len(cur):idx], idx)

                rtn_l[idx - len(cur) + adjust:idx + adjust] = [cur]

                adjust -= (len(cur) - 1)

        return rtn_l

    def ns(input_l, dim_end=1, strt_l=[], rtn_l=[], id_rec_main=0, wrk_l=None, flag_l=[]):

        wrk_l = input_l

        wrk_l_pre = []

        print("strt_l1: ", strt_l)

        print("id_rec_main depart: ", id_rec_main)

        for i in range(len(strt_l)):

            print("ok", strt_l[i])

            wrk_l_pre.append(wrk_l)

            if type(wrk_l[strt_l[i]]) != list:

                print(wrk_l[strt_l[i]])

                wrk_l = [wrk_l[strt_l[i]]]

            else:

                wrk_l = wrk_l[strt_l[i]]

        print("wrk_l1: ", wrk_l)

        print("wrk_l_pre: ", wrk_l_pre)

        list_status = False

        if len(strt_l) == 0:

            cnt = id_rec_main

        else:

            cnt = 0

        print("cnt: ", cnt)

        while list_status == False and cnt < len(wrk_l):

            if type(wrk_l[cnt]) == list:

                print("detected", dim_end)

                strt_l.append(cnt)

                list_status = True

            else:

                if len(strt_l) == 0:

                    id_rec_main += 1

                rtn_l.append(wrk_l[cnt])

            cnt += 1

        print("id_rec_main: ", id_rec_main)

        print("rtn_l: ", rtn_l)

        if list_status == False:

            if len(strt_l) > 0:

                print("ici", len(wrk_l_pre[-1]))

                if strt_l[-1] + 1 == len(wrk_l_pre[-1]):

                    print("sup")

                    if len(strt_l) == 1:

                        id_rec_main += 1

                        if id_rec_main == len(input_l):

                            return unnester.end_(input_l, rtn_l, flag_l, dim_end)

                    strt_l.pop()

                    wrk_l_pre.pop()

                if len(strt_l) > 0:

                    next_ = False

                    print("oup")

                    print(strt_l)

                    print(wrk_l_pre[-1])

                    while next_ == False and len(strt_l) > 0:

                        print("len: ", len(wrk_l_pre[-1]), "strt_l: ", strt_l[-1], strt_l)

                        if strt_l[-1] + 1 < len(wrk_l_pre[-1]):

                            print("nextt", strt_l[-1], wrk_l_pre[-1])

                            if strt_l[-1] < len(wrk_l_pre[-1]) - 1:

                                stop = 0

                                while stop == 0:

                                    strt_l[-1] += 1

                                    if strt_l[-1] == len(wrk_l_pre[-1]) - 1:

                                        print("next2b")

                                        if len(strt_l) == 1:

                                            id_rec_main += 1

                                            strt_l.pop()

                                            print("id_rec_main: ", id_rec_main)

                                            if id_rec_main == len(input_l):

                                                return unnester.end_(input_l, rtn_l, flag_l, dim_end)

                                        stop = 1

                                    else:

                                        print("next2", dim_end)

                                        if  type(wrk_l_pre[-1][strt_l[-1]]) == list:

                                            stop = 1

                                        else:

                                            rtn_l.append(wrk_l_pre[-1][strt_l[-1]])

                                        if len(strt_l) == 1:

                                            id_rec_main += 1

                                            if id_rec_main == len(input_l):

                                                return unnester.end_(input_l, rtn_l, flag_l, dim_end)
                            else:

                                strt_l[-1] += 1

                                print("ff")

                                if len(strt_l) == 1:

                                    id_rec_main += 1

                                    if id_rec_main == len(input_l):

                                        return unnester.end_(input_l, rtn_l, flag_l, dim_end) 

                            next_ = True

                        else:

                            print("oco")

                            strt_l.pop()

                            wrk_l_pre.pop() 

                            if len(strt_l) == 0:

                                print("ici2")

                                id_rec_main += 1

                                if id_rec_main == len(input_l):

                                    return unnester.end_(input_l, rtn_l, flag_l, dim_end)

                else:

                    id_rec_main += 1

                    print("ici id_rec_main: ", id_rec_main, rtn_l)

                    if id_rec_main == len(input_l):

                        return unnester.end_(input_l, rtn_l, flag_l, dim_end)

            elif id_rec_main == len(input_l):

                print("quoi", rtn_l)

                return unnester.end_(input_l, rtn_l, flag_l, dim_end) 

        if len(strt_l) <= dim_end and len(strt_l) > 0 and type(unnester.nestfind(input_l, strt_l)) == list:

            if len(flag_l) > 0:

                if strt_l != flag_l[-1]:

                    print("append: ", strt_l)

                    flag_l.append([ el for el in strt_l ])

            else:

                print("append: ", strt_l)

                flag_l.append([ el for el in strt_l ])

        print("strt_lf: ", strt_l)

        print("rtn_lf: ", rtn_l)

        print("id_rec_mainf: ", id_rec_main)

        print("")

        print("#######################")

        print("")

        return unnester.ns(input_l, dim_end, strt_l, rtn_l, id_rec_main, wrk_l, flag_l)

x = unnester.ns([1, [5, [[2], 4, [23, 3, 3]]], 2, 3334, [4, [55, 56], 7, [77, [66, 67], 78], 2, [33, 5]], 3, [5, 6], 4], 3)

print("")

print("return: ", x)

