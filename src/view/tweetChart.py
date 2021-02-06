import os
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

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
    
    # give a list with duplicated elements, and a sublist of this list, 
    # return a list without duplicated elements and the element of second list
    def goodLL(self, dati, list):
        l=[]
        for i in dati:
            if((type(i).__name__!='float')&(i!="")): 
                if i not in l:
                    if i not in list:
                        l.append(i)
        return l


# count 
# para: a list including duplicated elements(dirty), a list without duplicated elements(clean)
# def calCounts(self,dirty):
    def calCounts(self,clean,dirty):
        import numpy as np
        count = np.zeros(len(clean))
        a=0 #record all data include duplicated data
        for i in dirty:
            if  i != " ": a=a+1
            for element in range(len(clean)): 
                if i == clean[element]:
                    count[element] += 1
                    pass
        # print("len: ", a)
        total=0
        for i in count:
            total+=i
        # print("total: ", total)
        # print("Others: ", a-total)
        if "Others" in clean:
            count[-1] = a-total # count of 'others' is total count minus 'non others'
            # print(count)
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
        Xaxis=self.timeYMD(self.calDates(7),True)
        if ((file_name!="")&(tweets=="")):
            datess=self.datesJson(file_name)
            Yaxis=self.calCounts(self.calDates(7),self.timeYMD(datess))
        elif ((file_name=="")&(tweets!="")):
            x3=self.datesFunc(tweets)
            Yaxis=self.calCounts(self.calDates(7),self.timeYMD(x3))
        df = pd.DataFrame({'dates': Xaxis, 'counts': Yaxis})
        df.plot.bar(x='dates', y='counts',rot=0)
        plt.savefig(os.path.dirname(__file__) + "/../barchart.jpeg")

    def pieChart(self,file_name="",tweets=""):
        import matplotlib.pyplot as plt
        from matplotlib.patches import ConnectionPatch
        import numpy as np
        clean=['Twitter for Android', 'Twitter for iPhone', 'Twitter Web App', 'Others'] 
        if ((file_name!="")&(tweets=="")): #get data from the file
            Xaxis=['Twitter for Android', 'Twitter for iPhone', 'Twitter Web App', 'Others']
            Xaxis1=self.goodLL(self.sourceJson(file_name), Xaxis) #name of the sector
            Yaxis=self.calCounts(clean, self.sourceJson(file_name))
            Yaxis1=self.calCounts(Xaxis1, self.sourceJson(file_name))
        elif ((file_name=="")&(tweets!="")): #get the data from the funtion 
            Xaxis=['Twitter for Android', 'Twitter for iPhone', 'Twitter Web App', 'Others']
            Xaxis1=self.goodLL(self.sourceFunc(tweets), Xaxis)
            allSource=self.sourceFunc(tweets)
            Yaxis=self.calCounts(clean, allSource)
            Yaxis1=self.calCounts(Xaxis1, self.sourceFunc(tweets))

        data={"Xaxis": Xaxis, "Yaxis": Yaxis}
        others={"Xaxis": Xaxis1, "Yaxis": Yaxis1}

        # background
        fig = plt.figure(figsize=(12, 6),
                        facecolor='white'
                        )
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        fig.subplots_adjust(wspace=0)

        # bigger pie
        labs = data['Xaxis']
        Yaxis = data['Yaxis']
        explode = (0, 0, 0, 0.1)    # distance of explode

        ax1.pie(x=Yaxis,
                # colors=['cornflowerblue', 'orange', 'limegreen', 'orchid'], 
                colors=['deepskyblue', 'orange', 'limegreen', 'orchid'], 
                explode=explode,
                autopct='%1.1f%%',
                startangle=360,
                labels=labs,
                textprops={'color': 'w',
                        'fontsize': 12,
                        }
            )
        ax1.legend(loc='upper left')

        # smaller pie
        labs2 = others['Xaxis']
        Yaxis_2 = others['Yaxis']

        ax2.pie(x=Yaxis_2,
                # colors=['khaki', 'olive', 'gold'],
                autopct='%1.1f%%',
                startangle=70,
                labels=labs2,
                radius=0.6,
                textprops={'color': 'w',
                        'fontsize': 12,
                        },
            )

        ax2.legend(loc='upper left')

        # conjoint line tra two pie using ConnectionPatch
        # data in the edges of pie
        theta1 = ax1.patches[-1].theta1
        theta2 = ax1.patches[-1].theta2
        center = ax1.patches[-1].center
        r = ax1.patches[-1].r

        width=0.2
        # line in upper edges
        x = r*np.cos(np.pi/180*theta2)+center[0]
        y = np.sin(np.pi/180*theta2)+center[1]
        con_a = ConnectionPatch(xyA=(-width/2,0.6), xyB=(x,y),
                                coordsA='data', coordsB='data',
                                axesA=ax2, axesB=ax1
                            )

        #  line in under deges
        x = r*np.cos(np.pi/180*theta1)+center[0]
        y = np.sin(np.pi/180*theta1)+center[1]
        con_b = ConnectionPatch(xyA=(-width/2,-0.6), xyB=(x,y),
                                coordsA='data', coordsB='data',
                                axesA=ax2, axesB=ax1
                            )

        if (data['Yaxis'][3] != 0): # if 'others' != 0
            for con in [con_a, con_b]:
                con.set_linewidth(1)    # width of line
                con.set_color=([0,0,0])    # color of line
                ax2.add_artist(con)   # add conjoint line among two pictures
        plt.savefig(os.path.dirname(__file__) + "/../piechart.jpeg")