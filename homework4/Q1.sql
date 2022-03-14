create view mutual as 
select n1.name, n2.name 
from person, relationship 
where relationship.pid1 = p1.person.pid
and relationship.pid2 = p2.person.pid
and p1.pid1 = p2.pid1 
and p2.pid2 = p2.pid1 
and p1.rel = p2.rel;