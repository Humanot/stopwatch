from datetime import datetime
import time

def test_start_minute(app):
    if not app.process.write_current_time() == app.process.convert_time('00:00.00'):
        app.process.reset()
    app.process.start()
    app.process.validate_one_minute('01:00.00')

def test_stop_current(app):
    if not app.process.write_current_time() == app.process.convert_time('00:00.00'):
        app.process.reset()
    app.process.start()
    time.sleep(5)
    app.process.start()
    timer = app.process.stop_time()
    time.sleep(5)
    timer_2 = app.process.stop_time()

    if not timer == timer_2:
        print(timer, timer_2)
        raise Exception('Failed')

def test_reset_time(app):
    if app.process.write_current_time() == app.process.convert_time('00:00.00'):
        app.process.start()
    time.sleep(5)
    timer = app.process.reset()

    if not timer == app.process.convert_time('00:00.00'):
        print(timer)
        raise Exception('Failed')



