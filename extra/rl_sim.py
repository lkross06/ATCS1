#Lucas Ross 20 Nov. 2022
import random as r
import matplotlib.pyplot as plt
import numpy as np
import math as m

#model rocket league ranked 2s mmr growth over time
class Simulation:
    def __init__(self, pop, iterations):
        #constants

        #min and max mmr vals
        self.min = 0
        self.max = 2000

        self.num_ranks = 8
        self.mins = [ #minimum mmr requirement for each rank
            self.min, #bronze
            290, #silver
            475, #gold
            653, #plat
            835, #diamond
            1075, #champ
            1435, #gc
            1862, #ssl
            self.max # hopefully no one goes above this lols
        ]
        self.cols = [ #colors for each rank
            "brown",
            "darkgray",
            "gold",
            "cyan",
            "blue",
            "purple",
            "red",
            "black"
        ]
        self.ranks = [#names for each rank
            "bronze",
            "silver",
            "gold",
            "plat",
            "diamond",
            "champ",
            "gc",
            "ssl"
        ]

        self.pop = pop
        self.it = 0
        self.total_it = iterations
        self.change_mmr = 10
        self.queue_mmr_range = self.change_mmr * 4 

        self.player_data = []
        self.players = [self.get_start_mmr() for i in range(0, self.pop)] #keep track of each player's mmr (starting at 0)

        #run the entire simulation
        for i in range(0, self.total_it):
            self.iterate()
        self.end()

    def iterate(self): #runs another round of games
        print("Iteration " + str(self.it))

        self.player_data.append([])

        for i in range(0, self.pop):
            #play a game with the next player in the queue
            result = self.game(self.players[i])

            if result:
                self.win(i)
            else:
                self.lose(i)

            row = self.it
            col = i
            new = self.players[i]
            self.player_data[row].append(new)
        
        self.it += 1

    def game(self, p1):
        '''
        player is always on ORANGE team
        p1 + ai[0] vs. ai[1] + ai[2]
        '''
        ai = []
        #generate 3 players with random (but close in proximity) mmrs
        for x in range(0, 3):
            p = p1 + r.randint(-self.queue_mmr_range, self.queue_mmr_range)
            #allow the mmr to go under or over the min and max vals (we will fix it later)

            ai.append(p)

        orange_mmr = p1 + ai[0]
        blue_mmr = ai[1] + ai[2]

        #check to make sure mmrs are within mmr ranges:
        team_min = 2 * self.min
        team_max = 2 * self.max
        if orange_mmr > team_max:
            orange_mmr = team_max
        if orange_mmr < team_min:
            orange_mmr = team_min
        if blue_mmr > team_max:
            blue_mmr = team_max
        if blue_mmr < team_min:
            blue_mmr = team_min

        #failsafe if both vals are 0
        max = (orange_mmr if orange_mmr > blue_mmr else blue_mmr) if not(orange_mmr == 0 or orange_mmr == 0) else 1

        '''
        each team starts with a 50% chance of winning

        the difference between the two teams' mmrs are divided by the maximum mmr between both teams
        to get a % difference on a 1-100 scale

        then they are multiplied by 100 and added to 50 to either increase or decrease the team with larger mmr's
        chnace of winning by that much %
        '''
        orange_diff = (orange_mmr - blue_mmr)/max
        orange_win_rate = 50 + (orange_diff * 100)

        return orange_win_rate >= r.randint(0, 100)

    def win(self, p): # a player won a game, change player index
        self.players[p] += self.change_mmr
        #make sure it doesnt exceed cap
        if self.players[p] > self.max:
            self.players[p] = self.max

    def lose(self, p): # a player lost a game, change player index
        self.players[p] -= self.change_mmr
        #make sure its non-negative
        if self.players[p] < self.min:
            self.players[p] = self.min
            
    def get_start_mmr(self):
        mmr = 0
        #play 10 games
        for x in range(0, 10):
            result = self.game(mmr)

            if result:
                mmr += self.change_mmr
            else:
                mmr -= self.change_mmr
            
            if mmr > self.max:
                mmr = self.max
            if mmr < self.min:
                mmr = self.min
        
        return mmr

    def graph_avg(self):
        '''
        x axis / row: iterations
        y axis / col: player mmr
        '''

        #2d array to categorize the y values by rank
        cat = [[0 for j in range(0, self.it)] for i in range(0, self.num_ranks)]
        counts = [0 for i in range(0, self.num_ranks)]
        x = [x for x in range(0, self.it)]

        for i in range(0, self.pop):
            y = []
            for j in range(0, len(self.player_data)):
                y.append(self.player_data[j][i]) # take the ith entry of the jth row

            r = self.get_rank_index(y[-1]) #last element (current mrr)

            for i in range(0, len(cat[r])):
                cat[r][i] += y[i]
            counts[r] += 1

        for i in range(0, len(cat)):
            if counts[i] != 0: #if points exist
                rank = cat[i]
                for j in range(0, len(rank)):
                    rank[j] /= counts[i] # take the average


        for i in range(0, len(cat)):
            if counts[i] != 0: #if points exist
                #plot
                plt.plot(x, cat[i], color = self.cols[i])

        #add rank lines
        for i in range(0, self.num_ranks):
            plt.axhline(y=self.mins[i], color=self.cols[i])

        #edit y-axis tick lines
        plt.yticks(self.mins) 

        #set y lims
        plt.ylim(0, self.mins[self.get_max_rank_index(self.players) + 1])

        #edit titles
        plt.title(str(self.pop) + " Players / " + str(self.total_it) + " Iterations")
        plt.suptitle("Rocket League Ranked 2s Simulation [Average per Rank]")
        plt.xlabel("Number of Games Played")
        plt.ylabel("Average Ranked 2s MMR")
    
        plt.show()

    def graph_all(self):
        '''
        x axis / row: iterations
        y axis / col: player mmr
        '''

        #add data from every player
        for i in range(0, self.pop):
            y = []
            for j in range(0, len(self.player_data)):
                y.append(self.player_data[j][i]) # take the ith entry of the jth row

            final = y[-1] #last element (current mrr)

            col = self.cols[self.get_rank_index(final)]

            x = [n for n in range(0, self.it)]

            plt.plot(x, y, color=col)
        
        #add rank lines
        for i in range(0, self.num_ranks):
            plt.axhline(y=self.mins[i], color=self.cols[i])

        #edit y-axis tick lines
        plt.yticks(self.mins) 

        #set y lims
        plt.ylim(0, self.mins[self.get_max_rank_index(self.players) + 1])

        #edit titles
        plt.title(str(self.pop) + " Players / " + str(self.total_it) + " Iterations")
        plt.suptitle("Rocket League Ranked 2s Simulation [All Players]")
        plt.xlabel("Number of Games Played")
        plt.ylabel("Ranked 2s MMR")
    
        plt.show()
    
    def graph_dist(self):
        '''
        x axis / row: iterations
        y axis / col: player mmr
        '''

        #counters for every rank
        counts = [0 for x in range(0, self.num_ranks)]

        #add data from every player
        for i in range(0, self.pop):

            final = self.players[i] #current mrr
            r = self.get_rank_index(final)

            counts[r] += 1 #add 1 to rank

        for i in range(0, len(counts)):
            plt.bar(self.ranks[i], counts[i], color=self.cols[i]) #plot bar

        #make y axis multiples of 10
        max = np.max(counts)
        plt.ylim(0, (max - (max % 10)) + 10) #round up to next multiple of 10

        #edit titles
        plt.title(str(self.pop) + " Players / " + str(self.total_it) + " Iterations")
        plt.suptitle("Rocket League Ranked 2s Simulation [Distribution]")
        plt.xlabel("2s Rank")
        plt.ylabel("Frequency")
    
        plt.show()

    def end(self):
        self.get_rank_percentages(self.players) #self.players is updated with every player's final rank
        self.graph_all()
        self.graph_avg()
        self.graph_dist()

    def get_rank_percentages(self, arr): #gets the percentage metrics for each rank and prints them 
        def get_percent(n):
            return "{:,.2f}%".format(n)

        print("\n--- FINAL RANK PERCENTAGES ---")

        counts = [0 for x in range(0, self.num_ranks)]

        for i in arr:
            r = self.get_rank_index(i)
            counts[r] += 1

        total = self.pop
            
        for i in range(0, self.num_ranks):
            percent = get_percent((counts[i] / total) * 100)
            buffer = ":\t\t" if i != 4 else ":\t" #diamond is weird and so it requires only 1 tab
            print(self.ranks[i] + buffer + str(percent))
    
    def get_rank_index(self, mmr):
        for i in range(0, self.num_ranks): #only time we use len(self.mins) instead of self.num_ranks
            if mmr < self.mins[i]:
                return i - 1
        return 7

    def get_max_rank_index(self, arr): #gets the max rank any player reached
        max = 0
        for i in arr:
            r = self.get_rank_index(i)
            if r > max:
                max = r
        return max

iterations = 5000
population = 100
Simulation(population, iterations)
