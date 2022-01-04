import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import rstr

def ganttP1(tasks, P, D):
  tasks = [int(i) for i in tasks]
  fig, gnt = plt.subplots()
  #fig.figsize=(10, 20)
  fig.dpi=300
  gnt.set_ylim(0, len(tasks)) 
  gnt.set_xlim(0, sum(P)+10) 
  gnt.set_xlabel('Prossecing Time')
  gnt.set_ylabel('Tasks')
  yticks = []
  for i in range(0 , len(tasks)+1):
    yticks.append(i*10)
  gnt.set_yticks(yticks)
  gnt.set_yticklabels(list(range(1,len(tasks)+2)))
  gnt.grid(True)
  colors = ['tab:orange', 'tab:blue', 'tab:green', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']*(int(len(tasks)/9) + 1)
  PC = 0
  print(tasks)
  for i in tasks:
    gnt.broken_barh([(PC, P[i-1])], ((i-1)*10, 10), facecolors = (colors[i-1]))
    gnt.text(x=PC,y=i*10-5,s=" t="+str(int(PC)),ha='left', va='center', color='black', fontsize=6)
    if PC + P[i-1] > D[i-1]:
      gnt.broken_barh([(D[i-1], PC + P[i-1] - D[i-1])], ((i-1)*10, 3), facecolors = ('tab:red'))
    PC += P[i-1]
  fileName = rstr.xeger(r'[A-Z]\d[A-Z]\d[A-Z]\d') + ".png"
  plt.savefig("tardyJobs/files/results/" + fileName) 
  return fileName

def ganttP2(tasks, P, D, H, B):
  fig, gnt = plt.subplots() 
  fig.figsize=(15, 20)
  fig.dpi=300
  gnt.set_ylim(0, len(tasks)) 
  gnt.set_xlim(0, sum(P)+10) 
  gnt.set_xlabel('Prossecing Time')
  gnt.set_ylabel('Tasks') 
  yticks = []
  for i in range(0 , len(tasks)+1):
    yticks.append(i*10)
  gnt.set_yticks(yticks) 
  gnt.set_yticklabels(list(range(1,len(tasks)+2))) 
  gnt.grid(True)
  colors = ['tab:orange', 'tab:blue', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']*(int(len(tasks)/8) + 1)
  PC = 0
  for i in tasks:
    gnt.broken_barh([(PC, P[i-1])], ((i-1)*10, 10), facecolors = (colors[i-1]))
    gnt.text(x=PC,y=i*10-5,s=" t="+str(int(PC)),ha='left', va='center', color='black', fontsize=6)
    if PC + P[i-1] > D[i-1]:
      gnt.broken_barh([(D[i-1], PC + P[i-1] - D[i-1])], ((i-1)*10, 2), facecolors = ('tab:red'))
    if PC + P[i-1] < D[i-1]:
      gnt.broken_barh([(PC+P[i-1], D[i-1] - P[i-1] - PC)], ((i-1)*10, 2), facecolors = ('tab:green'))
    PC += P[i-1]
  #gnt.text(x=P[2],y=3*10-5,s="Text",ha='center', va='center', color='black')
  fileName = rstr.xeger(r'[A-Z]\d[A-Z]\d[A-Z]\d') + ".png"
  plt.savefig("tardyJobs/files/results/" + fileName)
  return fileName

def main(tasks, P, D, H = [], B=[]):
  if len(H) == 0:
    return ganttP1(tasks, P, D)
  else:
    return ganttP1(tasks, P, D, H, B)