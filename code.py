from ADXL345_spi import Accelerometer
import time

accelerometer = Accelerometer(cs_pin=board.GP9, scl_pin=board.GP10, sda_pin=board.GP11, sdo_pin=board.GP12, spi_freq=5000000)
accelerometer.init_spi()
accelerometer.set_sampling_rate(1000)   # Hz
accelerometer.set_g_range(4)            # max measurable acceleration pm 4g
accelerometer.set_fifo_mode('bypass')
accelerometer.set_power_mode('measure')

while 1:
    buf, T = accelerometer.read_many_xyz(n=1)
    x, y, z = accelerometer.xyzbytes2g(buf)  # convert bytearray in 3 acceleration arrays (x, y, z) in g units
    print("{}\t{}\t{}".format(x, y, z))
    time.sleep(0.001)

accelerometer.set_power_mode('standby')
accelerometer.deinit_spi()  # this is necessary, otherwise if another SPI is initialized it won't work