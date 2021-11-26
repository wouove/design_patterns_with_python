Coding exercises that come with Design Patterns with Python

#SOLID object oriented programming principles
**S**: Single responsibility \
**O**: Open/Closed. Class should be open to extension (by inheretance), but closed for modification \
**L**: Liskov substitution principle. \
**I**: Interface segregation principle. Many different interfaces are better than "One to rule them all" \
**D**: dependency inversion principle. Depend upon abstractions, not on implementations

# 1 Strategy pattern
- Encapsulate algorithms
- Several techniques available
- Red flag: sequences of if/elif statements

# 2 Observer pattern
- Detach the concerns of subject and observer
- Encapsulate what changes, i.e. the respective subjects and observers.
- Difficulty: the observer has to explicitly detach from the subject. Can be fixed by using context managers

# 3 Command pattern
- Encapsulates the commands
- Information for command is hidden, i.e. the client can invoke the command without knowing any details about it.
- Open/Closed principle: Easy to add new commands or additional capabilities, like validation of command or undo.
- Ideal for command line tools

# 4 Singleton pattern
- Ensure class has only one instance 
- Control access to limited resources, e.g. a database.
- Downsides classic singleton:
- Violates single responsibility priciple
- The class carries the state
- You do not use the usual way of instantiating on object.
- singleton_new:
  - __new__ is executed before __init__

# 5 Builder pattern
- Separates construction of object from its representation, so assembly is separated from its components    
- Encapsulate object construction
- Signs:
  - A lot of parameters to instantiate object
  - Both creation and definition of object in same class. In this way, what varies and what not varies are mixed.

# 6 Factory pattern
- Defines interface for creating an object
- Subclasses: 1 decide which object 2 instantiation done by sublclass
- Sign: many if/else statements to decide what objects to instantiate. Breaks 1 Open/Closed principle as main code 
  needs to be modified to add a new class. 2 Breaks dependency inversion principle as the instantiation need to 
  know about the implementation in the main program.
- Encapsulates object instantiation.
- Supports dependency inversion: clients do not depend on implementation. Depend on abstration instead.
- Simple factory pattern: one factory
- Classic factory pattern: one or more factories.

# 7 Abstract factory pattern
- Adheres to open/closed principle
- Helps with creating families of classes

# 8 Null pattern
- Provides a default object which mimics real object from class
- No longer needed to test for None
- Clients can just use the object returned.