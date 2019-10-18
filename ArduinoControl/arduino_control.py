import serial

# serial communication params
SERIAL_PORT = "/dev/ttyUSB0"
DEFAULT_BAUD_RATE = 9600

class ArduinoControlService:

    def __init__(self, port=SERIAL_PORT, baud_rate=DEFAULT_BAUD_RATE):
        self._controller = serial.Serial(port, baud_rate)
        self._state = 0

    # public methods
    def get_state(self):
        """
        Returns output state.
        :return: output state 0/1
        """
        return self._state

    def control(self, state):
        """
        Control arduino writing through serial port. Output state is written as str.
        :param state: value that determines output state - one of the following values (`switch`, `power off`,
        `power on`) (str)
        :return: void method
        """
        print("Calling arduino control method with params: [state = {}]".format(state))
        self._set_state(state)
        self._controller.write(str(self._state).encode())

    def dispose(self):
        """
        Closes the serial port.
        :return: void method
        """
        self._controller.close()

    # private methods
    def _state_switch(self):
        """
        Switches the output state.
        :return: void method
        """
        self._state = 1 - self._state

    def _turn_on(self):
        """
        Sets output state to high.
        :return: void method
        """
        self._state = 1

    def _turn_off(self):
        """
        Sets output state to low.
        :return: void method
        """
        self._state = 0

    def _set_state(self, state):
        """
        Sets output state based on state value.
        :param state: value that determines output state - one of the following values (`switch`, `power off`,
        `power on`) (str)
        :return: void method
        """
        if state == "switch":
            self._state_switch()
        elif state == "power off":
            self._turn_off()
        elif state == "power on":
            self._turn_on()
        else:
            raise ValueError("Invalid state.")
        print("Current relay state = {}".format(self.get_state()))


import time

ar_s = ArduinoControlService()
for i in range(6):
    ar_s.control("switch")
    print(ar_s.get_state())
    time.sleep(3)

ar_s.control("power on")
ar_s.control("power off")
ar_s.dispose()