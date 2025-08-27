% Facts: defining parent relationships.

parent(john, mary).
parent(mary, susan).
parent(mary, David).
parent(susan, alice).
 
% Rule: defining ancestor relationships.
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

 % Query examples:

% To find all ancestors of alice, you would ask:

% ?- ancestor(X, alice).

"""Explanation:

Facts: Declare direct relationships (e.g., parent(john, mary)) that form the knowledge base.
Rules: Define the relationship recursively. 
The rule ancestor(X, Y) first checks if X is a parent of Y and then reuses the ancestor relation to build deeper relationships."""