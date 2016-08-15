# otp
One-Time Password Generator

## Usage
~~~
$ ./otp -h
usage: otp [-h] [--version] key

One Time Password Generator

positional arguments:
  key         key or service name from ~/.otpkeys

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
~~~

## Examples
~~~
$ ./otp BEXUS3AVCUU7HYU4OZQ44WFXMULPNQB2TKQ4YCNUASPXMPEH6YAZ3IACFM5VEGUQ
OTP: 770400
~~~

## Key file ~/.otpkeys
You can save your keys to ~/.otpkeys file using ```service=key``` format, for example:

~~~
$ cat ~/.otpkeys
aws=N5VEJBTUA553BYJTTTUGS3GANKVDECG62RHVIOV2FLYR5THC726ZOIOF4SQZZ5NV
google=QYDL7HS7LHPVKX7GGYKYIP3UEYOML2IENWYQD5NHYGETBZIRWWODKQWC3PRNQ3FO
facebook=ZBSLA3KGE4PEXCEGIJ57AKJLOHW2S3ABQNOOWZVV3HOO4Q3455BOG6BRNU5M2QK4
~~~

Then you can generate OTP, by running:

~~~
$ ./otp service
~~~

Example:

~~~
$ ./otp google
google OTP: 760698

$ ./otp facebook
facebook OTP: 009176
~~~
