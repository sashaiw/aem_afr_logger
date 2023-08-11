import argparse
import csv
import datetime
import serial

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
    Log AFR/lambda from AEM Wideband UEGO Air/Fuel controllers over USB serial_logger.
    ''')
    parser.add_argument('-p', '--port', help='Serial port for sensor', required=True)
    parser.add_argument('-r', '--rate', nargs='?', help='Baud rate', type=int, default=9600)
    parser.add_argument('-o', '--output', nargs='?', help='Output CSV to log to', default='output.csv')

    args = parser.parse_args()

    # configure serial port
    try:
        print(f'Attempting to initialize logger on {args.port} at {args.rate} baud...')
        ser = serial.Serial(args.port, args.rate, timeout=1)
        print(f'Connected! Logging to {args.output}...')

        with open(args.output, 'a') as output:
            # set up CSV logger
            writer = csv.writer(output, delimiter=',', quoting=csv.QUOTE_NONE)

            # log whenever a serial message is received
            while True:
                try:
                    data = ser.readline()
                    timestamp = datetime.datetime.now()
                    writer.writerow([timestamp, data.strip()])

                # user has exited program
                except KeyboardInterrupt:
                    print(f'\nOutput written to {args.output}.')
                    ser.close()
                    break

                # something went wrong with the serial connection
                except serial.serialutil.SerialException as e:
                    print(f'Serial error: {e}')
                    break

    except serial.serialutil.SerialException as e:
        print(f'Failed to connect to serial port: {e}')
