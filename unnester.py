class unnester():

    def nestfind(input_l, dim_search):

        rtn_lb = input_l

        for i in dim_search:

            rtn_lb = rtn_lb[i]

        return rtn_lb

    def end_(input_l, rtn_l, flag_l, dim_end):

        idx = -1

        adjust = 1

        for el in range(len(flag_l)):

            if el == 0:

                idx += len(unnester.nestfind(input_l, flag_l[el])) + flag_l[el][-1]

            elif len(flag_l[el]) == len(flag_l[el - 1]):

                idx += len(unnester.nestfind(input_l, flag_l[el])) + (flag_l[el][-1] - flag_l[el - 1][-1]) - 1

            elif len(flag_l[el]) > len(flag_l[el - 1]): 

                idx += len(unnester.nestfind(input_l, flag_l[el])) - (len(unnester.nestfind(input_l, flag_l[el - 1])) - flag_l[el][-1])

            else:

                len_flag_l_curr = len(flag_l[el])

                remain_idx = 0

                for i in range(1, len(flag_l[el - 1]) - len_flag_l_curr + 1):

                    remain_idx += len(unnester.nestfind(input_l, flag_l[el - 1][0:len(flag_l[el - 1]) - i])) - flag_l[el - 1][-i] - 1

                idx += len(unnester.nestfind(input_l, flag_l[el])) + (flag_l[el][-1] - flag_l[el - 1][len_flag_l_curr - 1]) - 1 + remain_idx 

            if len(flag_l[el]) == dim_end:

                cur = unnester.nestfind(input_l, flag_l[el])

                rtn_l[idx - len(cur) + adjust:idx + adjust] = [cur]

                adjust -= (len(cur) - 1)

        return rtn_l

    def ns(input_l, dim_end=1, strt_l=[], rtn_l=[], id_rec_main=0, wrk_l=None, flag_l=[]):

        wrk_l = input_l

        wrk_l_pre = []

        for i in range(len(strt_l)):

            wrk_l_pre.append(wrk_l)

            if type(wrk_l[strt_l[i]]) != list:

                wrk_l = [wrk_l[strt_l[i]]]

            else:

                wrk_l = wrk_l[strt_l[i]]

        list_status = False

        if len(strt_l) == 0:

            cnt = id_rec_main

        else:

            cnt = 0

        while list_status == False and cnt < len(wrk_l):

            if type(wrk_l[cnt]) == list:

                strt_l.append(cnt)

                list_status = True

            else:

                if len(strt_l) == 0:

                    id_rec_main += 1

                rtn_l.append(wrk_l[cnt])

            cnt += 1

        if list_status == False:

            if len(strt_l) > 0:

                if strt_l[-1] + 1 == len(wrk_l_pre[-1]):

                    if len(strt_l) == 1:

                        id_rec_main += 1

                        if id_rec_main == len(input_l):

                            return unnester.end_(input_l, rtn_l, flag_l, dim_end)

                    strt_l.pop()

                    wrk_l_pre.pop()

                if len(strt_l) > 0:

                    next_ = False

                    while next_ == False and len(strt_l) > 0:

                        if strt_l[-1] + 1 < len(wrk_l_pre[-1]):

                            if strt_l[-1] < len(wrk_l_pre[-1]) - 1:

                                stop = 0

                                while stop == 0:

                                    strt_l[-1] += 1

                                    if strt_l[-1] == len(wrk_l_pre[-1]) - 1:

                                        if len(strt_l) == 1:

                                            id_rec_main += 1

                                            strt_l.pop()

                                            if id_rec_main == len(input_l):

                                                return unnester.end_(input_l, rtn_l, flag_l, dim_end)

                                        stop = 1

                                    else:

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

                                if len(strt_l) == 1:

                                    id_rec_main += 1

                                    if id_rec_main == len(input_l):

                                        return unnester.end_(input_l, rtn_l, flag_l, dim_end) 

                            next_ = True

                        else:

                            strt_l.pop()

                            wrk_l_pre.pop() 

                            if len(strt_l) == 0:

                                id_rec_main += 1

                                if id_rec_main == len(input_l):

                                    return unnester.end_(input_l, rtn_l, flag_l, dim_end)

                else:

                    id_rec_main += 1

                    if id_rec_main == len(input_l):

                        return unnester.end_(input_l, rtn_l, flag_l, dim_end)

            elif id_rec_main == len(input_l):

                return unnester.end_(input_l, rtn_l, flag_l, dim_end) 

        if len(strt_l) <= dim_end and len(strt_l) > 0 and type(unnester.nestfind(input_l, strt_l)) == list:

            if len(flag_l) > 0:

                if strt_l != flag_l[-1]:

                    flag_l.append([ el for el in strt_l ])

            else:

                flag_l.append([ el for el in strt_l ])

        return unnester.ns(input_l, dim_end, strt_l, rtn_l, id_rec_main, wrk_l, flag_l)



