import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import portSelectUI, onOffUI, serial_connection
from arduinoLED import arduino_LED
import serial


class arduino_on_off(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.COM = ''
        self.port_select_window = portSelectUI.portSelectWindow()
        self.onOff = onOffUI.onOffWindow()

        ser = serial_connection.SerialConn()
        port_choice_list = ser.get_port_list()
        self.port_select_window.ui.com_select.clear()
        self.port_select_window.ui.com_select.addItems(port_choice_list)

        self.port_select_window.ui.continue_COM_button.clicked.connect(self.continue_button)
        #self.onOff.ui.onOffSlider.valueChanged.connect(self.submit_button)
        self.onOff.ui.submitButton.clicked.connect(self.submit_button)
        self.onOff.ui.backButton.clicked.connect(self.go_back_button)

        #self.port_select_window.ui.label_3.setText("Hello")


    def go_back_button(self):

        self.onOff.hide_window()
        self.port_select_window.show_window()


    def continue_button(self):
        self.COM = self.port_select_window.ui.com_select.currentText()
        print(self.COM)
        self.show_onOff_window()
        self.port_select_window.hide_window()

    def submit_button(self):
        data = self.onOff.ui.onOffSlider.value()

        if(data == 1):
            data = str('on')
        else:
            data = str('off')

        try:
            arduino = arduino_LED()
            arduino.arduino_value(data, self.COM)
        except Exception as e:
            print(e)

        if (data == 'on'):
            self.onOff.ui.led_status.setText("LED: On")
        else:
            self.onOff.ui.led_status.setText("LED: Off")

    def show_portSelect_window(self):
        self.port_select_window.show()

    def show_onOff_window(self):
        self.onOff.show()

    def initialize_and_show(self):
        self.show_portSelect_window()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    arduino_window = arduino_on_off()
    arduino_window.initialize_and_show()
    sys.exit(app.exec_())
