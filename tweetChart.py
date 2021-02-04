import pandas as pd


class TweetChart():
    def __init__(self):
        pass
    
    def calDates(self,ddd):
        import datetime as dt 
        halfAgo=dt.date.today()-dt.timedelta(days=ddd)
        days=[]
        for i in range(ddd+1):
            days.append(str(halfAgo))
            halfAgo+=dt.timedelta(days=1)
        return days

    def timeYMD(self,dates,bool=False):
        l=[]
        for i in dates:
            j=pd.to_datetime(i)
            if(bool==False):
                aa=(j.strftime("%Y-%m-%d"))
            else:
                aa=(j.strftime("%m-%d"))
            l.append(aa)
        return  l

    def goodL(self,dati):
        l=[]
        for i in dati:
            if((type(i).__name__!='float')&(i!="")): 
                if i not in l:
                    l.append(i)
        return l

    def calCounts(self,clean,dirty):
        import numpy as np
        count = np.zeros(len(clean))
        for i in dirty: 
            for element in range(len(clean)): 
                if i == clean[element]:
                    count[element] += 1
                    pass
        return count

    def datesFunc(self,tweets):
        return [tweet["created_at"] for tweet in tweets]

    def sourceFunc(self,tweets):
        import re
        reg=re.compile('<[^>]*>')
        return [reg.sub('',tweet["source"]) for tweet in tweets]

    def loadJson(self, file_name):
        import json
        with open(file_name) as f:
            self.data = json.load(f)
        return self.data["Tweets"]

    def sourceJson(self,file_name):
        import re
        reg=re.compile('<[^>]*>')
        return [reg.sub('',tweet["source"]) for tweet in self.loadJson(file_name)]

    def datesJson(self,file_name):
        return [tweet["created_at"] for tweet in self.loadJson(file_name)]

    def barChart(self,file_name="",tweets=""):
        import matplotlib.pyplot as plt
        Xaxis=self.timeYMD(self.calDates(7),True)
        if ((file_name!="")&(tweets=="")):
            datess=self.datesJson(file_name)
            Yaxis=self.calCounts(self.calDates(7),self.timeYMD(datess))
        elif ((file_name=="")&(tweets!="")):
            x3=self.datesFunc(tweets)
            Yaxis=self.calCounts(self.calDates(7),self.timeYMD(x3))
        df=pd.DataFrame({'dates':Xaxis,'counts': Yaxis})
        ax=df.plot.bar(x='dates', y='counts',rot=0)
        plt.savefig("barchart.jpeg")

    def pieChart(self,file_name="",tweets=""):
        import matplotlib.pyplot as plt 
        if ((file_name!="")&(tweets=="")):
            Xaxis=self.goodL(self.sourceJson(file_name))
            Yaxis=self.calCounts(Xaxis,self.sourceJson(file_name))
        elif ((file_name=="")&(tweets!="")):
            allSource=self.sourceFunc(tweets)
            Xaxis=self.goodL(allSource)
            Yaxis=self.calCounts(Xaxis,allSource)
        pi = pd.Series(Yaxis, index=Xaxis, name='Sources')
        pi.plot.pie(fontsize=11, autopct='%.1f%%', figsize=(6, 6)) 
        plt.savefig("piechart.jpeg")