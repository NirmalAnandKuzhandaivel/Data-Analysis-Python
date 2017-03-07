
# Question 1


### Analysis 1 

Every employee commmunicates with every other employee. This analysis calculate the No of emails sent from every employee to every other employee (Basically a Many to Many calculation) Data is sorted to check which two employees have communicated the most. May be checking those emails may provide some clue to the Enron bankruptcy.

#### Sample Output:

From	Recipient	Count
vince.kaminski@enron.com	vkaminski@aol.com	1061
kay.mann@enron.com	suzanne.adams@enron.com	428
vince.kaminski@enron.com	shirley.crenshaw@enron.com	303
kay.mann@enron.com	nmann@erac.com	285
kay.mann@enron.com	ben.jacoby@enron.com	237



### Analysis 2 

Formulated Certain business terms - 'market','gas','price','power','energy','trade','business','service'
The emails who has these business terms in the body of the mail has communicated the most about business to the traders
and solutionists. This report shows who has done most business work in the company.

#### Sample Output:

Email-id	No of Business Email sent
vince.kaminski@enron.com	470
david.delainey@enron.com	160
drew.fossum@enron.com	152
mike.mcconnell@enron.com	116
kay.mann@enron.com	100
john.arnold@enron.com	99


### Analysis 3

Classify every email id present as Employee,CEO,CFO,Trader,President/VicePresident
This classification is done based on the research paper from Simon Fraser University
Link - http://www.sfu.ca/~shaw/papers/Joorabchi-EmailTimeCase-AbstractVAST10.pdf
#Classification Criteria is mentioned in the paper
  
  #Sent < #Received - President/VicePresident
  #Sent > #Received - Employee
  #Sent > #Received - Manager
  #Different email id - Vendor/Trader/Solution
  
#### Sample Output:
  
Email	Sent	Received	Categorization
canwest_leigh_lyons@worldnet.att.net	0	1	Trader
karie.davis@eprime.com	0	2	Trader
david.bayless@utility.com	0	2	Trader
kimberly.allen@enron.com	0	31	President/Vice-President
rring@enron.com	0	1	President/Vice-President
david.haug@enron.com	0	13	President/Vice-President
tpclosson@aol.com	0	1	Trader

  

# Question 2

## Chosen API - Articles and Books

### Chosen Data

Articles - About Sports Celebs mainly Tennis(Each article is stored in a json file for each player)
Books - Books data containing publishers name,group where book belongs etc.(Each json file for one category of book)

### Analysis 1(article.ipynb)

Articles are published everyday and about every celebrity. This analysis analyses the article published in 2016
and reports a data of how many articles were published every month for each  celebrity .

#### Sample Output:

Name	January	February	March	April	May	June	July	August	September	October	November	December
Novak,Djokovic	61	17	24	9	35	31	30	17	32	14	25	5
Michael,Phelps	8	0	9	6	4	43	36	148	9	4	1	12
Andy,Murray	36	7	17	7	36	37	39	20	24	24	39	14

### Analysis 2(books.ipynb)

Each book may belong to category like Fiction,Thriller,for Children etc.
This Analysis calculates how many books are present under each category.
Sorted the Books present under each category based on rank.
Reported the Top three most rated books and last three least rated book for the viewer under each category.

#### Sample Output:

Category	No of Books	Top Ranked Books	Least Ranked Books
Humor	10	TALKING AS FAST AS I CAN,BORN A CRIME,THE DAILY SHOW (THE BOOK)	GO THE -- TO SLEEP,WHY NOT ME?,KATHY GRIFFIN'S CELEBRITY RUN-INS
Childrens Middle Grade Paperback	10	HIDDEN FIGURES,A LONG WALK TO WATER,THE ONE AND ONLY IVAN	THE WAR THAT SAVED MY LIFE,BROWN GIRL DREAMING,OUT OF MY MIND
Young Adult E-Book	5	BURNING GLASS,FLAMECASTER,MISTRUST	MISTRUST,AND I DARKEN,WINDWITCH
Religion Spirituality and Faith	10	SHAKEN,THE BOOK OF JOY,THINK BETTER, LIVE BETTER	PRESENT OVER PERFECT,THE POWER OF NOW,THE AMERICAN MIRACLE


### Analysis 3(books.ipynb)

This Analysis ranks  the publishers based on how many books they published over the years.

#### Sample Output:

Rank	Publisher Name	No of Publications
1	Simon  Schuster	22
2	Random House	17
3	Houghton Mifflin Harcourt	16
3	Little Brown	16







