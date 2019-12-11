import tweepy
from datetime import datetime, timedelta
import networkx as nx
import matplotlib.pyplot as plt

# ParsingData class


class ParsingData:

    __userName = None
    __api = ""
    __listOfTweets = []
    __listOfFollowers = []  # Contains a list of the user's followers as a string

    # NOTE: all of these keys can't be in here
    __consumer_key = 
    __consumer_secert = 
    __access_token_secert = 
    __access_token = 

    """ Constructor
        Accesses the api and obtains the users' tweets and list of followers
    """

    def __init__(self, userName):
        self.__userName = userName

        # access API
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secert)
        auth.set_access_token(self.__access_token, self.__access_token_secert)
        self.__api = tweepy.API(auth, wait_on_rate_limit=True)

        # obtains user's tweets [UNCOMMENT NEXT LINE FOR TWEETS TO WORK]
        self.getTweets()

        # obtaining the user's followers [UNCOMMENT NEXT LINE FOR FOLLOWERS TO WORK]
        #for page in tweepy.Cursor(self.__api.followers, screen_name=self.__userName).pages():
         #   self.__listOfFollowers.extend(page)

        self.follower_list = self.getFollowersCount()

    """ getTweets
        obtains the users tweets from the last seven months and placing it in the __listOfTweets variable
    """

    def getTweets(self):
        cursor = tweepy.Cursor(self.__api.user_timeline, screen_name=self.__userName)
        for tweet in cursor.items():
            if (datetime.now() - tweet.created_at).days < 213:
                self.__listOfTweets.append(tweet)
            else:
                break

    """ avgLikeForSixMonths
        Obtains the average number of likes per month, within a six month period

        returns: averageData -  2-D list that contains the date (YYYY-mm) and the average
    """

    def avgLikesForSixMonths(self):
        # Declaring variable
        averageData = []                        # 2D list containing the avg number of like/month
        numOfTweets = 0                         # contains the number of tweets per period
        monthToComp = datetime.today().month    # month to compare tweets with
        currentDate = datetime.today()          # current date
        numOfLikes = 0                          # number of likes per month
        numOfMonths = 6                         # number of months to find average of
        userTweets = self.__listOfTweets        # The user's tweets

        i = 0                                   # iterate through 6 months
        j = 0                                   # iterate through the userTweets

        # go through each month within a 6 month period
        while (i < numOfMonths):

            # Go through the list of tweets starting from tweets made in the begining of the months to the end
            while j in range(len(userTweets)):
                if (userTweets[j].created_at.month == monthToComp):
                    numOfTweets = numOfTweets + 1
                    numOfLikes = numOfLikes + userTweets[j].favorite_count
                    j += 1
                else:
                    break

            # Add averages and dates to the averageDate
            averageData.append([])
            dateToSave = datetime(currentDate.year,
                                  monthToComp, currentDate.day)
            averageData[len(averageData)-1].append(dateToSave.strftime("%Y-%m"))

            # Used to avoid error (i.e. division by zero)
            if (numOfTweets != 0):
                averageData[len(averageData)-1].append(numOfLikes/numOfTweets)
            else:
                averageData[len(averageData)-1].append(0)

            # decreasing the months
            first = currentDate.replace(day=1)
            currentDate = first - timedelta(days=1)
            monthToComp = currentDate.month

            # Reset values
            numOfTweets = 0
            numOfLikes = 0
            i += 1

        return averageData

    """ avgLikesForWeek
        Obtains the average number of likes within a week over a period of four weeks

        returns: averageData -  2-D list that contains the start date (YYYY-mm-dd) and the average
    """

    def avgLikesForWeek(self):
        tweetsInMonth = []                      # tweets within the last 30 days
        averageData = []                        # the averages - to be returned from function
        endDay = datetime.today()               # the date at the end of the week
        startDay = endDay - timedelta(days=7)   # the date at the begining of the week
        numOfTweets = 0                         # the number of tweets made during a week
        count = 0                               # used to count the number of items in the averageData array
        sum = 0                                 # the sum of all of likes tweets made in a particular week

        # obtaining tweets within the last 35 days
        for tweet in self.__listOfTweets:
            if ((datetime.now() - tweet.created_at).days <= 35):
                tweetsInMonth.append(tweet)
            else:
                break
        print("\n")
        # go through each week in the month and store the average and start date in the averageData array
        i = 0
        while (i < len(tweetsInMonth)):
            # check if the four items have been stored in the array if it is break from loop
            if count > 3:
                break

            # Check if the tweet is within the week and add the number of likes and number of tweets accordingly
            if (startDay <= tweetsInMonth[i].created_at <= endDay):
                numOfTweets += 1
                sum = sum + tweetsInMonth[i].favorite_count

            # checks if the tweet is before the begining of the current week
                # if it is: find and store average and date
            if ((startDay > tweetsInMonth[i].created_at)):
                averageData.append([])
                averageData[len(averageData)-1].append(startDay.strftime("%Y-%m-%d"))
                count += 1
                # used to avoid error - if no tweets were made
                if (numOfTweets == 0):
                    numOfTweets = 1

                averageData[len(averageData)-1].append(sum/numOfTweets)

                # still need to check if the current tweets is within range it was not before
                # Therefore decrease i so it is at the previous tweet
                i -= 1

                # reseting values for new week
                numOfTweets = 0
                sum = 0
                endDay = startDay
                startDay = endDay - timedelta(days=7)
            # point to next item in list of tweets
            i += 1
        return averageData

        """ avgRetweetForWeek
            Obtains the average number of retweets within a week over a period of four weeks

            TO BE DELETED: [EVERYTHING IS THE SAME EXCEPT FOR ONE LINE]

            returns: averageData -  2-D list that contains the start date (YYYY-mm-dd) and the average
        """

    def avgRetweetForWeek(self):
        tweetsInMonth = []                      # tweets within the last 30 days
        averageData = []                        # the averages - to be returned from function
        endDay = datetime.today()               # the date at the end of the week
        startDay = endDay - timedelta(days=7)   # the date at the begining of the week
        numOfTweets = 0                         # the number of tweets made during a week
        count = 0                               # used to count the number of items in the averageData array
        sum = 0                                 # the sum of all of likes tweets made in a particular week

        # obtaining tweets within the last 35 days
        for tweet in self.__listOfTweets:
            if ((datetime.now() - tweet.created_at).days <= 35):
                tweetsInMonth.append(tweet)
            else:
                break
        print("\n")
        # go through each week in the month and store the average and start date in the averageData array
        i = 0
        while (i < len(tweetsInMonth)):
            # check if the four items have been stored in the array if it is break from loop
            if count > 3:
                break

            # Check if the tweet is within the week and add the number of retweets and number of tweets accordingly
            if (startDay <= tweetsInMonth[i].created_at <= endDay):
                numOfTweets += 1
                sum = sum + tweetsInMonth[i].retweet_count

            # checks if the tweet is before the begining of the current week
                # if it is: find and store average and date
            if ((startDay > tweetsInMonth[i].created_at)):
                averageData.append([])
                averageData[len(averageData)-1].append(startDay.strftime("%Y-%m-%d"))
                count += 1
                # used to avoid error - if no tweets were made
                if (numOfTweets == 0):
                    numOfTweets = 1

                averageData[len(averageData)-1].append(sum/numOfTweets)

                # still need to check if the current tweets is within range it was not before
                # Therefore decrease i so it is at the previous tweet
                i -= 1

                # reseting values for new week
                numOfTweets = 0
                sum = 0
                endDay = startDay
                startDay = endDay - timedelta(days=7)
            # point to next item in list of tweets
            i += 1
        return averageData

    """ avgRetweetForSixMonths
        Obtains the average number of retweet per month, within a six month period

        TO BE DELETED: [EVERYTHING IS THE SAME EXCEPT FOR ONE LINE]

        returns: averageData -  2-D list that contains the date (YYYY-mm) and the average
    """

    def avgRetweetForSixMonths(self):
        # Declaring variable
        averageData = []                        # 2D list containing the avg number of retweets/month
        numOfTweets = 0                         # contains the number of tweets per period
        monthToComp = datetime.today().month    # month to compare tweets with
        currentDate = datetime.today()          # current date
        numOfRetweets = 0                          # number of retweets per month
        numOfMonths = 6                         # number of months to find average of
        userTweets = self.__listOfTweets        # The user's tweets

        i = 0                                   # iterate through 6 months
        j = 0                                   # iterate through the userTweets

        # go through each month within a 6 month period
        while (i < numOfMonths):

            # Go through the list of tweets starting from tweets made in the begining of the months to the end
            while j in range(len(userTweets)):
                if (userTweets[j].created_at.month == monthToComp):
                    numOfTweets = numOfTweets + 1
                    numOfRetweets = numOfRetweets + userTweets[j].retweet_count
                    j += 1
                else:
                    break

            # Add averages and dates to the averageDate
            averageData.append([])
            dateToSave = datetime(currentDate.year,
                                  monthToComp, currentDate.day)
            averageData[len(averageData)-1].append(dateToSave.strftime("%Y-%m"))

            # Used to avoid error (i.e. division by zero)
            if (numOfTweets != 0):
                averageData[len(averageData)-1].append(numOfRetweets/numOfTweets)
            else:
                averageData[len(averageData)-1].append(0)

            # decreasing the months
            first = currentDate.replace(day=1)
            currentDate = first - timedelta(days=1)
            monthToComp = currentDate.month

            # Reset values
            numOfTweets = 0
            numOfRetweets = 0
            i += 1

        return averageData

    """  getFollowersCount

        get list of the user's followers follower's twitter handle, number of followers and number of users they
        are following

        return: listOfFollowersCount - 3D array that contains the user's followers follower's twitter handle, number of followers
                                       and number of users they are following
    """

    def getFollowersCount(self):
        # Declaring variable

        # contains the user's followers follower's twitter handle, number of followers and number of users they are following
        listOfFollowersCount = []

        # user's Information from api
        user = self.__api.get_user(self.__userName)

        # The minimum number of followers who will be included in the array. This is used to avoid bots
        if (user.friends_count < 5):
            lowerThreshold = 3
            upperThreshold = 5
        else:
            lowerThreshold = user.friends_count * 0.3
            upperThreshold = user.friends_count * 5

        # Goes through the user's followers and adds their followers follower's information
        for user in self.__listOfFollowers:

            if(user.followers_count > lowerThreshold) & (user.followers_count < upperThreshold) & (user.screen_name is not None):
                listOfFollowersCount.append([])
                listOfFollowersCount[len(listOfFollowersCount) -
                                     1].append(user.screen_name)
                listOfFollowersCount[len(listOfFollowersCount) -
                                     1].append(user.followers_count)
                listOfFollowersCount[len(listOfFollowersCount) -
                                     1].append(user.friends_count)

        return listOfFollowersCount

    def printFollowers(self):
        for follower in self.__listOfFollowers:
            print(follower.screen_name)

    """ monthlyPrediction

        returns the prediction values for likes and retweets based on values gathered in the past month

    """''

    def monthlyPrediction(self):
        numOfLikes = 0
        numOfRetweet = 0
        numOfTweets = 0
        prediction = []

        # obtaining the likes from the last 30 days
        for tweet in self.__listOfTweets:
            if ((datetime.now() - tweet.created_at).days <= 30):
                numOfLikes = numOfLikes + tweet.favorite_count
                numOfRetweet = numOfRetweet + tweet.retweet_count
                numOfTweets = numOfTweets + 1
            else:
                break
        prediction.append(numOfTweets)  
        prediction.append(numOfRetweet)
        prediction.append(numOfLikes)

        if numOfTweets == 0: 
            numOfTweets = 1
            
        aveLikesPerTweet = numOfLikes/numOfTweets
        likePred = aveLikesPerTweet * 5
        prediction.append(likePred)
        aveRetweetsPerTweet = numOfLikes/numOfTweets
        rtPred = aveRetweetsPerTweet * 5
        prediction.append(rtPred)
            
        return prediction

    
    def drawNetwork(self):
        user = self.__userName
        # [name, #of followers, #following] below is test code
        # follower_list = [['f1', 1000, 1234], ['f2', 1500, 1234], ['f3', 2300, 1234], ['f4',150, 1234]]
        follower_list = self.follower_list
        print(follower_list)
        size_list = [len(follower_list)]

        soc_map = nx.Graph()

        for follower in follower_list:
            weight = (follower[1]/follower[2])
            soc_map.add_edge(user, follower[0], weight=weight)
            size_list.append(follower[1]/len(follower_list))

        nx.spring_layout(soc_map)
        nx.draw_networkx(soc_map, node_size=size_list, font_size=6, k=0.30, iterations=20, width=0)
        print(nx.info(soc_map))

        plt.savefig("graph.jpg", format="JPEG")
        plt.show

    def topFollower(self):
        follower_list = self.follower_list

        for follower in follower_list:
            weight = (follower[1]/follower[2])
            follower.append(weight)

        sortList = sorted(follower_list, key=lambda x: (-x[3], -x[1]))
        top_follower = sortList[0][0]
        return top_follower


