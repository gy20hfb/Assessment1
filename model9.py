import random
import operator
import matplotlib.pyplot
import agentframework
import csv

seed = 1

random.seed(seed)

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#open csv file
f = open("in.txt", newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Lines here happen before any data is processed
""" Creating the environments list to link to the agents and the agents list to link to the agents. """
environment = []
agents = []

""" shuffle the agents in each iteration """
random.shuffle(agents)

for row in reader:
    rowlist = []
    # Lines here happen before each row is processed
    for values in row:
        # do something with values
        rowlist.append(values)  
    # Lines here happen before after row is processed
    environment.append(rowlist)
# Lines here happen after all the data is processed
f.close()    

#make agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    
#test agents
print("After making agents")
for i in range(num_of_agents):
    print(agents[i])

#move agents
""" Behavioural methods move, eat and share with neighbours. """
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbourhood(neighbourhood)

#test agents after eating, moving and shareing with neighbours
print("After eating, moving and sharing with neighbours")
for i in range(num_of_agents):
    print(agents[i])

#plot in graph
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    matplotlib.pyplot.show()


"""
Was unable to get the animations and GUI/Webscaping code working correctly by the deadline, many apologies for this.
"""

"""
Animation code used to animate the model and run the number of iterations before stopping the animation.

""" 
#import matplotlib.animation 

#fig = matplotlib.pyplot.figure(figsize=(7, 7))
#ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

# Make the agents.
#for i in range(num_of_agents):
    #agents.append([random.randint(0,100),random.randint(0,100)])

#carry_on = True	
	
#def update(frame_number):
    
   # fig.clear()   
   # global carry_on
    
    #for i in range(num_of_agents):
        #if random.random() < 0.5:
           # agents[i][0]  = (agents[i][0] + 1) % 99 
        #else:
          #  agents[i][0]  = (agents[i][0] - 1) % 99
        #
        #if random.random() < 0.5:
          # agents[i][1]  = (agents[i][1] + 1) % 99 
       # else:
            #agents[i][1]  = (agents[i][1] - 1) % 99 
        
    #if random.random() < 0.1:
      #  carry_on = False
       # print("stopping condition")
    
    #for i in range(num_of_agents):
        #matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        #print(agents[i][0],agents[i][1])
		
#def gen_function(b = [0]):
   # a = 0
   # global carry_on #Not actually needed as we're not assigning, but clearer
   # while (a < 10) & (carry_on) :
      #  yield a			# Returns control and waits next call.
      #  a = a + 1

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

#matplotlib.pyplot.show()


"""
GUI and webscaping code to get the model to animate in a seperate GUI with model initialising button. 
Also webscaping code to add in data from the web to the top of the model in the GUI.
"""
#import matplotlib
#matplotlib.use('TkAgg')

#import requests
#import bs4

#r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
#content = r.text
#soup = bs4.BeautifulSoup(content, 'html.parser')
#td_ys = soup.find_all(attrs={"class" : "y"})
#td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)

#def run():
    #matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    #canvas.draw()
    
    #root = tkinter.Tk()
    #root.wm_title("Model")
    #canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(master=root)
    #canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    #menu_bar = tkinter.Menu(root)
    #root.config(menu=menu_bar)
    #model_menu = tkinter.Menu(menu_bar)
    #menu_bar.add_cascade(label="Model", menu=model_menu)
    #model_menu.add_command(label="Run model", command=run)
    #tkinter.mainloop()

              
        

