class configure:
    def __init__(self):
        self.user_data = {'userName': None,'mobile':None,'score':None,
                    "startTime":None,"endTime":None,"level":None}
    
    def setName(self,name):
        self.user_data['userName'] = name

    
    def setMobile(self, number):
        self.user_data['mobile'] = number

    def setScore(self, score):
        if score:
            print("score:", score)
            # uid = self.user_data.get(number, 0)
            # print("uid:",uid)
            self.user_data['score'] = score
        print("---SCORE----",self.user_data['score'])

    def setStartTime(self, St):
        # print("Setting start time")
        #print("setStartTime: number:" + str(number) + "St:" + str(St))
        if St:
            print("start time: ",St)
    
        self.user_data['startTime'] = St
    
        
    def setEndTime(self, Et):
        if Et:
            print("end time: ",Et)
        # if number:
        #     uid = self.user_data.get(number,0)
        #     if uid:
        self.user_data['endTime'] = Et
    
    def setLevel(self, level = None):
        
        # if number:
        #     uid = self.user_data.get(number,None)
        #     if uid:
        self.user_data['level'] = level

    
    def getName(self):
        try:
            print("name:", self.user_data.get('userName'))
            return self.user_data['userName']

        except Exception as e:
            print("ERROR in getName function",e)
  

        
    def getMobile(self):
        try:
            print("mobile number:", self.user_data.get('mobile'))
            return self.user_data['mobile'] 
        except Exception as e:
            print("error in getMobile function",e)

    def getScore(self):
            print("score:", self.user_data.get('score'))
            return self.user_data['score']



    def getStartTime(self):
        print("Getting start time")
        # print("setStartTime: number:" + str(number) + "St:" + str(St))
        print("start time: ",self.user_data.get('startTime'))
        val = self.user_data['startTime']
        # print(val)
        # print(type(val))
        return val

    def getEndTime(self):
            print("end time: ",self.user_data.get('endTime'))
            return self.user_data['endTime']
       
    def getLevel(self):
            print("level:", self.user_data.get('level'))
            return self.user_data['level']
