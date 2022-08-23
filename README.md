# aws-secureboot-blob

The `aws-secureboot-blob` creates a binary blob containing
a pre-filled variable store containing the UEFI Secure Boot keys.
This binary blob can then be used to boot a AWS EC2 instance
with secure boot enabled.

See also the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-binary-blob-creation.html).

## requirements

To be able to run `aws-secureboot-blob`, some software needs
to be installed:

```
sudo apt install --yes sbsigntool efitools
sudo snap install uefivars
```

## usage

To create the binary blob, do:

```
./aws-secureboot-blob
```

That will create the blob (by default for `amd64`) file called
`aws-uefiblob.bin`.

The blob can then be used during image registration. For details how
to create a new AMI based on an existing Ubuntu AMI, see the `test-instance` script.

