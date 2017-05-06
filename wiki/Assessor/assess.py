#!/usr/bin/env python3

import re

# TODO: Read votes.py into arrays

class Voter:
   def __init__(self, name, votes):
         self.n = name
         self.v = votes

class Proposal:
   def __init__(self, name, ai):
      self.n = name
      self.ai = float(ai)
      self.q = 0
      self.f = 0
      self.a = 0
      self.p = 0
      self.v_c = 0

   def votes(self):
#      print(self.f + self.a + self.p - self.v_c)
      return self.f + self.a + self.p - self.v_c

   def met_quorum(self):
      return (self.votes() >= self.q)

   def met_ai(self):
      return ((self.a == 0) and (self.f > 0)) or (((self.f/self.a) >= self.ai) and (self.f/self.a > 1))

   def passed(self):
      return self.met_ai() and self.met_quorum()

   def next_quorum(self):
      return self.votes() - 3

   def f_a(self):
      return str(self.f) + "/" + str(self.a)

file = open("votes.txt", "r")

voters = []
proposals = []
name_space = 0
prop_space = 0

for line in file:
   line_arr = re.split(r';', re.sub("\n","",line))
   if line_arr[0] == "q":
      first_q = int(line_arr[1])
   elif line_arr[0] == "p":
      proposals.append(Proposal(line_arr[1],line_arr[2]))
      prop_space = max(len(line_arr[1])+2, prop_space)
   elif line_arr[0] == "v":
      voters.append(Voter(line_arr[1],line_arr[2:]))
      name_space = max(len(line_arr[1]), name_space)
   else:
      print("Unrecognized line: " + str(line_arr))

voters.sort(key = lambda x: x.n.lower())

proposals[0].q = first_q

# TODO: Calculate

for i in range(len(proposals)):
   for j in range(len(voters)):
      vote = voters[j].v[i]
      if vote == "F":
         proposals[i].f += 1
      elif vote == "FF":
         proposals[i].f += 2
         proposals[i].v_c +=1
      elif vote == "A":
         proposals[i].a += 1
      elif vote == "AA":
         proposals[i].a +=2
         proposals[i].v_c +=1
      elif vote == "P":
         proposals[i].p += 1
      else:
         print("Didn't capture vote " + vote)

for i in range(len(proposals)-1):
   proposals[i+1].q = proposals[i].next_quorum()

# TODO: Format output
print("|" + name_space*' ' + " |",end='')
for p in proposals:
   print(" " + p.n + " |",end='')
print()

print("|" + name_space*"-" + "-+" + len(proposals)*(prop_space*"-" + "+"))

for v in voters:
   print("|" + v.n + (name_space-len(v.n))*" " + " |",end='')
   for i in range(len(proposals)):
      print(" " + v.v[i] + (prop_space-len(v.v[i])-1)*' ' + "|" ,end='')
   print()

print("|" + name_space*"-" + "-+" + len(proposals)*(prop_space*"-" + "+"))

print("|" + "F/A" + (name_space-3)*' ' + " |",end='')
for p in proposals:
   print(" " + p.f_a() + (prop_space-len(p.f_a())-1)*' ' + "|", end='')
print()

print("|" + "AI" + (name_space-2)*' ' + " |",end='')
for p in proposals:
   print(" " + str(p.ai) + (prop_space-len(str(p.ai))-1)*' ' + "|", end='')
print()

print("|" + "V" + (name_space-1)*' ' + " |",end='')
for p in proposals:
   print(" " + str(p.votes()) + (prop_space-len(str(p.votes()))-1)*' ' + "|", end='')
print()

print("|" + "Q" + (name_space-1)*' ' + " |",end='')
for p in proposals:
   print(" " + str(p.q) + (prop_space-len(str(p.q))-1)*' ' + "|",end='')
print()

print("|" + "P" + (name_space-1)*' ' + " |",end='')
for p in proposals:
   print(" " + str(p.passed())[0] + (prop_space-2)*' ' + "|",end='')
print()
print()

print("Final quorum: " + str(proposals[-1].next_quorum()))
