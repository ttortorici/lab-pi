# Lab Pi

This codebase allows you to set up a Raspberry Pi as a server which can be used to control devices.

It is currently set up to control a LabJack U6 as a DAC and ADC and a Prologix GPIB-USB controller.

## Dependencies

[pySerial](https://pyserial.readthedocs.io/en/latest/)
    
    pip install pyserial

[lib-usb](https://libusb.info/)
    
    sudo apt install libusb-1.0-0-dev

[Exodriver](https://labjack.com/pages/support?doc=/software-driver/installer-downloads/exodriver/) 

    git clone https://github.com/labjack/exodriver.git
    cd exodriver
    sudo ./install.sh

[LabJackPython](https://labjack.com/pages/support?doc=/software-driver/example-codewrappers/labjackpython-for-ud-exodriver-u12-windows-mac-linux/)

    pip install LabJackPython

