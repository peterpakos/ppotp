# ppotp
Tool to generate One-Time Passwords and copy them to clipboard

PyPI package: [ppotp](https://pypi.python.org/pypi/ppotp)

## Installation
A recommended way of installing the tool is pip install.

Once installed, a command line tool `otp` should be available in your system's PATH.

### pip install
The tool is available in PyPI and can be installed using pip:
```
$ pip install --user ppotp
$ otp --help
```

## Usage
```
$ otp --help
usage: otp [--version] [--help] [--debug] [-l] [key]

Tool to generate One-Time Passwords and copy them to clipboard

positional arguments:
  key         key or service name from ~/.otpkeys

optional arguments:
  --version   show program's version number and exit
  --help      show this help message and exit
  --debug     debugging mode
  -l, --list  list services from ~/.otpkeys
```

## Examples
```
$ otp BEXUS3AVCUU7HYU4OZQ44WFXMULPNQB2TKQ4YCNUASPXMPEH6YAZ3IACFM5VEGUQ
770400
```

## Key file ~/.otpkeys
You can save your keys to `~/.otpkeys` file using `service=key` format, for
example:
```
$ cat ~/.otpkeys
aws=N5VEJBTUA553BYJTTTUGS3GANKVDECG62RHVIOV2FLYR5THC726ZOIOF4SQZZ5NV
google=QYDL7HS7LHPVKX7GGYKYIP3UEYOML2IENWYQD5NHYGETBZIRWWODKQWC3PRNQ3FO
facebook=ZBSLA3KGE4PEXCEGIJ57AKJLOHW2S3ABQNOOWZVV3HOO4Q3455BOG6BRNU5M2QK4
```

To list services defined in `~/.otpkeys`:
```
$ otp --list
aws
google
facebook
```

To generate OTP for a service:
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

## Auto copy OTP to clipboard
The tool attempts to automatically copy successfully generated code to the
clipboard. It uses [pyperclip](https://pypi.org/project/pyperclip/) module
for cross-platform copying text to the clipboard. 

Example:
```
$ otp cloud
324982
```
At this point, provided your system supports it, the above OTP should be in
the clipboard.

### Copy to clipboard issue
Pyperclip uses various mechanisms to copy text to the clipboard. If your system
is missing them, you may see a debug message that says:
```
Pyperclip could not find a copy/paste mechanism for your system.
For more information, please visit https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error
```

Currently, this error should only appear on Linux (not Windows or Mac).

Please check [this guide](https://pyperclip.readthedocs.io/en/latest/#not-implemented-error)
for more information on how to fix this.
