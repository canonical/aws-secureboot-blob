#!/usr/bin/python3

"""
Split the signature and content from a dbxupdate.bin file (eg.
from /usr/share/secureboot/updates/dbx/ ). That splitted dbxupdate.bin.esl
file can than be used together with https://github.com/awslabs/python-uefivars

Inspired by https://www.powershellgallery.com/packages/SplitDbxContent/1.0
"""

import argparse
import sys


def _parser():
    parser = argparse.ArgumentParser(
        description='split a secureboot dbxupdate.bin')
    parser.add_argument(
        '--content', default='dbxupdate.bin.esl',
        help='the content filename to write. default: %(default)s')
    parser.add_argument(
        '--signature', default='dbxupdate.bin.p7',
        help='the signature filename to write. default: %(default)s')
    parser.add_argument(
        'dbxupdate', help='path to the dbxupdate.bin file')
    return parser


if __name__ == '__main__':
    parser = _parser()
    args = parser.parse_args()

    with open(args.dbxupdate, 'rb') as f:
        buf = f.read()
        # Identify file signature
        chop = buf[40:]

        if hex(chop[0]) != '0x30' or hex(chop[1]) != '0x82':
            print('error: can not find signature', file=sys.stderr)
            sys.exit(1)

        # Signature is known to be ASN size plus header of 4 bytes
        signature_length = (chop[2] * 256) + chop[3] + 4
        signature = chop[0:signature_length - 1]

        if signature_length > (len(buf) + 40):
            print('error: signature longer than file size', file=sys.stderr)
            sys.exit(2)

        # the dbxupdate.bin content without the signature
        content = chop[signature_length:]
        with open(args.content, 'wb') as c:
            for byte in content:
                c.write(byte.to_bytes(1, byteorder='big'))

        # the dbxupdate.bin signature without the content
        with open(args.signature, 'wb') as s:
            for byte in signature:
                s.write(byte.to_bytes(1, byteorder='big'))
