# BOOK TICKER APP
#### Video Demo:  <URL HERE>
#### Description:
The Book Ticker App is a simple Python application designed for reading text documents, particularly PDF files, in a ticker-like manner. The app presents the text content of a PDF document one page at a time, scrolling horizontally across the screen like a news ticker. This scrolling functionality aims to provide a dynamic reading experience, especially for users who prefer consuming content at a steady pace.
#### Files and Functionality:

#### project.py:
This file contains the main code for the Book Ticker App.
It defines the BookTickerApp class, which encapsulates the application's functionality.
The BookTickerApp class initializes the GUI window, handles PDF file loading, extracts text from the PDF, and implements features such as navigating between pages, controlling playback speed, and toggling play/pause functionality.
The class utilizes the Tkinter library for creating the graphical user interface.
It also includes methods for updating the displayed text, moving the text horizontally for the ticker effect, and centering the application window on the screen.

#### test_project.py:
This file contains unit tests for the functions implemented in project.py.
Each test function corresponds to a specific method or functionality in the BookTickerApp class.
The tests verify the correctness of key features such as text extraction, page navigation, play/pause control, and speed adjustment.

#### Design Choices:
##### Use of Tkinter:
Tkinter was chosen as the GUI toolkit for its simplicity and ease of use, making it suitable for a straightforward application like the Book Ticker App.

#### Class-based Implementation:
The decision to organize the code into a class-based structure was made to include related functionality within the BookTickerApp class.
This approach promotes code organization, reusability, and most importantly easier testability.

#### Ticker-like Reading Experience:
The horizontal scrolling text feature was implemented to simulate a ticker-like reading experience.
By presenting text content in a continuous scrolling manner, users can focus on reading without the distraction of manual page turns.
This design choice aims to enhance user engagement and provide an alternative reading mode for digital text documents.

#### Unit Testing:
Unit tests were included to ensure the correctness of the application's functionality.
By systematically testing individual components and methods, potential bugs and errors can be identified and addressed.

Overall, the Book Ticker App offers a novel way to consume textual content from PDF documents, catering to users who prefer a dynamic and continuous reading experience. With its intuitive interface and customizable features, the app provides a convenient solution for users seeking an alternative reading mode.
