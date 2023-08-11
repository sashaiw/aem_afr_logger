# AEM AFR logger
Module for logging AFR from AEM Wideband UEGO Air/Fuel controllers over USB serial. Outputs to CSV.

**THIS IS NOT TESTED YET SINCE I DO NOT HAVE ACCESS TO THE HARDWARE.**

## Installation
```commandline
git clone https://github.com/sashaiw/aem-afr-logger.git
python3 -m pip install -r requirements.txt
```

## Usage
```commandline
python3 -m aem_afr_logger [-h] -p PORT [-r [RATE]] [-o [OUTPUT]]
```

### Options
 
| Option                             | Description                     |
|------------------------------------|---------------------------------|
| `-h`, `--help`                     | show this help message and exit |
| `-p PORT`, `--port PORT`           | Serial port for sensor          |
| `-r [RATE]`, `--rate [RATE]`       | Baud rate                       |
| `-o [OUTPUT]`, `--output [OUTPUT]` | Output CSV to log to            |


### Example
```commandline
python3 -m aem_afr_logger --port /dev/ttyUSB0 --output legacy_rotated_dyno_run.csv
```