# cse210-04
# Greed Game 
# **Overview:**

- Greed is a game in which the player seeks to gather as many falling gems as possible.
- The game continues until the player decides they are done!

## **Rules:**

_Greed is played according to the following rules._

- Gems (\*) and rocks (o) randomly appear and fall from the top of the screen.
- The player (#) can move left or right along the bottom of the screen.
- If the player touches a gem, they earn a point.
- If the player touches a rock, they lose a point.
- Gems and rocks are removed when the player touches them.
- The game continues until the player closes the window.

**Requirements:**

- The program contains a README file.
- The program contains 3 folders labeled images, keyboard_support, and sprites. 
- The program contains eight classes.
- The class Director will inherit traits from the class DrawScreen, and the class player_movement will inherit traits from the class Keyboard.
- Each module, class and method contains a corresponding comment.
- The game remains generally true to the order of play described earlier.

**Project Structure:**
_The project files are the following:_

- +-- keyboard_input.py 
- +-- player_movement.py 
- +-- gem.py 
- +-- rock.py 
- +-- player.py 
- +-- director.py 
- +-- draw_screen.py 
- +-- main.py 
- +-- score.py 
- +-- color.py 
- +-- gem.png
- +-- rock.png 
- +-- player.png
- +-- pycache
- +-- README.md

---

_The project files are organized in folders as follows:_

```
root                                (project root folder)
+-- images                          (images for game)
+-- keyboard_support                (specific game classes)
+-- sprites                         (specific game classes)
+-- director.py                     (specific game classes)
+-- draw_screen.py                  (specific game classes)
+-- main.py                         (entry point for program)
+-- score.py                        (specific game classes)
+-- README.md                       (general info)
```

**Required Technologies:**

- Python 3.8.0 or greater
- Pygame

## **Authors: (Team E)**

- Mazzarella-Woelzl, Alison Reed (maz12005@byui.edu)
- Saenz, Paula (sae21002@byui.edu)
- Ogboanoh, Richard Oshiomole Ephraim (ogb22001@byui.edu)
- Diab, Garren Mark (dia22004@byui.edu)
