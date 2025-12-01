Encapsulation:

Encapsulation is the principle of bundling data and controling the amount of access
other files or users can have to that data. This is represented in the python library
through naming comventions rather than something like public or private variables/classes.
Data is still bundled together through using separate classes, but as for limiting access
to different attributes you are supposed to use the underscore before the name of a 
'private variable'. Using getters also helps to point users in the right direction,
which helps with preventing errors.

Inheritance:

While python uses both composition and inheritance, inheritance is the more prominant
relationship. Inheritance established an 'is-a' relationship, which means that objects 
like 'Book' and 'Dvd' are items and have to implement its methods. On the other hand 
the 'Member' class still only 'has-a' relationship with the 'Catalog' class, and this
represents the composition.

Polymorphism:

Polymorphism is used in python similarly to Rust. Such that when we are looking to use 
'get_item_details' we don't care which 'Item' is being sent because we will treat it 
differently if it's a 'Book' or a 'Dvd'. Python in general is very polymorphic since it
is dynamically typed. This means that you can declare something like 'x=5' and then later
'x="hi"' and python will treat that same variable differently in both cases.
