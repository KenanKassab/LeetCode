class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = sorted(events, key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        Active = {"id" + str(id) : True for id in range(numberOfUsers)}
        Ans = {"id" + str(id) : 0 for id in range(numberOfUsers)}
        Back = {}
        # print(events)
        for event in events:
            # print(Active)
            M, t, s = event
            if M == "MESSAGE":
                for kk,v in Back.items():
                    if int(t) >= v:
                        Active[kk] = True 


                if s == "ALL":
                    for k, v in Ans.items():
                        Ans[k] += 1
                elif s == "HERE":
                    for k, v in Active.items():
                        # print(k)
                        if v:
                            Ans[k] += 1
                else:
                    for id in s.split():
                        Ans[id] += 1

            else:
                id = "id" + s 
                Active[id] = False
                Back[id] = int(t) + 60

        # print(Ans)
        return list(Ans.values())


