



import time

spentCookie = 0
clickedCookie = 0
cookie = 0
cps = 0

cursor = 0
grandma = 0


starttime=time.time() 

def cps_thing():
  global cookie 
  global clickedCookie

  cookie = round(((((round((time.time() - starttime))) *cps) + (clickedCookie)) - spentCookie), 1)
  print('you have ' + str(cookie) + ' cookies!                                at ' + str(cps) +' cookies per sec!' )
  print('''

                                  (type what you want to buy)            SHOP    
                                                                       ==========
                                                            | 15 cookies | -> cursor  ('''+str(cursor)+''')

                                                                -------------------------
    
                                                         | 100 cookies | o-|<  grandma  ('''+str(grandma)+''')

    _________
   /         \

  /    o    o \

  |            |
  | o    o     |
  |            |
  \ o     o   /
   \_________/
    



  
  
  
  
  
  

  
  
  
  

  
  
  
    
  

  
  
  
  
  ''')
  clickedCookie += 1
  
def cps_counter():
  global cps
  global cursor

  if cursor >= 0:
    cps = (round((cursor * .2), 1)) + (grandma * 1)


def instructions():
  print('''
    This is Cookie Clicker
    type any letter and press enter to click a cookie
    =======================================================================================
    ''')






instructions()

while True:
  
  cps_counter()
  cps_thing()


  #buying System
  buy = ''


  while buy == '':
      buy = input('')

  buy = buy.lower().split()
  

  if buy[0] == 'cursor':
    if cookie >= 15:
      spentCookie += 15
      cursor += 1
    else:
      print('''
====================================
      you need 15 cookies
====================================
      ''')

  if buy[0] == 'grandma':
    if cookie >= 100:
      spentCookie += 100
      grandma += 1
    else:
      print('''
====================================
      you need 100 cookies
====================================
      ''')
