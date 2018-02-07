# otp
Tool to generate One-Time Passwords

PyPI package: [myotp](https://pypi.python.org/pypi/myotp)

If you spot any problems or have any improvement ideas then feel free to open
an issue and I will be glad to look into it for you.

## Installation
A recommended way of installing the tool is pip install.

Once installed, a command line tool `otp` should be available in your system's PATH.

### pip install
The tool is available in PyPI and can be installed using pip:
```
$ pip install --user myotp
$ otp --help
```

### Manual install
Run the following command to install required Python modules:
```
$ git clone https://github.com/peterpakos/otp.git
$ cd otp
$ pip install --user -r requirements.txt
$ ./otp --help
```

## Usage
```
$ otp --help
usage: otp [--help] [--version] key

Tool to generate One-Time Passwords

positional arguments:
  key        key or service name from ~/.otpkeys

optional arguments:
  --help     show this help message and exit
  --version  show program's version number and exit
```

## Examples
```
$ otp BEXUS3AVCUU7HYU4OZQ44WFXMULPNQB2TKQ4YCNUASPXMPEH6YAZ3IACFM5VEGUQ
770400
```

## Key file ~/.otpkeys
You can save your keys to ~/.otpkeys file using `service=key` format, for
example:
```
$ cat ~/.otpkeys
aws=N5VEJBTUA553BYJTTTUGS3GANKVDECG62RHVIOV2FLYR5THC726ZOIOF4SQZZ5NV
google=QYDL7HS7LHPVKX7GGYKYIP3UEYOML2IENWYQD5NHYGETBZIRWWODKQWC3PRNQ3FO
facebook=ZBSLA3KGE4PEXCEGIJ57AKJLOHW2S3ABQNOOWZVV3HOO4Q3455BOG6BRNU5M2QK4
```

Then you can generate OTP, by running:
```
$ otp {service}
```

Example:
```
$ otp aws
443782

$ otp google
760698

$ otp facebook
009176
```

## Auto copy OTP to clipboard (Mac OS X)
Add the following code at the end of your `~/.bashrc` file (change path to otp if needed):
```
otp_func() {
  if code=$(/usr/local/bin/otp $1 2>&1); then
    printf "%s\n" "$code" | tee /dev/tty | pbcopy
  else
    printf "%s\n" "$code" >&2
    return 1
  fi
}
alias otp='otp_func'
```

Example:
```
$ vim ~/.bashrc
$ source ~/.bashrc
$ otp cloud
324982
```
At this point the above OTP should be in the clipboard.
