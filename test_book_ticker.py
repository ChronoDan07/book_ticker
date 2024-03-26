import pytest
from book_ticker import BookTickerApp

def test_extract_text():
    app = BookTickerApp("mock-pdf-1.pdf")
    assert app.extract_text(0) == "Lorem ipsum  "
    assert app.extract_text(1) == "Dolor sit amet "

def test_next_page():
    app = BookTickerApp("mock-pdf-2.pdf")
    app.current_page = 0
    app.page_display = 1
    app.next_page()
    assert app.current_page == 1
    assert app.page_display == 2

def test_previous_page():
    app = BookTickerApp("mock-pdf-2.pdf")
    app.current_page = 1
    app.page_display = 2
    app.previous_page()
    assert app.current_page == 0
    assert app.page_display == 1

def test_toggle_pause_play():
    app = BookTickerApp("mock-pdf-2.pdf")
    app.paused = False
    app.toggle_pause_play()
    assert app.paused == True
    app.toggle_pause_play()
    assert app.paused == False

def test_toggle_speed_up():
    app = BookTickerApp("mock-pdf-2.pdf")
    app.speed = 1
    app.toggle_speed_up()
    assert app.speed == 2

def test_toggle_speed_down():
    app = BookTickerApp("mock-pdf-2.pdf")
    app.speed = 2
    app.toggle_speed_down()
    assert app.speed == 1



