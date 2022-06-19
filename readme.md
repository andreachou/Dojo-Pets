# Dojo Pets

# Coding Dojo Practice 06.19.2022

<br/>

For this assignment, you'll be asked to create a Ninja class and a Pet class. Your Ninjas will be able to have a pet - and you can even practice using inheritance by creating sub-classes of pets, if you're ready to stretch yourself!

## **Ninja Class**

<br/>

**Attributes**

* first_name
* last_name
* pet
* treats
* pet_food

**Methods**

* walk()
* feed()
* bathe()

```py
class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
        	
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method

```

## **Pet Class**

<br/>

**Attributes**

* name
* type
* tricks
* health
* energy

**Methods**

* sleep()
* eat()
* play()
* noise()

```py
class Pet:
    # implement __init__( name , type , tricks ):
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound
```