# Virtual Grocery Market POS
#### Video Demo:  https://youtu.be/R-deHdykcPc
#### Description:
Virtual Grocery Market POS is a program that helps users (i.e., customers) with their shopping experience at a grocery market (or any other shopping place as we will explain later). Users will have the ability to view and manage their cart simultaneously during their shopping experience. This program facilitates the shopping process, making it simpler and faster.
I chose to build a command-line program, with the intention of developing it later with more features and visuals if needed.

## Project Files:
* **`project.py`**: This file contains the main project with all its core components, including classes and root-level functions.
* **`test_project.py`**: This file contains test cases for three of the root-level functions other than the `main()` function in **`project.py`**. It uses the `pytest` library to evaluate the constant return value of a function. It also tests three different scenarios for the other two functions, proving the program correctly rejects invalid inputs and accepts valid ones.
* **`requirements.txt`**: This file contains external libraries needed to run the main program.

## Architecture and Design Choices:
* **Object-Oriented Programming (OOP):**
In the main program, I have implemented Object-Oriented Programming concepts. I created two classes, one named `Item`, which represents each item shown for sale, and another for the `Cart` which represents a dynamic cart changing according to user inputs and needs.
The `Item` class works as a blueprint for any item shown for sale, where each item should have a number (ID), name, type (which represents how it's sold), price, and quantity or amount whose default value is zero at the beginning.
The `Cart` class manages the current items added or removed from the cart, as well as the total price to be paid. When printed, it shows each item added to the cart multiplied by the amount or quantity chosen by the user and its price.
The algorithm behind showing current items in the cart and calculating the total price lies in creating a list of current objects inside the cart, where each object inside the list holds all properties (attributes) needed to represent it anywhere. The created list is the first place changed when changing any item inside the cart. We can use any value of the attributes assigned to the object to show its quantity or amount, calculate the price of each item and the total price by accumulating it in a single variable.

I chose to implement classes rather than just dictionaries or lists for the whole program to be organised and versatile in properties of each item shown. Since all items shown are similar in properties (attributes), the best way to represent them is by creating a class for them.

* **Handling Variable Units:**
For all items shown, there is an attribute called `unit_type` which represents how the item shown will be sold, either per unit or per 1000 grams. I implemented logic so that if this attribute is "/1000gm", it calculates the user's input amount as a fraction of 1000 grams and multiplies it by the price of 1000 grams. Otherwise, the program multiplies the user's input quantity by the unit price.

* **Menu Navigation:**
In the main menu (features menu), there are several options (features) to choose from, where the user inputs a number from the shown screen which is then matched with one of the available features to open a sub-menu. For example, in the addition feature, the user chooses an item to add to the cart and specifies its quantity or amount.

At each stage (the main menu, sub-menus, and item selection), a loop continuously prompts the user if their input is invalid. If valid, the loop breaks to either execute an action or return to the previous stage. Also, in the sub-menu and whatever comes after it, I assigned '0' as a button to return, also by breaking the current loop.

If the user's input is invalid, the screen prompts them to try again with a clear, understandable error message.

Breaking the loop automatically to return after finishing a process and handling errors that arise from a user's invalid input provide a more user-friendly experience, which is an important aspect of the program.

## Testing with Pytest:
I created a test file to test some of the root-level functions other than the `main` function.

I checked that the main menu (features menu) is printed correctly. Then, I tested the validation processes of the user's input in some functions using `pytest`'s built-in `monkeypatch` with the `iter()` function to simulate the behaviour of the `input()` function for several input cases to make sure the validation process is working well.

## How to Run:
1. Run `pip install -r requirements.txt`
2. Run `python project.py`
3. Follow the on-screen menu prompts to add items to the cart and checkout.

## Generalization of the code:
In the description, I have stated that the program helps the user with their shopping experience in any shop, not only a grocery market, and that's because of structuring the program using **Object-Oriented Programming (OOP)**.

Since all items sold in a marketplace have nearly the same properties (attributes) like a number (ID), name, price, etc., we need something like a blueprint or a mold that has fixed properties for everything sold, with different values depending on the item sold, and that's where OOP excels. OOP creates the blueprint we need to describe any product and apply it to our chosen products by instantiating as many objects (products to sell) as we want from this class, assigning the value of each property according to each specific object. After instantiating the required objects, I placed them together in a list, which serves as a menu of available objects to sell.

By using OOP, we can apply the same idea to any market, not only grocery markets, which makes the program usable in many applications as a POS.
