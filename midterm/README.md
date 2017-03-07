
# Question 1


### Analysis 1 

Every employee commmunicates with every other employee. This analysis calculate the No of emails sent from every employee to every other employee (Basically a Many to Many calculation) Data is sorted to check which two employees have communicated the most. May be checking those emails may provide some clue to the Enron bankruptcy.


### Analysis 2 

Formulated Certain business terms - 'market','gas','price','power','energy','trade','business','service'
The emails who has these business terms in the body of the mail has communicated the most about business to the traders
and solutionists. This report shows who has done most business work in the company.


### Analysis 3

Classify every email id present as Employee,CEO,CFO,Trader,President/VicePresident
This classification is done based on the research paper from Simon Fraser University
Link - http://www.sfu.ca/~shaw/papers/Joorabchi-EmailTimeCase-AbstractVAST10.pdf
Classification Criteria is mentioned in the paper
  
  Sent < #Received - President/VicePresident
  Sent > #Received - Employee
  Sent > #Received - Manager
  Different email id - Vendor/Trader/Solution
  
 

# Question 2

## Chosen API - Articles and Books

### Chosen Data

Articles - About Sports Celebs mainly Tennis(Each article is stored in a json file for each player)
Books - Books data containing publishers name,group where book belongs etc.(Each json file for one category of book)

### Analysis 1(article.ipynb)

Articles are published everyday and about every celebrity. This analysis analyses the article published in 2016
and reports a data of how many articles were published every month for each  celebrity .


### Analysis 2(books.ipynb)

Each book may belong to category like Fiction,Thriller,for Children etc.
This Analysis calculates how many books are present under each category.
Sorted the Books present under each category based on rank.
Reported the Top three most rated books and last three least rated book for the viewer under each category.


### Analysis 3(books.ipynb)

This Analysis ranks  the publishers based on how many books they published over the years.









