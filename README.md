# face-detection-linked-list

## Linked List

The linked list class defined in the code is a singly linked list with function like append remove and insert. Append adds a node to the end of the list. Insert adds a node at a certain location and remove deletes a certain node.
The create_cycle function creates a loop in the linked list such that the last node is linked to a previous node. The locate_cycle function finds the node that the last node is linked in case there is a loop in the list. The display and the display_cycle functions display all the nodes in the list and the loop respectively. The length and the loop_length function find the length of the list and the loop respectively.

## Face Detection

For detecting the face in the photo I used the opencv haarcascade frontal face detector. This returns rectanguar coordinates for the location of the face. I made the scaling factor 1.1 and the min no. of neighbors parameter as 5. For blurring the image I used a averaging kernal of size 25x25. Two samples of what it can do is given below. 

![Alt text](https://github.com/RishalAggarwal/face-detection-linked-list/blob/master/face%20detec%20%2B%20linked%20list/face_detect1.png) 

![Alt text](https://github.com/RishalAggarwal/face-detection-linked-list/blob/master/face%20detec%20%2B%20linked%20list/face_detect2.png)
